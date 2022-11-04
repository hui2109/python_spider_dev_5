# Scrapy管道



在上一小节中, 我们初步掌握了Scrapy的基本运行流程以及基本开发流程. 本节继续讨论关于Scrapy更多的内容. 

## 一. 关于管道

上一节内容, 我们已经可以从spider中提取到数据. 然后通过引擎将数据传递给pipeline, 那么在pipeline中如何对数据进行保存呢? 我们主要针对四种数据存储展开讲解. 

前三个案例以https://match.lottery.sina.com.cn/lotto/pc_zst/index?lottoType=ssq&actionType=chzs为案例基础. 最后一个以https://desk.zol.com.cn/dongman/为案例基础. 

### 1. csv文件写入

​		写入文件是一个非常简单的事情. 直接在pipeline中开启文件即可. 但这里要说明的是. 如果我们只在process_item中进行处理文件是不够优雅的.  总不能有一条数据就open一次吧

```python
class CaipiaoFilePipeline:
    
    def process_item(self, item, spider):
        with open("caipiao.txt", mode="a", encoding='utf-8') as f:
            # 写入文件
            f.write(f"{item['qihao']}, {'_'.join(item['red_ball'])}, {'_'.join(item['blue_ball'])}\n")
        return item
```

​		我们希望的是, 能不能打开一个文件, 然后就用这一个文件句柄来完成数据的保存. 答案是可以的. 我们可以在pipeline中创建两个方法, 一个是open_spider(), 另一个是close_spider(). 看名字也能明白其含义: 

​		open_spider(), 在爬虫开始的时候执行一次
​		close_spider(), 在爬虫结束的时候执行一次

​		有了这俩货, 我们就可以很简单的去处理这个问题

```python
class CaipiaoFilePipeline:

    def open_spider(self, spider):
        self.f = open("caipiao.txt", mode="a", encoding='utf-8')

    def close_spider(self, spider):
        if self.f:
            self.f.close()

    def process_item(self, item, spider):
        # 写入文件
        self.f.write(f"{item['qihao']}, {'_'.join(item['red_ball'])}, {'_'.join(item['blue_ball'])}\n")
        return item
```

​		在爬虫开始的时候打开一个文件, 在爬虫结束的时候关闭这个文件. 满分~

​		对了, 别忘了设置settings

```python
ITEM_PIPELINES = {
   'caipiao.pipelines.CaipiaoFilePipeline': 300,
}
```



### 2. mysql数据库写入

​		有了上面的示例, 写入数据库其实也就很顺其自然了, 首先, 在open_spider中创建好数据库连接. 在close_spider中关闭链接. 在proccess_item中对数据进行保存工作. 

先把mysql相关设置丢到settings里

```python
# MYSQL配置信息
MYSQL_CONFIG = {
   "host": "localhost",
   "port": 3306,
   "user": "root",
   "password": "test123456",
   "database": "spider",
}
```



```python
from caipiao.settings import MYSQL_CONFIG as mysql
import pymysql

class CaipiaoMySQLPipeline:

    def open_spider(self, spider):
        self.conn = pymysql.connect(host=mysql["host"], port=mysql["port"], user=mysql["user"], password=mysql["password"], database=mysql["database"])

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        # 写入文件
        try:
            cursor = self.conn.cursor()
            sql = "insert into caipiao(qihao, red, blue) values(%s, %s, %s)"
            red = ",".join(item['red_ball'])
            blue = ",".join(item['blue_ball'])
            cursor.execute(sql, (item['qihao'], red, blue))
            self.conn.commit()
            spider.logger.info(f"保存数据{item}")
        except Exception as e:
            self.conn.rollback()
            spider.logger.error(f"保存数据库失败!", e, f"数据是: {item}")  # 记录错误日志
        return item

```

别忘了把pipeline设置一下

```python
ITEM_PIPELINES = {
   'caipiao.pipelines.CaipiaoMySQLPipeline': 301,
}
```



### 3. mongodb数据库写入

​		mongodb数据库写入和mysql写入如出一辙...不废话直接上代码吧

```python
MONGO_CONFIG = {
   "host": "localhost",
   "port": 27017,
   #'has_user': True,
   #'user': "python_admin",
   #"password": "123456",
   "db": "python"
}
```



```python
from caipiao.settings import MONGO_CONFIG as mongo
import pymongo

class CaipiaoMongoDBPipeline:
    def open_spider(self, spider):
        client = pymongo.MongoClient(host=mongo['host'],
                                     port=mongo['port'])
        db = client[mongo['db']]
        #if mongo['has_user']:
        #    db.authenticate(mongo['user'], mongo['password'])
        self.client = client  #  你们那里不用这么麻烦. 
        self.collection = db['caipiao']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert({"qihao": item['qihao'], 'red': item["red_ball"], 'blue': item['blue_ball']})
        return item
```

```python
ITEM_PIPELINES = {
    # 三个管道可以共存~
   'caipiao.pipelines.CaipiaoFilePipeline': 300,
   'caipiao.pipelines.CaipiaoMySQLPipeline': 301,
   'caipiao.pipelines.CaipiaoMongoDBPipeline': 302,
}
```



### 4. 文件保存

接下来我们来尝试使用scrapy来下载一些图片, 看看效果如何. 

```先安装模块
pip install pillow
```

首先, 随便找个图片网站(安排好的). https://desk.zol.com.cn/dongman/. 可以去看看

接下来. 创建好项目, 完善spider, 注意看yield scrapy.Request()

```python
import scrapy
from urllib.parse import urljoin


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['https://desk.zol.com.cn/dongman/']

    def parse(self, resp, **kwargs):  # scrapy自动执行这个parse -> 解析数据
        # print(resp.text)
        # 1. 拿到详情页的url
        a_list = resp.xpath("//*[@class='pic-list2  clearfix']/li/a")
        for a in a_list:
            href = a.xpath("./@href").extract_first()
            if href.endswith(".exe"):
                continue

            # href = urljoin(resp.url, href)  # 这个拼接才是没问题的.
            # print(resp.url)  # resp.url   当前这个响应是请求的哪个url回来的.
            # print(href)
            # 仅限于scrapy
            href = resp.urljoin(href)  # resp.url 和你要拼接的东西
            # print(href)
            # 2. 请求到详情页. 拿到图片的下载地址

            # 发送一个新的请求
            # 返回一个新的请求对象
            # 我们需要在请求对象中, 给出至少以下内容(spider中)
            # url  -> 请求的url
            # method -> 请求方式
            # callback -> 请求成功后.得到了响应之后. 如何解析(parse), 把解析函数名字放进去
            yield scrapy.Request(
                url=href,
                method="get",
                # 当前url返回之后.自动执行的那个解析函数
                callback=self.suibianqimignzi,
            )

    def suibianqimignzi(self, resp, **kwargs):
        # 在这里得到的响应就是url=href返回的响应
        img_src = resp.xpath("//*[@id='bigImg']/@src").extract_first()
        # print(img_src)
        yield {"img_src": img_src}

```

​		关于Request()的参数:
​			url: 请求地址
​            method: 请求方式
​            callback: 回调函数
​            errback: 报错回调
​            dont_filter: 默认False, 表示"不过滤", 该请求会重新进行发送
​            headers: 请求头. 
​            cookies: cookie信息

​		接下来就是下载问题了. 如何在pipeline中下载一张图片呢? Scrapy早就帮你准备好了. 在Scrapy中有一个ImagesPipeline可以实现自动图片下载功能. 

```python
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
from itemadapter import ItemAdapter
# ImagesPipeline 图片专用的管道
from scrapy.pipelines.images import ImagesPipeline


class TuPipeline:
    def process_item(self, item, spider):
        print(item['img_src'])
        # 一个存储方案.
        # import requests
        # resp = requests.get(img_src)
        # resp.content
        return item

# scrapy的方案
class MyTuPipeline(ImagesPipeline):
    # 1. 发送请求(下载图片, 文件, 视频,xxx)
    def get_media_requests(self, item, info):
        url = item['img_src']
        yield scrapy.Request(url=url, meta={"sss": url})  # 直接返回一个请求对象即可

    # 2. 图片的存储路径
    # 完整的路径: IMAGES_STORE + file_path()的返回值
    # 在这个过程中. 文件夹自动创建
    def file_path(self, request, response=None, info=None, *, item=None):
        # 可以准备文件夹
        img_path = "dongman/imgs/kunmo/libaojun/liyijia"
        # 准备文件名字
        # 坑: response.url 没办法正常使用
        # file_name = response.url.split("/")[-1]  # 直接用响应对象拿到url
        # print("response:", file_name)
        file_name = item['img_src'].split("/")[-1]  # 用item拿到url
        print("item:", file_name)
        file_name = request.meta['sss'].split("/")[-1]
        print("meta:", file_name)

        real_path = img_path + "/" + file_name  # 文件夹路径拼接
        return real_path  # 返回文件存储路径即可

    # 3. 可能需要对item进行更新
    def item_completed(self, results, item, info):
        # print(results)
        for r in results:
            print(r[1]['path'])
        return item  # 一定要return item 把数据传递给下一个管道


```

最后, 需要在settings中设置以下内容:

```python
LOG_LEVEL = "WARNING"

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {
   'tu.pipelines.TuPipeline': 300,
   'tu.pipelines.MyTuPipeline': 301,
}

MEDIA_ALLOW_REDIRECTS = True
# 下载图片. 必须要给出一个配置
# 总路径配置
IMAGES_STORE = "./qiaofu"
```
