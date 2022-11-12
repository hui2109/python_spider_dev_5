# Scrapy抓取全网站数据

## 一. 使用常规Spider

我们把目光对准汽车之家. 抓取二手车信息.

注意, 汽车之家的访问频率要控制一下. 要不然会跳验证的. 

```python
DOWNLOAD_DELAY = 3
```

```python
class ErshouSpider(scrapy.Spider):
    name = 'ershou'
    allowed_domains = ['che168.com']
    start_urls = ['https://www.che168.com/china/a0_0msdgscncgpi1ltocsp1exx0/']

    def parse(self, resp, **kwargs):
        # print(resp.text)
        # 链接提取器
        le = LinkExtractor(restrict_xpaths=("//ul[@class='viewlist_ul']/li/a",), deny_domains=("topicm.che168.com",) )
        links = le.extract_links(resp)
        for link in links:
            yield scrapy.Request(
                url=link.url,
                callback=self.parse_detail
            )
        # 翻页功能
        le2 = LinkExtractor(restrict_xpaths=("//div[@id='listpagination']/a",))
        pages = le2.extract_links(resp)
        for page in pages:
            yield scrapy.Request(url=page.url, callback=self.parse)

    def parse_detail(self, resp, **kwargs):
        title = resp.xpath('/html/body/div[5]/div[2]/h3/text()').extract_first()
        print(title)

```

LinkExtractor: 链接提取器. 可以非常方便的帮助我们从一个响应页面中提取到url链接. 我们只需要提前定义好规则即可. 

参数: 

​	allow, 接收一堆正则表达式, 可以提取出符合该正则的链接
​	deny, 接收一堆正则表达式, 可以剔除符合该正则的链接
​	allow_domains: 接收一堆域名, 符合里面的域名的链接被提取
​	deny_domains: 接收一堆域名, 剔除不符合该域名的链接
​	restrict_xpaths: 接收一堆xpath, 可以提取符合要求xpath的链接
​	restrict_css: 接收一堆css选择器, 可以提取符合要求的css选择器的链接
​	tags: 接收一堆标签名, 从某个标签中提取链接, 默认a, area
​	attrs: 接收一堆属性名, 从某个属性中提取链接, 默认href

值得注意的, ==在提取到的url中, 是有重复的内容的. 但是我们不用管. scrapy会自动帮我们过滤掉重复的url请求.== 



## 二. 使用CrawlSpider

在scrapy中提供了CrawlSpider来完成全站数据抓取. 

1. 创建项目

    ```
    scrapy startproject qichezhijia
    ```

    

2. 进入项目

    ```
    cd qichezhijia
    ```

    

3. 创建爬虫(CrawlSpider)

    ```
    scrapy genspider -t crawl ershouche che168.com
    ```

    

    和以往的爬虫不同. 该爬虫需要用到crawl的模板来创建爬虫. 

4. 修改spider中的rules和回调函数

    ```python
    class ErshoucheSpider(CrawlSpider):
        name = 'ershouche'
        allowed_domains = ['che168.com', 'autohome.com.cn']
        start_urls = ['https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp1exx0/']
    
        le = LinkExtractor(restrict_xpaths=("//ul[@class='viewlist_ul']/li/a",), deny_domains=("topicm.che168.com",) )
        le1 = LinkExtractor(restrict_xpaths=("//div[@id='listpagination']/a",))
        rules = (
            Rule(le1, follow=True),  # 单纯为了做分页
            Rule(le, callback='parse_item', follow=False), # 单纯提取数据
        )
    
        def parse_item(self, response):
            print(response.url)
    ```

    CrawlSpider的工作流程. 

    前期和普通的spider是一致的. 在第一次请求回来之后. 会自动的将返回的response按照rules中订制的规则来提取链接. 并进一步执行callback中的回调. 如果follow是True, 则继续在响应的内容中继续使用该规则提取链接.  相当于在parse中的scrapy.request(xxx, callback=self.parse)

    
