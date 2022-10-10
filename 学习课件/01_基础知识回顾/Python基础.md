# 第一节,  爬虫入门+python基础内容回顾. 



## 一. 关于上课(重要)

通常情况下, 五期课程, 前期每周三, 周五, 晚上8点上课, 后期. 会根据课程进度调整到每周一, 周三, 周五.  各位一定要注意群公告. 有些人习惯性把群屏蔽.  请把"樵夫"设置为关注的群成员.  这样就能避免遗漏掉最新的通知. 

关于答疑, 写程序嘛, 出问题很正常, 不要慌. 先阅读错误信息.  找到错误信息中的关键点. 第一个, 是最后一句错误信息, 第二个, 是行号. 
最后一句错误信息一般都会很直接的告诉你. 出了什么问题. 而行号, 能告诉你, 哪里出问题了. 再去结合你写的代码. 去感觉, 去猜测, 哪里会出问题. 慢慢的培养自己解决问题的能力. 这个很重要. 

关于伸手党, 之前我没注意过这东西. 后来发现. 有人接单, 然后发给我. 让我给做. 做完了. 他去赚钱. 这个商业思维很6. 兄弟们. 不能这么干啊. 这是要搞死我的节奏. 所以, 这种伸手党, 不学, 只求结果的. 一概拒绝. 



如果你截图截的是代码。 那么请带上行号。 

樵夫的诉求。 尽量不要用手机拍照了。 



## 二. 关于爬虫的特殊性

爬虫是一个很蛋疼的东西, 可能今天讲解的案例. 明天就失效了. 所以, 不要死盯着一个网站干.  要学会**<u>见招拆招</u>**(爬虫的灵魂)

爬虫程序如果编写的不够完善. 访问频率过高. 很有可能会对服务器造成毁灭性打击, 所以, 不要死盯着一个网站干. 请放慢你爬取的速度. 为你好, 也为网站好.  

腾讯, 阿里, 字节的网站, 反爬手段很残忍. 新手不要去挑战这种大厂. 等你有实力了. 慢慢研究(哪个都要研究很久....)
gov的网站, 非必要, 不爬取. 非要爬取. 请一定降低访问频率. 为你好....

不要以为gov的网站好欺负. 那是地方性的网站. 中央的很多重要网站都有非常强力的防护措施(瑞数等...) 这种. 愿意搞的. 自己研究. 樵夫搞不定....

网站的多变性: 这个是爬虫的魅力. 我们要全方位的去思考. 就像找漏洞一样. 思维逻辑不可能是固定的. 达到目的即可. 不要死磕牛角尖. 要不然, 你会死的很惨....



## 三. 必须要掌握的py基础

### 3.1 基础语法相关

 1. if条件判断

    ```python
    if 条件:
        # 事情1
    else:
        # 事情2
        
    当你需要判断的时候. 就去写if. 
    
    ```

    上面就是if的最基础的语法规则. 含义是, 如果条件为真, 去执行`事情1`, 如果条件不真, 去执行`事情2`. 这东西. 我就不拆开聊了. 关于if. 你要记住的事情是, `它是用来做条件判断的`. 以后你的程序里,  如果需要条件判断了. 就用它....

    举例,

    在写爬虫的时候. 我们会遇到这样的两种情况 

    情况一, 数据里有一些我们并不需要的内容

    ```python
    data = "10,英雄本色,1500万"   # 正常你需要的数据
    data = "11,-,-"  # 你不需要的数据
    
    # 伪代码, 理解含义(思路)
    if data里有你需要的数据:
    	处理数据
    else:
     	再见
    
    ```

    baidu.com

    第一页的内容和第二页的内容

    网页有可能会有多种页面结构

    小伙伴1. 逼着自己写一个提取器。 去适应不同的页面结构  -> 难度系数(非常高)

    小伙伴2. 写两个提取器, 不同的提取器去爬取不同的网页

    

    情况二, 页面结构不统一, 会有两种页面结构

    ```python
    # 伪代码, 理解含义(思路)
    提取器1 = xxxx  #  用来提取页面中内容的
    提取器2 = xxxxxx
    
    # 页面有可能是不规则的。 
    结果1 = 提取器1.提取(页面)
    if 结果1:
        有结果. 存起来
    else:
        没有结果. 
        结果2 = 提取器2.提取(页面)
    ```

    相信我, 上面的逻辑并不难. 但是, 到了后面很多小伙伴容易踩坑. 我们完全没必要用一个提取器获取所有的数据. 完全没必要.....

    

 2. while循环
    关于循环, 我们必须要知道一个事情. 

    ```python
    while 条件:
        循环体
    ```

    如果条件为真, 就执行循环体, 然后再次判断条件.....直到条件为假. 结束循环. 

    反复的执行一段代码

    

 3. 关于True和False

    True, 是真的意思. 翻译成人话:  对的, OK, 没毛病. 确定

    False, 是假的意思. 翻译成人话: 不对劲, 错误, No. 有瑕疵. 不对劲

    这个应该都能看懂. 

    但是下面这个, 需要各位去记住

    ```python
    # 几乎所有能表示为空的东西. 都可以认为是False
    print(bool(0))
    print(bool(""))
    print(bool([]))
    print(bool({}))
    print(bool(set()))
    print(bool(tuple()))
    print(bool(None))
    # 上面这一坨全是False, 相反的. 都是真. 利用这个特性. 我们可以有以下的一些写法
    
    # 伪代码, 理解逻辑. 
    结果 = 提取器.提取(页面)
    if 结果:
        有结果. 我要保存结果
    else:
        没结果.......
    ```

    

### 3.2  字符串

​	字符串在`爬虫`里. 必须要知道的几个操作:

  1. 索引和切片
     索引, 就是第几个字符. 它从0开始. 
     切片, 从字符串中提取n个字符. 

     ```python
     s = "我爱黎明,黎明爱我"
     print(s[1])
     print(s[0])
     
     print(s[2:4])  从第2个, 到第4个(取不到4)
     ```

     

  2. strip()

     我们从网页上提取的数据. 很多都是带有一些杂质的(换行, 空格),怎么去掉?

     strip()可以去掉字符串`左右两端`的空白(空格, 换行\n, 回车\r, 制表符\t)

     ```python
     s = "    \t\t\t我的天哪\r\r      \n\n  "  # 够乱的字符串
     s1 = s.strip()
     print(s1)  # 好了 `我的天哪`
     ```

     

  3. split()

     split,  做切割的. 

     ```python
     s = "10,男人本色,100000万"  # 你在网页上提取到这样的一段数据. 现在我需要电影名称
     tmps = s.split(",")
     name = tmps[1]
     print(name)  # 男人本色
     
     id, name, money = s.split(",")  # 切割后. 把三个结果直接怼给三个变量
     print(id)
     print(name)
     print(money)
     ```

     

  4. replace()

     replace, 字符串替换

     ```python
     s = "我      \t\t\n\n爱   黎       明    "   # 这是你从网页上拿到的东西
     s1 = replace(" ", "").replace("\t", "").replace("\n", "")  # 干掉空格, \t, \n
     print(s1)  # 我爱黎明
     ```

     

  5. join()

     join, 将列表拼接为一个完整的字符串

     ```python
     lst = ["我妈", "不喜欢", "黎明"]  # 有时,由于网页结构的不规则, 导致获取的数据是这样的. 
     s1 = "".join(lst)  # 用空字符串把lst中的每一项拼接起来
     print(s1)  # 我妈不喜欢黎明
     
     lst2 = ["\n\r","\n\r","周杰伦\n\r", "\n不认识我\r"] 
     s2 = "".join(lst2).replace("\n", "").replace("\r", "")
     print(s2)  # 周杰伦不认识我
     
     ```

  6. f-string

     格式化字符串的一种方案

     ```python
     s = "周杰伦"
     s1 = f"我喜欢{s}"  #  它会把一个变量塞入一个字符串
     print(s1)  # 我喜欢周杰伦
     
     k = 10085
     s2 = f"我的电话号是{k+1}" # 它会把计算结果赛入一个字符串
     print(s2)  # 我的电话号是10086
     
     # 综上, f-string的大括号里, 其实是一段表达式.能计算出结果即可
     
     ```

     

### 3.3  列表

列表, 我们未来遇见的仅次于字符串的一种数据类型. 它主要是能承载大量的数据. 理论上. 你的内存不炸. 它就能一直存

1. 索引, 切片

   列表的索引和切片逻辑与字符串完全一致

   ```python
   lst = ["赵本山", "王大陆", "大嘴猴", "马后炮"]
   item1 = lst[2]  # 大嘴猴
   item2 = lst[1]  # 王大陆
   
   lst2 = lst[2:]
   print(lst2)  # ["大嘴猴", "马后炮"]
   
   # 注意, 如果列表中没有数据. 取0会报错
   lst = []
   print(lst[0])  # 报错, Index out of bounds
   
   # 注意, 如果给出的索引下标超过了列表的最大索引. 依然会报错
   lst = ["123", "456"]
   print(lst[9999])  # 报错, Index out of bounds
   
   ```

   

2. 增加

   给列表添加数据.   append

   ```python
   lst = [11,22]
   lst.append(33)
   lst.append(44)
   print(lst)  # [11,22,33,44]
   ```

   

3. 删除

   删除数据(不常用, 好不容易爬到的数据. 为什么要删)

   ```python
   lst.remove("周润发")  #  把周润发删掉
   ```

   

4. 修改

   ```python
   lst = ["赵本山", "王大陆", "大嘴猴", "马后炮"]
   lst[1] = "周杰伦"
   print(lst)  # ["赵本山", "周杰伦", "大嘴猴", "马后炮"]
   ```

   

5. range

   用for循环数数的一个东西

   ```python
   for i in range(10):
       print(i)   # 从0数到9
      
   for i in range(5, 10):
       print(i)  # 从5 数到 9
   ```

6. 查询(必会!!!!)

   ```python
   lst = ["赵本山", "周杰伦", "大嘴猴", "马后炮"]
   print(lst[0])
   print(lst[1])
   print(lst[2])
   print(lst[3])
   
   # 循环列表的索引
   for i in range(len(lst)):
       print(lst[i])
   # 循环列表的内容
   for item in lst:
       print(item)
   ```

   

### 3.4  字典

字典可以成对儿的保存数据. 

1. 增加

   ```python
   dic = {}
   dic['name'] = '樵夫'
   dic['age'] = 18
   
   print(dic)  # {"name": "樵夫", "age": 18}
   
   ```

   

2. 修改

   ```python
   dic = {"name": "樵夫", "age": 18}
   dic['age'] = 19
   print(dic)  # {"name": "樵夫", "age": 19}
   ```

   

3. 删除(不常用)

   ```python
   dic = {"name": "樵夫", "age": 18}
   dic.pop("age")
   print(dic)  # {'name': '樵夫'}
   ```

   

4. 查询(重点)

   ```python
   dic = {"name": "樵夫", "age": 18}
   
   a = dic['name']  # 查询'name'的值
   print(a)  # 樵夫
   
   b = dic['age']  # 拿到dic中age对应的值
   print(b)  # 18
   
   c = dic['哈拉少']   # 没有哈拉少. 报错
   d = dic.get("哈拉少")  # 没有哈拉少, 不报错. 返回None. 它好. 它不报错
   
   ```

   循环

   ```python
   dic = {"name": "樵夫", "age": 18}
   for k in dic:  # 循环出所有的key
       print(k)  
       print(dic[k])  # 获取到所有的value并打印
       
   ```

   嵌套

   ```python
   dic = {
       "name": "王峰",
       "age": 18,
       "wife": {
           "name": "章子怡",
           "age": 19,
       },
       "children": [
           {'name':"胡一菲", "age": 19},
           {'name':"胡二菲", "age": 18},
           {'name':"胡三菲", "age": 17},
       ]
   }
   
   value = dic["马化腾"]  # key不存在会报错
   value = dic.get("马化腾")  # 不会报错, 返回给你一个None
   
   # 王峰的第二个孩子的名字
   print(dic['children'][1]['name'])
   # 王峰所有孩子的名称和年龄
   for item in dic['children']:
       print(item['name'])
       print(item['age'])
   ```
   
   

### 3.5  字符集和bytes

字符集, 记住两个字符集就够了. 一个是utf-8, 一个是gbk. 都是支持中文的. 但是utf-8的编码数量远大于gbk. 我们平时使用的最多的是utf-8

```python
# 把字符串转化成字节
bs = "我的天哪abcdef".encode("utf-8")
print(bs)  #  b'\xe6\x88\x91\xe7\x9a\x84\xe5\xa4\xa9\xe5\x93\xaaabcdef'
# 一个中文在utf-8里是3个字节. 一个英文是一个字节. 所以英文字母是正常显示的

# 把字节还原回字符串
bs = b'\xe6\x88\x91\xe7\x9a\x84\xe5\xa4\xa9\xe5\x93\xaaabcdef'
s = bs.decode("utf-8")
print(s)

```

记住, bytes不是给人看的. 是给机器看的. 我们遇到的所有文字, 图片, 音频, 视频. 所有所有的东西到了计算机里都是字节. 



### 3.6 文件操作

python中. 想要处理一个文件. 必须用open()先打开一个文件

语法规则

```python
f = open(文件名, mode="模式", encoding='文件编码')
f.read()|f.write()
f.close()
```

文件名就不解释了. 

模式: 
	我们需要知道的主要有4个. 分别是: r, w, a, b

1. r  只读模式. 含义是, 当前这一次open的目的是读取数据. 所以, 只能读. 不能写
2. w 只写模式. 含义是, 当前这一次open的目的是写入数据. 所以, 只能写, 不能读
3. a 追加模式. 含义是, 当前这一次open的目的是向后追加. 所以, 只能写, 不能读
4. b 字节模式. 可以和上面三种模式进行混合搭配. 目的是. 写入的内容或读取的内容是字节. 

问: 

1. 如果我想保存一张图片. 应该用哪种模式?
2. 我想读取txt文件, 用哪种模式?
3. 我想复制一个文件. 应该用哪种模式?

encoding: 文件编码. 只有处理的文件是文本的时候才能使用. 并且mode不可以是`b`.   99%的时候我们用的是`utf-8`

另一种写法:

```python
with open(文件名, mode=模式, encoding=编码) as f:
    pass
```

这种写法的好处是, 不需要我们手动去关闭`f`

读取一个文本文件:

```python
with open("躺尸一摆手.txt", mode="r", encoding="utf-8") as f:
    for line in f:  # for循环可以逐行的进行循环文件中的内容
        print(line)
```



### 3.7  关于函数

在代码量很少的时候, 我们并不需要函数. 但是一旦代码量大了. 一次写个几百行代码. 调试起来就很困难. 此时, 建议把程序改写成一个一个具有特定功能的函数. 方便调试. 也方便代码的重用

```python
def 函数名(形式参数):
    # 函数体
    return 返回值
```

上面是编写一个函数的固定逻辑. 但是, 编写好的函数是不会自己运行的. 必须有人调用才可以

```python
函数名(实际参数)
```

写一个试试:

```python
def get_page_source(url):
    print("我要发送请求了. 我要获取到页面源代码啊")
    return "页面源代码"

pg_one = get_page_source("baidu.com")
pg_two = get_page_source("koukou.com")
```

再来一个

```python
def download_image(url, save_path):
    print(f"我要下载图片{url}了", f"保存在{save_path}")

donwload_image("http://www.baidu.com/abc/huyifei.jpg", "胡二飞.jpg")
donwload_image("http://www.baidu.com/aaa/dagedagefeifeifei.jpg", "大哥大哥飞飞飞.jpg")

```

总结, 函数的好处就是, 以后需要该功能. 不用再写重复代码了. 



### 3.8 关于模块

模块是啥? 模块就是已经有人帮我们写好了的一些代码, 这些代码被保存在一个py文件或者一个文件夹里. 我们可以拿来直接用

在python中有三种模块.

第一种, python内置模块

​	不用安装. 直接导入就能用

第二种, 第三方模块

​	需要安装. 安装后. 导入就可以用了

第三种, 自定义模块(新手先别自己定义模块)

​	直接导入就能用

导入模块的语法

```python
import 模块
from 模块 import 功能
from 模块.子模块 import 功能

举例子, 
import os
import sys
from urllib.parse import urljoin
from bs4 import BeautifulSoup
```

搞爬虫.必须要了解的一些python内置模块

1. time模块

   ```python
   import time
   time.time()  # 这个是获取到时间戳
   time.sleep(999)  # 让程序暂停999秒
   ```

   

2. os模块 

   ```python
   import os
   # 判断文件是否存在
   os.path.exists()  #  判断文件或者文件夹是否存在
   os.path.join()    # 路径拼接
   os.makedirs()     # 创建文件夹
   ```
   
   
   
3. json模块(重中之重)

   现在的网站不同于从前了. 习惯性用json来传递数据. 所以, 我们必须要知道json是啥, 以及python如何处理json. 

   json是一种类似字典一样的东西.  对于python而言, json是字符串.  

   例如, 

   ```python
   s = '{"name": "jay", "age": 18}'
   ```

   你看. 这破玩意就是`json`

   如何来转化它. 

   **<span style="background-color:yellow;color:red;">json字符串 => python字典</span>**

   ```python
   import json
   s = '{"name": "jay", "age": 18}'
   dic = json.loads(s)
   print(type(dic))
   ```

   **<span style="background-color:yellow;color:red;">python字典 => json字符串</span>**

   ```python
   import json
   dic = {"name": "jay", "age": 18}
   s = json.dumps(dic)
   print(type(s))
   ```

   

4. random模块

   随机. 没别的用处.生成随机数

   ```python
   import random
   i = random.randint(1, 10)  # 1~10的随机数
   print(i)   # 多跑两次.效果更加
   ```

   

5. 异常处理

   这个是重点. 我们在写爬虫的时候. 非常容易遇到问题. 但这些问题本身并不是我们程序的问题. 

   比如, 你在抓取某网站的时候. 由于网络波动或者他服务器本身压力太大. 导致本次请求失败. 这种现象太常见了. 此时, 我们程序这边就会崩溃. 打印一堆红色的文字. 让你难受的一P.  怎么办?

   我们要清楚一个事情. 我们平时在打开一个网址的时候. 如果长时间没有反应, 或者加载很慢的时候. 我们习惯性的会刷新网页. 对吧. 这个逻辑就像: `程序如果本次请求失败了. 能不能重新来一次`. OK, 我们接下来聊的这个异常处理. 就是干这个事儿的. 

   ```python
   try: # 尝试...
       print("假如, 我是一段爬虫代码, 请求到对方服务器")
       print("我得出事儿啊")
       print(1/0)  # 出事儿了
   except Exception as e:  # 出错了. 我给你兜着
       print(e)  # 怎么兜?  打印一下. 就过去了
       
   print("不论上面是否出错. 我这里, 依然可以执行")
   ```

   看懂了么? 程序执行的时候. 如果`try`中的代码出现错误. 则自动跳到`except`中. 并执行`except`中的代码. 然后程序正常的, 继续执行

   有了这玩意. 我们就可以写出一段很漂亮的代码逻辑:

   ```python
   while 1:
       try:
           我要发送请求了. 我要干美国CIA的总部. 我要上天
           print("我成功了!!")
           break  # 成功了.就跳出循环
       except Exception as e:
           print("失败了")
           print("我不怕失败")
           print("再来")
          
   ```

   改良版:

   ```python
   import time
   for i in range(10):
       try:
           我要发送请求了. 我要干美国CIA的总部. 我要上天
           print("我成功了!!")
           break  # 成功了.就跳出循环
       except Exception as e:
           print("失败了")
           print("我不怕失败")
           print("再来")
           time.sleep(i * 10)
           
   ```

<span style='background-color:yellow;color:red;font-size:1cm;line-height:1.5cm;'>在写代码测试阶段. 不要加try...except... 要不然. 出错了. 你都不知道. 啥错了, 错哪儿了. </span>

## 今日作业 ( 不用交 ) 

请想办法搞出下列`json`中所有的`英雄名称`和`英雄title`. 并将`英雄名称`和`英雄title`写入`names.txt`文件中. 

```python
{"hero":[{"heroId":"1","name":"\u9ed1\u6697\u4e4b\u5973","alias":"Annie","title":"\u5b89\u59ae","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"3","magic":"10","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/1.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/1.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"2000","camp":"","campId":"","keywords":"\u5b89\u59ae,\u9ed1\u6697\u4e4b\u5973,\u706b\u5973,Annie,anni,heianzhinv,huonv,an,hazn,hn"},{"heroId":"2","name":"\u72c2\u6218\u58eb","alias":"Olaf","title":"\u5965\u62c9\u592b","roles":["fighter","tank"],"isWeekFree":"1","attack":"9","defense":"5","magic":"3","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/2.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/2.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"1500","camp":"","campId":"","keywords":"\u72c2\u6218\u58eb,\u5965\u62c9\u592b,kzs,alf,Olaf,kuangzhanshi,aolafu"},{"heroId":"3","name":"\u6b63\u4e49\u5de8\u50cf","alias":"Galio","title":"\u52a0\u91cc\u5965","roles":["tank","mage"],"isWeekFree":"0","attack":"1","defense":"10","magic":"6","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/3.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/3.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2000","camp":"","campId":"","keywords":"\u6b63\u4e49\u5de8\u50cf,\u52a0\u91cc\u5965,Galio,jla,zyjx,zhengyijuxiang,jialiao"},{"heroId":"4","name":"\u5361\u724c\u5927\u5e08","alias":"TwistedFate","title":"\u5d14\u65af\u7279","roles":["mage"],"isWeekFree":"0","attack":"6","defense":"2","magic":"6","difficulty":"9","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/4.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/4.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u5361\u724c\u5927\u5e08,\u5d14\u65af\u7279,\u5361\u724c,TwistedFate,kp,cst,kpds,kapaidashi,cuisite,kapai"},{"heroId":"5","name":"\u5fb7\u90a6\u603b\u7ba1","alias":"XinZhao","title":"\u8d75\u4fe1","roles":["fighter","assassin"],"isWeekFree":"0","attack":"8","defense":"6","magic":"3","difficulty":"2","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/5.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/5.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u5fb7\u90a6\u603b\u7ba1,\u5fb7\u90a6,\u8d75\u4fe1,XinZhao,db,dbzg,zx,debangzongguan,debang,zhaoxin"},{"heroId":"6","name":"\u65e0\u754f\u6218\u8f66","alias":"Urgot","title":"\u5384\u52a0\u7279","roles":["fighter","tank"],"isWeekFree":"0","attack":"8","defense":"5","magic":"3","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/6.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/6.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"1000","camp":"","campId":"","keywords":"\u65e0\u754f\u6218\u8f66,\u5384\u52a0\u7279,ejt,wwzc,Urgot,wuweizhanche,ejiate"},{"heroId":"7","name":"\u8be1\u672f\u5996\u59ec","alias":"Leblanc","title":"\u4e50\u8299\u5170","roles":["assassin","mage"],"isWeekFree":"0","attack":"1","defense":"4","magic":"10","difficulty":"9","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/7.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/7.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"2500","camp":"","campId":"","keywords":"\u8be1\u672f\u5996\u59ec,\u5996\u59ec,\u4e50\u8299\u5170,Leblanc,lfl,yj,gsyj,guishuyaoji,yaoji,lefulan"},{"heroId":"8","name":"\u7329\u7ea2\u6536\u5272\u8005","alias":"Vladimir","title":"\u5f17\u62c9\u57fa\u7c73\u5c14","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"6","magic":"8","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/8.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/8.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u7329\u7ea2\u6536\u5272\u8005,\u5438\u8840\u9b3c,\u5f17\u62c9\u57fa\u7c73\u5c14,fljme,xxg,xhsgz,Vladimir,xinghongshougezhe,xixiegui,fulajimier"},{"heroId":"9","name":"\u8fdc\u53e4\u6050\u60e7","alias":"FiddleSticks","title":"\u8d39\u5fb7\u63d0\u514b","roles":["mage","support"],"isWeekFree":"0","attack":"2","defense":"3","magic":"9","difficulty":"9","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/9.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/9.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u8fdc\u53e4\u6050\u60e7,\u8d39\u5fb7\u63d0\u514b,\u7a3b\u8349\u4eba,FiddleSticks,yuangukongju,feidetike,daocaoren,dcr,fdtk,ygkj"},{"heroId":"10","name":"\u6b63\u4e49\u5929\u4f7f","alias":"Kayle","title":"\u51ef\u5c14","roles":["fighter","support"],"isWeekFree":"0","attack":"6","defense":"6","magic":"7","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/10.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/10.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"450","couponPrice":"1000","camp":"","campId":"","keywords":"\u6b63\u4e49\u5929\u4f7f,\u51ef\u5c14,\u5929\u4f7f,ts,zyts,ke,Kayle,zhengyitianshi,kaier,tianshi"},{"heroId":"11","name":"\u65e0\u6781\u5251\u5723","alias":"MasterYi","title":"\u6613","roles":["assassin","fighter"],"isWeekFree":"0","attack":"10","defense":"4","magic":"2","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/11.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/11.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"450","couponPrice":"1000","camp":"","campId":"","keywords":"\u65e0\u6781\u5251\u5723,\u6613,\u5251\u5723,js,y,wjjs,MasterYi,wujijiansheng,yi,jiansheng"},{"heroId":"12","name":"\u725b\u5934\u914b\u957f","alias":"Alistar","title":"\u963f\u5229\u65af\u5854","roles":["tank","support"],"isWeekFree":"0","attack":"6","defense":"9","magic":"5","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/12.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/12.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"1000","camp":"","campId":"","keywords":"\u963f\u5229\u65af\u5854,\u725b\u5934,\u725b\u5934\u914b\u957f,\u914b\u957f,alisita,niutou,niutouqiuzhang,qiuzhang,Alistar,alst,nt,ntqz,qz"},{"heroId":"13","name":"\u7b26\u6587\u6cd5\u5e08","alias":"Ryze","title":"\u745e\u5179","roles":["mage","fighter"],"isWeekFree":"1","attack":"2","defense":"2","magic":"10","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/13.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/13.ogg","isARAMweekfree":"0","ispermanentweekfree":"1","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"450","couponPrice":"1000","camp":"","campId":"","keywords":"\u7b26\u6587\u6cd5\u5e08,\u745e\u5179,Ryze,\u5149\u5934,rz,fwfs,gt,fuwenfashi,ruizi,guangtou"},{"heroId":"14","name":"\u4ea1\u7075\u6218\u795e","alias":"Sion","title":"\u8d5b\u6069","roles":["tank","fighter"],"isWeekFree":"0","attack":"5","defense":"9","magic":"3","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/14.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/14.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u4ea1\u7075\u6218\u795e,\u585e\u6069,\u8d5b\u6069,se,wlzs,Sion,wanglingzhanshen,saien"},{"heroId":"15","name":"\u6218\u4e89\u5973\u795e","alias":"Sivir","title":"\u5e0c\u7ef4\u5c14","roles":["marksman"],"isWeekFree":"0","attack":"9","defense":"3","magic":"1","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/15.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/15.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"450","couponPrice":"1000","camp":"","campId":"","keywords":"\u6218\u4e89\u5973\u795e,\u8f6e\u5b50\u5988,\u5e0c\u7ef4\u5c14,lzm,xwe,zzns,Sivir,zhanzhengnvshen,lunzima,xiweier"},{"heroId":"16","name":"\u4f17\u661f\u4e4b\u5b50","alias":"Soraka","title":"\u7d22\u62c9\u5361","roles":["support","mage"],"isWeekFree":"0","attack":"2","defense":"5","magic":"7","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/16.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/16.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"450","couponPrice":"1000","camp":"","campId":"","keywords":"\u4f17\u661f\u4e4b\u5b50,\u7d22\u62c9\u5361,\u661f\u5988,\u5976\u5988,xm,nm,slk,zxzz,Soraka,zhongxingzhizi,suolaka,xingma,naima"},{"heroId":"17","name":"\u8fc5\u6377\u65a5\u5019","alias":"Teemo","title":"\u63d0\u83ab","roles":["marksman","assassin"],"isWeekFree":"1","attack":"5","defense":"3","magic":"7","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/17.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/17.ogg","isARAMweekfree":"0","ispermanentweekfree":"1","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"3500","camp":"","campId":"","keywords":"\u8fc5\u6377\u65a5\u5019,\u63d0\u83ab,timo,Teemo,tm,xjch,xunjiechihou,timo"},{"heroId":"18","name":"\u9ea6\u6797\u70ae\u624b","alias":"Tristana","title":"\u5d14\u4e1d\u5854\u5a1c","roles":["marksman","assassin"],"isWeekFree":"0","attack":"9","defense":"3","magic":"5","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/18.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/18.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"1000","camp":"","campId":"","keywords":"\u9ea6\u6797\u70ae\u624b,\u5c0f\u70ae,\u5d14\u4e1d\u5854\u5a1c,xp,cstn,mlps,Tristana,mailinpaoshou,xiaopao,cuisitana"},{"heroId":"19","name":"\u7956\u5b89\u6012\u517d","alias":"Warwick","title":"\u6c83\u91cc\u514b","roles":["fighter","tank"],"isWeekFree":"0","attack":"9","defense":"5","magic":"3","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/19.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/19.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u7956\u5b89\u6012\u517d,\u6c83\u91cc\u514b,\u72fc\u4eba,lr,wlk,zans,Warwick,zuannushou,wolike,langren"},{"heroId":"20","name":"\u96ea\u539f\u53cc\u5b50","alias":"Nunu","title":"\u52aa\u52aa\u548c\u5a01\u6717\u666e","roles":["tank","fighter"],"isWeekFree":"0","attack":"4","defense":"6","magic":"7","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/20.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/20.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"450","couponPrice":"1000","camp":"","campId":"","keywords":"\u96ea\u539f\u53cc\u5b50,\u52aa\u52aa\u548c\u5a01\u6717\u666e,\u52aa\u52aa,\u96ea\u4eba,Nunu,nn,xr,xysz,mmhwlp,xueyuanshuangzi,nunuheweilangpu,nunu,xueren"},{"heroId":"21","name":"\u8d4f\u91d1\u730e\u4eba","alias":"MissFortune","title":"\u5384\u8fd0\u5c0f\u59d0","roles":["marksman"],"isWeekFree":"0","attack":"8","defense":"2","magic":"5","difficulty":"1","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/21.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/21.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u8d4f\u91d1\u730e\u4eba,\u8d4f\u91d1,\u5384\u8fd0\u5c0f\u59d0,MF,MissFortune,sj,sjlr,eyxj,shangjinlieren,shangjin,eyunxiaojie"},{"heroId":"22","name":"\u5bd2\u51b0\u5c04\u624b","alias":"Ashe","title":"\u827e\u5e0c","roles":["marksman","support"],"isWeekFree":"1","attack":"7","defense":"3","magic":"2","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/22.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/22.ogg","isARAMweekfree":"0","ispermanentweekfree":"1","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"450","couponPrice":"1000","camp":"","campId":"","keywords":"\u827e\u5e0c,\u5bd2\u51b0,\u7231\u5c04,\u827e\u5c04,\u51b0\u5f13,Ashe,aixi,hanbing,aishe,aishe,binggong,ax,hb,as,bg"},{"heroId":"23","name":"\u86ee\u65cf\u4e4b\u738b","alias":"Tryndamere","title":"\u6cf0\u8fbe\u7c73\u5c14","roles":["fighter","assassin"],"isWeekFree":"0","attack":"10","defense":"5","magic":"2","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/23.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/23.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u86ee\u65cf\u4e4b\u738b,\u86ee\u738b,\u6cf0\u8fbe\u7c73\u5c14,Tryndamere,tdme,mw,mzzw,manzuzhiwang,manwang,taidamier"},{"heroId":"24","name":"\u6b66\u5668\u5927\u5e08","alias":"Jax","title":"\u8d3e\u514b\u65af","roles":["fighter","assassin"],"isWeekFree":"0","attack":"7","defense":"5","magic":"7","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/24.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/24.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u6b66\u5668\u5927\u5e08,\u8d3e\u514b\u65af,\u6b66\u5668,Jax,wq,jks,wqds,wuqidashi,jiakesi,wuqi"},{"heroId":"25","name":"\u5815\u843d\u5929\u4f7f","alias":"Morgana","title":"\u83ab\u7518\u5a1c","roles":["mage","support"],"isWeekFree":"0","attack":"1","defense":"6","magic":"8","difficulty":"1","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/25.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/25.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u5815\u843d\u5929\u4f7f,\u83ab\u7518\u5a1c,MGN,dlts,Morgana,duoluotianshi,moganna"},{"heroId":"26","name":"\u65f6\u5149\u5b88\u62a4\u8005","alias":"Zilean","title":"\u57fa\u5170","roles":["support","mage"],"isWeekFree":"0","attack":"2","defense":"5","magic":"8","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/26.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/26.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"450","couponPrice":"1000","camp":"","campId":"","keywords":"\u65f6\u5149\u5b88\u62a4\u8005,\u57fa\u5170,Zilean,jl,sgshz,\u65f6\u5149\u8001\u4eba,\u65f6\u5149\u8001\u5934,shiguangshouhuzhe,jilan,shiguanglaoren,shiguanglaotou"},{"heroId":"27","name":"\u70bc\u91d1\u672f\u58eb","alias":"Singed","title":"\u8f9b\u5409\u5fb7","roles":["tank","fighter"],"isWeekFree":"0","attack":"4","defense":"8","magic":"7","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/27.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/27.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u70bc\u91d1\u672f\u58eb,\u8f9b\u5409\u5fb7,\u70bc\u91d1,lj,xjd,ljss,Singed,lianjinshushi,xinjide,lianjin"},{"heroId":"28","name":"\u75db\u82e6\u4e4b\u62e5","alias":"Evelynn","title":"\u4f0a\u8299\u7433","roles":["assassin","mage"],"isWeekFree":"0","attack":"4","defense":"2","magic":"7","difficulty":"10","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/28.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/28.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u75db\u82e6\u4e4b\u62e5,\u4f0a\u8299\u7433,\u5be1\u5987,Evelynn,tongkuzhiyong,yifulin,guafu,gf,tkzy,yfl"},{"heroId":"29","name":"\u761f\u75ab\u4e4b\u6e90","alias":"Twitch","title":"\u56fe\u5947","roles":["marksman","assassin"],"isWeekFree":"0","attack":"9","defense":"2","magic":"3","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/29.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/29.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u761f\u75ab\u4e4b\u6e90,\u56fe\u5947,\u8001\u9f20,Twitch,ls,tq,wyzy,wenyizhiyuan,tuqi,laoshu"},{"heroId":"30","name":"\u6b7b\u4ea1\u9882\u5531\u8005","alias":"Karthus","title":"\u5361\u5c14\u8428\u65af","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"2","magic":"10","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/30.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/30.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u6b7b\u4ea1\u9882\u5531\u8005,\u5361\u5c14\u8428\u65af,\u6b7b\u6b4c,Karthus,sg,kess,swscz,siwangsongchangzhe,kaersasi,sige"},{"heroId":"31","name":"\u865a\u7a7a\u6050\u60e7","alias":"Chogath","title":"\u79d1\u52a0\u65af","roles":["tank","mage"],"isWeekFree":"0","attack":"3","defense":"7","magic":"7","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/31.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/31.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"1500","camp":"","campId":"","keywords":"\u865a\u7a7a\u6050\u60e7,\u79d1\u52a0\u65af,\u5927\u866b\u5b50,\u866b\u5b50,Chogath,xukongkongju,kejiasi,dachongzi,chongzi,xkkj,kjs,dcz,cz"},{"heroId":"32","name":"\u6b87\u4e4b\u6728\u4e43\u4f0a","alias":"Amumu","title":"\u963f\u6728\u6728","roles":["tank","mage"],"isWeekFree":"0","attack":"2","defense":"6","magic":"8","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/32.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/32.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u963f\u6728\u6728,\u6728\u4e43\u4f0a,\u5206\u5934,\u6b87\u4e4b\u6728\u4e43\u4f0a,\u6728\u6728,\u4f24\u4e4b\u6728\u4e43\u4f0a,amumu,munaiyi,fentou,shangzhimunaiyi,amm,szmny,mny,ft,mm,mumu"},{"heroId":"33","name":"\u62ab\u7532\u9f99\u9f9f","alias":"Rammus","title":"\u62c9\u83ab\u65af","roles":["tank","fighter"],"isWeekFree":"1","attack":"4","defense":"10","magic":"5","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/33.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/33.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u62ab\u7532\u9f99\u9f9f,\u62c9\u83ab\u65af,\u9f99\u9f9f,lg,pjlg,lms,Rammus,pijialonggui,lamosi,longgui"},{"heroId":"34","name":"\u51b0\u6676\u51e4\u51f0","alias":"Anivia","title":"\u827e\u5c3c\u7ef4\u4e9a","roles":["mage","support"],"isWeekFree":"1","attack":"1","defense":"4","magic":"10","difficulty":"10","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/34.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/34.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u51e4\u51f0,\u51b0\u6676\u51e4\u51f0,\u827e\u5c3c\u7ef4\u4e9a,Anivia,fenghuang,bingjingfenghuang,ainiweiya,anwy,bjfh,fh"},{"heroId":"35","name":"\u6076\u9b54\u5c0f\u4e11","alias":"Shaco","title":"\u8428\u79d1","roles":["assassin"],"isWeekFree":"0","attack":"8","defense":"4","magic":"6","difficulty":"9","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/35.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/35.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"2000","camp":"","campId":"","keywords":"\u6076\u9b54\u5c0f\u4e11,\u5c0f\u4e11,\u6c99\u6263,\u6c99\u53e3,\u8428\u79d1,xc,emxc,sk,emoxiaochou,xiaochou,sake,Shaco"},{"heroId":"36","name":"\u7956\u5b89\u72c2\u4eba","alias":"DrMundo","title":"\u8499\u591a\u533b\u751f","roles":["fighter","tank"],"isWeekFree":"0","attack":"5","defense":"7","magic":"6","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/36.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/36.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u7956\u5b89\u72c2\u4eba,\u8499\u591a\u533b\u751f,\u8499\u591a,DrMundo,zuankuangren,mengduoyisheng,mengduo,md,mdys,zakr"},{"heroId":"37","name":"\u7434\u745f\u4ed9\u5973","alias":"Sona","title":"\u5a11\u5a1c","roles":["support","mage"],"isWeekFree":"0","attack":"5","defense":"2","magic":"8","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/37.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/37.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u7434\u745f\u4ed9\u5973,\u7434\u5973,\u5a11\u5a1c,sn,qn,qsxn,Sona,qinsexiannv,qinnv,suona"},{"heroId":"38","name":"\u865a\u7a7a\u884c\u8005","alias":"Kassadin","title":"\u5361\u8428\u4e01","roles":["assassin","mage"],"isWeekFree":"0","attack":"3","defense":"5","magic":"8","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/38.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/38.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u865a\u7a7a\u884c\u8005,\u5361\u8428\u4e01,ksd,xkxz,Kassadin,xukongxingzhe,kasading"},{"heroId":"39","name":"\u5200\u950b\u821e\u8005","alias":"Irelia","title":"\u827e\u745e\u8389\u5a05","roles":["fighter","assassin"],"isWeekFree":"0","attack":"7","defense":"4","magic":"5","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/39.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/39.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4000","camp":"","campId":"","keywords":"\u5200\u950b\u821e\u8005,\u827e\u745e\u8389\u5a05,\u5973\u5200,\u5973\u5200\u950b,Irelia,nd,ndf,dfwz,arly,daofengwuzhe,airuiliya,nvdao,nvdaofeng"},{"heroId":"40","name":"\u98ce\u66b4\u4e4b\u6012","alias":"Janna","title":"\u8fe6\u5a1c","roles":["support","mage"],"isWeekFree":"1","attack":"3","defense":"5","magic":"7","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/40.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/40.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u98ce\u66b4\u4e4b\u6012,\u8fe6\u5a1c,\u98ce\u5973,fn,jn,fbzn,Janna,fengbaozhinu,jiana,fengnv"},{"heroId":"41","name":"\u6d77\u6d0b\u4e4b\u707e","alias":"Gangplank","title":"\u666e\u6717\u514b","roles":["fighter"],"isWeekFree":"1","attack":"7","defense":"6","magic":"4","difficulty":"9","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/41.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/41.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u6d77\u6d0b\u4e4b\u707e,\u666e\u6717\u514b,\u8239\u957f,plk,cz,hyzz,Gangplank,haiyangzhizai,pulangke,chuanzhang"},{"heroId":"42","name":"\u82f1\u52c7\u6295\u5f39\u624b","alias":"Corki","title":"\u5e93\u5947","roles":["marksman"],"isWeekFree":"0","attack":"8","defense":"3","magic":"6","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/42.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/42.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"3500","camp":"","campId":"","keywords":"\u82f1\u52c7\u6295\u5f39\u624b,\u5e93\u5947,\u98de\u673a,Corki,yingyongtoudanshou,kuqi,feiji,fj,kq,yytds"},{"heroId":"43","name":"\u5929\u542f\u8005","alias":"Karma","title":"\u5361\u5c14\u739b","roles":["mage","support"],"isWeekFree":"0","attack":"1","defense":"7","magic":"8","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/43.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/43.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u5929\u542f\u8005,\u5361\u5c14\u739b,\u6247\u5b50\u5988,Karma,szm,kem,tqz,tianqizhe,kaerma,shanzima"},{"heroId":"44","name":"\u74e6\u6d1b\u5170\u4e4b\u76fe","alias":"Taric","title":"\u5854\u91cc\u514b","roles":["support","fighter"],"isWeekFree":"0","attack":"4","defense":"8","magic":"5","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/44.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/44.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"1500","camp":"","campId":"","keywords":"\u74e6\u6d1b\u5170\u4e4b\u76fe,\u5854\u91cc\u514b,\u5b9d\u77f3,bs,tlk,wllzd,Taric,waluolanzhidun,talike,baoshi"},{"heroId":"45","name":"\u90aa\u6076\u5c0f\u6cd5\u5e08","alias":"Veigar","title":"\u7ef4\u8fe6","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"2","magic":"10","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/45.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/45.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u90aa\u6076\u5c0f\u6cd5\u5e08,\u5c0f\u6cd5\u5e08,\u7ef4\u8fe6,xfs,xexfs,wj,Veigar,xieexiaofashi,xiaofashi,weijia"},{"heroId":"48","name":"\u5de8\u9b54\u4e4b\u738b","alias":"Trundle","title":"\u7279\u6717\u5fb7\u5c14","roles":["fighter","tank"],"isWeekFree":"0","attack":"7","defense":"6","magic":"2","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/48.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/48.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u5de8\u9b54\u4e4b\u738b,\u5de8\u9b54,\u7279\u6717\u5fb7\u5c14,Trundle,jm,jmzw,tlde,jumozhiwang,jumo,telangdeer"},{"heroId":"50","name":"\u8bfa\u514b\u8428\u65af\u7edf\u9886","alias":"Swain","title":"\u65af\u7ef4\u56e0","roles":["mage","fighter"],"isWeekFree":"0","attack":"2","defense":"6","magic":"9","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/50.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/50.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u8bfa\u514b\u8428\u65af\u7edf\u9886,\u4e4c\u9e26,\u65af\u7ef4\u56e0,swy,wy,nksstl,Swain,nuokesasitongling,wuya,siweiyin"},{"heroId":"51","name":"\u76ae\u57ce\u5973\u8b66","alias":"Caitlyn","title":"\u51ef\u7279\u7433","roles":["marksman"],"isWeekFree":"0","attack":"8","defense":"2","magic":"2","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/51.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/51.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"3000","camp":"","campId":"","keywords":"\u76ae\u57ce\u5973\u8b66,\u51ef\u7279\u7433,\u5973\u8b66,\u76ae\u57ce,Caitlyn,pichengnvjing,kaitelin,nvjing,picheng,pc,nj,pcnj,ctl"},{"heroId":"53","name":"\u84b8\u6c7d\u673a\u5668\u4eba","alias":"Blitzcrank","title":"\u5e03\u91cc\u8328","roles":["tank","fighter","support"],"isWeekFree":"0","attack":"4","defense":"8","magic":"5","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/53.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/53.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u84b8\u6c7d\u673a\u5668\u4eba,\u5e03\u91cc\u8328,\u673a\u5668\u4eba,Blitzcrank,zhengqijiqiren,bulici,jiqiren,zqjqr,jqr,blc"},{"heroId":"54","name":"\u7194\u5ca9\u5de8\u517d","alias":"Malphite","title":"\u58a8\u83f2\u7279","roles":["tank","fighter"],"isWeekFree":"0","attack":"5","defense":"9","magic":"7","difficulty":"2","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/54.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/54.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"1000","camp":"","campId":"","keywords":"\u7194\u5ca9\u5de8\u517d,\u58a8\u83f2\u7279,\u77f3\u5934\u4eba,Malphite,str,mft,ryjs,rongyanjushou,mofeite,shitouren"},{"heroId":"55","name":"\u4e0d\u7965\u4e4b\u5203","alias":"Katarina","title":"\u5361\u7279\u7433\u5a1c","roles":["assassin","mage"],"isWeekFree":"0","attack":"4","defense":"3","magic":"9","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/55.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/55.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u4e0d\u7965\u4e4b\u5203,\u5361\u7279\u7433\u5a1c,\u5361\u7279,kt,ktln,bxzr,\u4e0d\u8be6,bx,Katarina,buxiangzhiren,katelinna,kate,buxiang"},{"heroId":"56","name":"\u6c38\u6052\u68a6\u9b47","alias":"Nocturne","title":"\u9b54\u817e","roles":["assassin","fighter"],"isWeekFree":"0","attack":"9","defense":"5","magic":"2","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/56.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/56.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u6c38\u6052\u68a6\u9b47,\u9b54\u817e,noc,Nocturne,\u68a6\u9b47,my,yhmy,mt,yonghengmengyan,moteng,mengyan"},{"heroId":"57","name":"\u626d\u66f2\u6811\u7cbe","alias":"Maokai","title":"\u8302\u51ef","roles":["tank","mage"],"isWeekFree":"0","attack":"3","defense":"8","magic":"6","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/57.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/57.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u626d\u66f2\u6811\u7cbe,\u8302\u51ef,\u5927\u6811,ds,mk,nqsj,Maokai,niuqushujing,maokai,dashu"},{"heroId":"58","name":"\u8352\u6f20\u5c60\u592b","alias":"Renekton","title":"\u96f7\u514b\u987f","roles":["fighter","tank"],"isWeekFree":"0","attack":"8","defense":"5","magic":"2","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/58.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/58.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u8352\u6f20\u5c60\u592b,\u9cc4\u9c7c,\u96f7\u514b\u987f,ey,lkd,mmtf,huangmotufu,eyu,leikedun"},{"heroId":"59","name":"\u5fb7\u739b\u897f\u4e9a\u7687\u5b50","alias":"JarvanIV","title":"\u5609\u6587\u56db\u4e16","roles":["tank","fighter"],"isWeekFree":"0","attack":"6","defense":"8","magic":"3","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/59.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/59.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u5fb7\u739b\u897f\u4e9a\u7687\u5b50,\u5609\u6587\u56db\u4e16,\u7687\u5b50,\u5609\u6587,JarvanIV,jw,hz,dmxyhz,jwss,demaxiyahuangzi,jiawensishi,huangzi,jiawen"},{"heroId":"60","name":"\u8718\u86db\u5973\u7687","alias":"Elise","title":"\u4f0a\u8389\u4e1d","roles":["mage","fighter"],"isWeekFree":"1","attack":"6","defense":"5","magic":"7","difficulty":"9","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/60.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/60.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u8718\u86db\u5973\u7687,\u4f0a\u8389\u4e1d,\u8718\u86db,Elise,zz,zznh,yls,zhizhunvhuang,yilisi,zhizhu"},{"heroId":"61","name":"\u53d1\u6761\u9b54\u7075","alias":"Orianna","title":"\u5965\u8389\u5b89\u5a1c","roles":["mage","support"],"isWeekFree":"1","attack":"4","defense":"3","magic":"9","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/61.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/61.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"3000","camp":"","campId":"","keywords":"\u53d1\u6761\u9b54\u7075,\u5965\u8389\u5b89\u5a1c,\u53d1\u6761,Orianna,ftml,ft,alan,fatiaomoling,aolianna,fatiao"},{"heroId":"62","name":"\u9f50\u5929\u5927\u5723","alias":"MonkeyKing","title":"\u5b59\u609f\u7a7a","roles":["fighter","tank"],"isWeekFree":"0","attack":"8","defense":"5","magic":"2","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/62.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/62.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u9f50\u5929\u5927\u5723,\u5b59\u609f\u7a7a,MonkeyKing,\u7334\u5b50,hz,qtds,swk,qitiandasheng,sunwukong,houzi"},{"heroId":"63","name":"\u590d\u4ec7\u7130\u9b42","alias":"Brand","title":"\u5e03\u5170\u5fb7","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"2","magic":"9","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/63.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/63.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"2000","camp":"","campId":"","keywords":"\u590d\u4ec7\u7130\u9b42,\u5e03\u5170\u5fb7,\u706b\u7537,Brand,fuchouyanhun,bulande,huonan,cfyh,bld,hn"},{"heroId":"64","name":"\u76f2\u50e7","alias":"LeeSin","title":"\u674e\u9752","roles":["fighter","assassin"],"isWeekFree":"0","attack":"8","defense":"5","magic":"3","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/64.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/64.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u76f2\u50e7,\u778e\u5b50,\u674e\u9752,lq,xz,ms,LeeSin,mangseng,xiazi,liqing"},{"heroId":"67","name":"\u6697\u591c\u730e\u624b","alias":"Vayne","title":"\u8587\u6069","roles":["marksman","assassin"],"isWeekFree":"0","attack":"10","defense":"1","magic":"1","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/67.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/67.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u6697\u591c\u730e\u624b,\u8587\u6069,vn,Vayne,ve,ayls,anyelieshou,weien"},{"heroId":"68","name":"\u673a\u68b0\u516c\u654c","alias":"Rumble","title":"\u5170\u535a","roles":["fighter","mage"],"isWeekFree":"0","attack":"3","defense":"6","magic":"8","difficulty":"10","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/68.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/68.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u673a\u68b0\u516c\u654c,\u5170\u535a,Rumble,lb,jxgd,jixiegongdi,lanbo"},{"heroId":"69","name":"\u9b54\u86c7\u4e4b\u62e5","alias":"Cassiopeia","title":"\u5361\u897f\u5965\u4f69\u5a05","roles":["mage"],"isWeekFree":"1","attack":"2","defense":"3","magic":"9","difficulty":"10","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/69.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/69.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u9b54\u86c7\u4e4b\u62e5,\u5361\u897f\u5965\u4f69\u5a05,\u86c7\u5973,Cassiopeia,moshezhiyong,kaxiaopeiya,shenv,mszy,kxapy,sn"},{"heroId":"72","name":"\u6c34\u6676\u5148\u950b","alias":"Skarner","title":"\u65af\u5361\u7eb3","roles":["fighter","tank"],"isWeekFree":"0","attack":"7","defense":"6","magic":"5","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/72.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/72.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u6c34\u6676\u5148\u950b,\u65af\u5361\u7eb3,skn,sjxf,\u874e\u5b50,xz,Skarner,shuijingxianfeng,sikana,xiezi"},{"heroId":"74","name":"\u5927\u53d1\u660e\u5bb6","alias":"Heimerdinger","title":"\u9ed1\u9ed8\u4e01\u683c","roles":["mage","support"],"isWeekFree":"0","attack":"2","defense":"6","magic":"8","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/74.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/74.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u5927\u53d1\u660e\u5bb6,\u9ed1\u9ed8\u4e01\u683c,\u5927\u5934,Heimerdinger,dt,dfmj,hmdg,dafamingjia,heimodingge,datou"},{"heroId":"75","name":"\u6c99\u6f20\u6b7b\u795e","alias":"Nasus","title":"\u5185\u745f\u65af","roles":["fighter","tank"],"isWeekFree":"0","attack":"7","defense":"5","magic":"6","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/75.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/75.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u6c99\u6f20\u6b7b\u795e,\u5185\u745f\u65af,\u72d7\u5934,gt,nss,smss,Nasus,shamosishen,neisesi,goutou"},{"heroId":"76","name":"\u72c2\u91ce\u5973\u730e\u624b","alias":"Nidalee","title":"\u5948\u5fb7\u4e3d","roles":["assassin","mage"],"isWeekFree":"0","attack":"5","defense":"4","magic":"7","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/76.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/76.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"3500","camp":"","campId":"","keywords":"\u72c2\u91ce\u5973\u730e\u624b,\u5948\u5fb7\u4e3d,\u8c79\u5973,bn,ndl,kynls,Nidalee,kuangyenvlieshou,naideli,baonv"},{"heroId":"77","name":"\u517d\u7075\u884c\u8005","alias":"Udyr","title":"\u4e4c\u8fea\u5c14","roles":["fighter","tank"],"isWeekFree":"0","attack":"8","defense":"7","magic":"4","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/77.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/77.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u517d\u7075\u884c\u8005,\u4e4c\u8fea\u5c14,Udyr,wde,slxz,UD,shoulingxingzhe,wudier"},{"heroId":"78","name":"\u5723\u9524\u4e4b\u6bc5","alias":"Poppy","title":"\u6ce2\u6bd4","roles":["tank","fighter"],"isWeekFree":"0","attack":"6","defense":"7","magic":"2","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/78.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/78.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"450","couponPrice":"1000","camp":"","campId":"","keywords":"\u5723\u9524\u4e4b\u6bc5,\u6ce2\u6bd4,bb,sczy,Poppy,shengchuizhiyi,bobi"},{"heroId":"79","name":"\u9152\u6876","alias":"Gragas","title":"\u53e4\u62c9\u52a0\u65af","roles":["fighter","mage"],"isWeekFree":"0","attack":"4","defense":"7","magic":"6","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/79.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/79.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u9152\u6876,\u53e4\u62c9\u52a0\u65af,\u5564\u9152\u4eba,\u8089\u86cb\u8471\u9e21,Gragas,pjr,jt,gljs,rdcj,jiutong,gulajiasi,pijiuren,roudancongji"},{"heroId":"80","name":"\u4e0d\u5c48\u4e4b\u67aa","alias":"Pantheon","title":"\u6f58\u68ee","roles":["fighter","assassin"],"isWeekFree":"0","attack":"9","defense":"4","magic":"3","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/80.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/80.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"1500","camp":"","campId":"","keywords":"\u4e0d\u5c48\u4e4b\u67aa,\u6f58\u68ee,Pantheon,PS,bqzq,buquzhiqiang,pansen"},{"heroId":"81","name":"\u63a2\u9669\u5bb6","alias":"Ezreal","title":"\u4f0a\u6cfd\u745e\u5c14","roles":["marksman","mage"],"isWeekFree":"0","attack":"7","defense":"2","magic":"6","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/81.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/81.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u63a2\u9669\u5bb6,\u4f0a\u6cfd\u745e\u5c14,ez,Ezreal,tanxianjia,yizeruier,txj,yzrr"},{"heroId":"82","name":"\u94c1\u94e0\u51a5\u9b42","alias":"Mordekaiser","title":"\u83ab\u5fb7\u51ef\u6492","roles":["fighter"],"isWeekFree":"0","attack":"4","defense":"6","magic":"7","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/82.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/82.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"1500","camp":"","campId":"","keywords":"\u94c1\u94e0\u51a5\u9b42,\u83ab\u5fb7\u51ef\u6492,\u94c1\u7537,Mordekaiser,tn,mdks,tkmh,tiekaiminghun,modekaisa,tienan"},{"heroId":"83","name":"\u7267\u9b42\u4eba","alias":"Yorick","title":"\u7ea6\u91cc\u514b","roles":["fighter","tank"],"isWeekFree":"0","attack":"6","defense":"6","magic":"4","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/83.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/83.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u7267\u9b42\u4eba,\u7ea6\u91cc\u514b,\u6398\u5893\u4eba,jmr,mhr,ylk,Yorick,muhunren,yuelike,juemuren"},{"heroId":"84","name":"\u79bb\u7fa4\u4e4b\u523a","alias":"Akali","title":"\u963f\u5361\u4e3d","roles":["assassin"],"isWeekFree":"0","attack":"5","defense":"3","magic":"8","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/84.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/84.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u963f\u5361\u4e3d,\u79bb\u7fa4\u4e4b\u523a,akali,liqunzhici,akl,lqzc"},{"heroId":"85","name":"\u72c2\u66b4\u4e4b\u5fc3","alias":"Kennen","title":"\u51ef\u5357","roles":["mage","marksman"],"isWeekFree":"0","attack":"6","defense":"4","magic":"7","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/85.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/85.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"2500","camp":"","campId":"","keywords":"\u72c2\u66b4\u4e4b\u5fc3,\u51ef\u5357,kn,kbzx,Kennen,kuangbaozhixin,kainan"},{"heroId":"86","name":"\u5fb7\u739b\u897f\u4e9a\u4e4b\u529b","alias":"Garen","title":"\u76d6\u4f26","roles":["fighter","tank"],"isWeekFree":"1","attack":"7","defense":"7","magic":"1","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/86.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/86.ogg","isARAMweekfree":"0","ispermanentweekfree":"1","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"1000","camp":"","campId":"","keywords":"\u5fb7\u739b\u897f\u4e9a\u4e4b\u529b,\u76d6\u4f26,\u5927\u5b9d\u5251,Garen,dbj,gl,dmxyzl,demaxiyazhili,gailun,dabaojian"},{"heroId":"89","name":"\u66d9\u5149\u5973\u795e","alias":"Leona","title":"\u857e\u6b27\u5a1c","roles":["tank","support"],"isWeekFree":"0","attack":"4","defense":"8","magic":"3","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/89.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/89.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u66d9\u5149\u5973\u795e,\u857e\u6b27\u5a1c,\u65e5\u5973,\u66d9\u5149,\u5973\u5766,nt,rn,sg,lon,sgns,shuguangnvshen,leiouna,rinv,shuguang,Leona,nvtan"},{"heroId":"90","name":"\u865a\u7a7a\u5148\u77e5","alias":"Malzahar","title":"\u739b\u5c14\u624e\u54c8","roles":["mage","assassin"],"isWeekFree":"0","attack":"2","defense":"2","magic":"9","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/90.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/90.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u865a\u7a7a\u5148\u77e5,\u739b\u5c14\u624e\u54c8,\u8682\u86b1,\u9a6c\u5c14\u624e\u54c8,Malzahar,mz,mezh,xkxz,xukongxianzhi,maerzhaha,mazha,maerzhaha"},{"heroId":"91","name":"\u5200\u950b\u4e4b\u5f71","alias":"Talon","title":"\u6cf0\u9686","roles":["assassin"],"isWeekFree":"0","attack":"9","defense":"3","magic":"1","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/91.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/91.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5200\u950b\u4e4b\u5f71,\u7537\u5200,\u6cf0\u9686,tl,nd,dfzy,Talon,daofengzhiying,nandao,tailong"},{"heroId":"92","name":"\u653e\u9010\u4e4b\u5203","alias":"Riven","title":"\u9510\u96ef","roles":["fighter","assassin"],"isWeekFree":"0","attack":"8","defense":"5","magic":"1","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/92.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/92.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u653e\u9010\u4e4b\u5203,\u9510\u96ef,Riven,rw,fzzr,fangzhuzhiren,ruiwen"},{"heroId":"96","name":"\u6df1\u6e0a\u5de8\u53e3","alias":"KogMaw","title":"\u514b\u683c\u83ab","roles":["marksman","mage"],"isWeekFree":"0","attack":"8","defense":"2","magic":"5","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/96.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/96.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"2000","camp":"","campId":"","keywords":"\u6df1\u6e0a\u5de8\u53e3,\u514b\u683c\u83ab,\u5927\u5634,KogMaw,dz,kgm,syjk,shenyuanjukou,kegemo,dazui"},{"heroId":"98","name":"\u66ae\u5149\u4e4b\u773c","alias":"Shen","title":"\u614e","roles":["tank"],"isWeekFree":"0","attack":"3","defense":"9","magic":"3","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/98.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/98.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"1350","couponPrice":"2000","camp":"","campId":"","keywords":"\u66ae\u5149\u4e4b\u773c,\u614e,yaozi,s,mgzy,Shen,muguangzhiyan,shen"},{"heroId":"99","name":"\u5149\u8f89\u5973\u90ce","alias":"Lux","title":"\u62c9\u514b\u4e1d","roles":["mage","support"],"isWeekFree":"0","attack":"2","defense":"4","magic":"9","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/99.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/99.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"3150","couponPrice":"2500","camp":"","campId":"","keywords":"\u5149\u8f89\u5973\u90ce,\u62c9\u514b\u4e1d,\u5149\u8f89,lux,lks,gh,ghnl,guanghuinvlang,lakesi,guanghui"},{"heroId":"101","name":"\u8fdc\u53e4\u5deb\u7075","alias":"Xerath","title":"\u6cfd\u62c9\u65af","roles":["mage"],"isWeekFree":"1","attack":"1","defense":"3","magic":"10","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/101.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/101.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"2500","camp":"","campId":"","keywords":"\u8fdc\u53e4\u5deb\u7075,\u6cfd\u62c9\u65af,guancaiban,gbc,zls,ygwl,Xerath,yuanguwuling,zelasi"},{"heroId":"102","name":"\u9f99\u8840\u6b66\u59ec","alias":"Shyvana","title":"\u5e0c\u74e6\u5a1c","roles":["fighter","tank"],"isWeekFree":"0","attack":"8","defense":"6","magic":"3","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/102.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/102.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u9f99\u8840\u6b66\u59ec,\u9f99\u5973,\u5e0c\u74e6\u5a1c,ln,xwn,lxwj,Shyvana,longxuewuji,longnv,xiwana"},{"heroId":"103","name":"\u4e5d\u5c3e\u5996\u72d0","alias":"Ahri","title":"\u963f\u72f8","roles":["mage","assassin"],"isWeekFree":"0","attack":"3","defense":"4","magic":"8","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/103.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/103.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"3500","camp":"","campId":"","keywords":"\u4e5d\u5c3e,\u4e5d\u5c3e\u5996\u72d0,\u72d0\u72f8,\u963f\u72f8,jiuwei,jiuweiyaohu,huli,ali,ahri,jwyh,al,hl,jw"},{"heroId":"104","name":"\u6cd5\u5916\u72c2\u5f92","alias":"Graves","title":"\u683c\u96f7\u798f\u65af","roles":["marksman"],"isWeekFree":"0","attack":"8","defense":"5","magic":"3","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/104.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/104.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6cd5\u5916\u72c2\u5f92,\u683c\u96f7\u798f\u65af,\u7537\u67aa,Graves,nq,glfs,fwkt,fawaikuangtu,geleifusi,nanqiang"},{"heroId":"105","name":"\u6f6e\u6c50\u6d77\u7075","alias":"Fizz","title":"\u83f2\u5179","roles":["assassin","fighter"],"isWeekFree":"0","attack":"6","defense":"4","magic":"7","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/105.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/105.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6f6e\u6c50\u6d77\u7075,\u83f2\u5179,\u5c0f\u9c7c\u4eba,Fizz,fz,xyr,cxhl,chaoxihailing,feizi,xiaoyuren"},{"heroId":"106","name":"\u4e0d\u706d\u72c2\u96f7","alias":"Volibear","title":"\u6c83\u5229\u8d1d\u5c14","roles":["fighter","tank"],"isWeekFree":"0","attack":"7","defense":"7","magic":"4","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/106.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/106.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u4e0d\u706d\u72c2\u96f7,\u6c83\u5229\u8d1d\u5c14,Volibear,\u72d7\u718a,gx,wlbe,bmkl,bumiekuanglei,wolibeier,gouxiong"},{"heroId":"107","name":"\u50b2\u4e4b\u8ffd\u730e\u8005","alias":"Rengar","title":"\u96f7\u6069\u52a0\u5c14","roles":["assassin","fighter"],"isWeekFree":"0","attack":"7","defense":"4","magic":"2","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/107.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/107.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u50b2\u4e4b\u8ffd\u730e\u8005,\u72ee\u5b50\u72d7,\u96f7\u6069\u52a0\u5c14,szg,leje,azzlz,Rengar,aozhizhuiliezhe,shizigou,leienjiaer"},{"heroId":"110","name":"\u60e9\u6212\u4e4b\u7bad","alias":"Varus","title":"\u97e6\u9c81\u65af","roles":["marksman","mage"],"isWeekFree":"0","attack":"7","defense":"3","magic":"4","difficulty":"2","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/110.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/110.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u60e9\u6212\u4e4b\u7bad,\u97e6\u9c81\u65af,\u7ef4\u9c81\u65af,wls,cjzj,Varus,chengjiezhijian,weilusi"},{"heroId":"111","name":"\u6df1\u6d77\u6cf0\u5766","alias":"Nautilus","title":"\u8bfa\u63d0\u52d2\u65af","roles":["tank","fighter"],"isWeekFree":"0","attack":"4","defense":"6","magic":"6","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/111.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/111.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u6df1\u6d77\u6cf0\u5766,\u8bfa\u63d0\u52d2\u65af,\u6cf0\u5766,Nautilus,tt,ntls,shtt,shenhaitaitan,nuotileisi,taitan"},{"heroId":"112","name":"\u673a\u68b0\u5148\u9a71","alias":"Viktor","title":"\u7ef4\u514b\u6258","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"4","magic":"10","difficulty":"9","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/112.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/112.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"2500","camp":"","campId":"","keywords":"\u673a\u68b0\u5148\u9a71,\u7ef4\u514b\u6258,\u4e09\u53ea\u624b,szs,wkt,jxxq,Viktor,jixiexianqu,weiketuo,sanzhishou"},{"heroId":"113","name":"\u5317\u5730\u4e4b\u6012","alias":"Sejuani","title":"\u745f\u5e84\u59ae","roles":["tank","fighter"],"isWeekFree":"1","attack":"5","defense":"7","magic":"6","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/113.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/113.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u5317\u5730\u4e4b\u6012,\u732a\u59b9,\u745f\u5e84\u59ae,zm,szn,bdzn,Sejuani,beidizhinu,zhumei,sezhuangni"},{"heroId":"114","name":"\u65e0\u53cc\u5251\u59ec","alias":"Fiora","title":"\u83f2\u5965\u5a1c","roles":["fighter","assassin"],"isWeekFree":"0","attack":"10","defense":"4","magic":"2","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/114.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/114.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u65e0\u53cc\u5251\u59ec,\u83f2\u5965\u5a1c,\u5251\u59ec,Fiora,jj,wsjj,fan,wushuangjianji,feiaona,jianji"},{"heroId":"115","name":"\u7206\u7834\u9b3c\u624d","alias":"Ziggs","title":"\u5409\u683c\u65af","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"4","magic":"9","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/115.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/115.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u7206\u7834\u9b3c\u624d,\u70b8\u5f39\u4eba,\u5409\u683c\u65af,Ziggs,jgs,zdr,bpgc,baopoguicai,zhadanren,jigesi"},{"heroId":"117","name":"\u4ed9\u7075\u5973\u5deb","alias":"Lulu","title":"\u7490\u7490","roles":["support","mage"],"isWeekFree":"0","attack":"4","defense":"5","magic":"7","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/117.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/117.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u4ed9\u7075\u5973\u5deb,\u7490\u7490,ll,xlnw,Lulu,xianlingnvwu,lulu"},{"heroId":"119","name":"\u8363\u8000\u884c\u5211\u5b98","alias":"Draven","title":"\u5fb7\u83b1\u6587","roles":["marksman"],"isWeekFree":"0","attack":"9","defense":"3","magic":"1","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/119.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/119.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u8363\u8000\u884c\u5211\u5b98,\u5fb7\u83b1\u6587,Draven,rongyaoxingxingguan,delaiwen,ryxxg,dlw"},{"heroId":"120","name":"\u6218\u4e89\u4e4b\u5f71","alias":"Hecarim","title":"\u8d6b\u5361\u91cc\u59c6","roles":["fighter","tank"],"isWeekFree":"1","attack":"8","defense":"6","magic":"4","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/120.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/120.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u6218\u4e89\u4e4b\u5f71,\u8d6b\u5361\u91cc\u59c6,\u4eba\u9a6c,Hecarim,rm,zzzy,hlkm,zhanzhengzhiying,hekalimu,renma"},{"heroId":"121","name":"\u865a\u7a7a\u63a0\u593a\u8005","alias":"Khazix","title":"\u5361\u5179\u514b","roles":["assassin"],"isWeekFree":"0","attack":"9","defense":"4","magic":"3","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/121.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/121.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u865a\u7a7a\u63a0\u593a\u8005,\u87b3\u8782,\u5361\u5179\u514b,kzk,tl,xkldz,Khazix,xukonglueduozhe,tanglang,kazike"},{"heroId":"122","name":"\u8bfa\u514b\u8428\u65af\u4e4b\u624b","alias":"Darius","title":"\u5fb7\u83b1\u5384\u65af","roles":["fighter","tank"],"isWeekFree":"0","attack":"9","defense":"5","magic":"1","difficulty":"2","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/122.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/122.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u8bfa\u514b\u8428\u65af\u4e4b\u624b,\u5fb7\u83b1\u5384\u65af,\u8bfa\u624b,Darius,nuokesasizhishou,delaiesi,nuoshou,nksszs,ns,dles"},{"heroId":"126","name":"\u672a\u6765\u5b88\u62a4\u8005","alias":"Jayce","title":"\u6770\u65af","roles":["fighter","marksman"],"isWeekFree":"0","attack":"8","defense":"4","magic":"3","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/126.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/126.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u672a\u6765\u5b88\u62a4\u8005,\u6770\u65af,Jayce,js,wlshz,weilaishouhuzhe,jiesi"},{"heroId":"127","name":"\u51b0\u971c\u5973\u5deb","alias":"Lissandra","title":"\u4e3d\u6851\u5353","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"5","magic":"8","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/127.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/127.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"3000","camp":"","campId":"","keywords":"\u51b0\u971c\u5973\u5deb,\u51b0\u5973,\u4e3d\u6851\u5353,Lissandra,bn,lsz,bsnw,bingshuangnvwu,bingnv,lisangzhuo"},{"heroId":"131","name":"\u768e\u6708\u5973\u795e","alias":"Diana","title":"\u9edb\u5b89\u5a1c","roles":["fighter","mage"],"isWeekFree":"1","attack":"7","defense":"6","magic":"8","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/131.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/131.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u768e\u6708\u5973\u795e,\u9edb\u5b89\u5a1c,\u768e\u6708,Diana,jiaoyuenvshen,daianna,jiaoyue,jy,dan,jyns"},{"heroId":"133","name":"\u5fb7\u739b\u897f\u4e9a\u4e4b\u7ffc","alias":"Quinn","title":"\u594e\u56e0","roles":["marksman","assassin"],"isWeekFree":"0","attack":"9","defense":"4","magic":"2","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/133.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/133.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5fb7\u739b\u897f\u4e9a\u4e4b\u7ffc,\u594e\u56e0,\u9e1f\u4eba,ky,dmxyzz,Quinn,nr,demaxiyazhiyi,kuiyin,niaoren"},{"heroId":"134","name":"\u6697\u9ed1\u5143\u9996","alias":"Syndra","title":"\u8f9b\u5fb7\u62c9","roles":["mage","support"],"isWeekFree":"0","attack":"2","defense":"3","magic":"9","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/134.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/134.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6697\u9ed1\u5143\u9996,\u7403\u5973,\u8f9b\u5fb7\u62c9,qn,xdl,ahyy,Syndra,anheiyuanshou,qiunv,xindela"},{"heroId":"136","name":"\u94f8\u661f\u9f99\u738b","alias":"AurelionSol","title":"\u5965\u745e\u5229\u5b89\u7d22\u5c14","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"3","magic":"8","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/136.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/136.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u94f8\u661f\u9f99\u738b,\u5965\u745e\u5229\u5b89\u7d22\u5c14,\u7d22\u5c14,\u9f99\u738b,AurelionSol,zhuxinglongwang,aoruiliansuoer,suoer,longwang,zxlw,lw,se,arlasr"},{"heroId":"141","name":"\u5f71\u6d41\u4e4b\u9570","alias":"Kayn","title":"\u51ef\u9690","roles":["fighter","assassin"],"isWeekFree":"0","attack":"10","defense":"6","magic":"1","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/141.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/141.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5f71\u6d41\u4e4b\u9570,\u51ef\u9690,ky,ylzl,Kayn,yingliuzhilian,kaiyin"},{"heroId":"142","name":"\u66ae\u5149\u661f\u7075","alias":"Zoe","title":"\u4f50\u4f0a","roles":["mage","support"],"isWeekFree":"0","attack":"1","defense":"7","magic":"8","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/142.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/142.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u66ae\u5149\u661f\u7075,\u4f50\u4f0a,zy,mgxl,Zoe,muguangxingling,zuoyi"},{"heroId":"143","name":"\u8346\u68d8\u4e4b\u5174","alias":"Zyra","title":"\u5a55\u62c9","roles":["mage","support"],"isWeekFree":"0","attack":"4","defense":"3","magic":"8","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/143.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/143.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u8346\u68d8\u4e4b\u5174,\u5a55\u62c9,jl,jjzx,Zyra,jingjizhixing,jiela"},{"heroId":"145","name":"\u865a\u7a7a\u4e4b\u5973","alias":"Kaisa","title":"\u5361\u838e","roles":["marksman"],"isWeekFree":"0","attack":"8","defense":"5","magic":"3","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/145.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/145.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u865a\u7a7a\u4e4b\u5973,\u5361\u838e,ks,xkzn,Kaisa,xukongzhinv,kasha"},{"heroId":"147","name":"\u661f\u7c41\u6b4c\u59ec","alias":"Seraphine","title":"\u8428\u52d2\u82ac\u59ae","roles":["mage","support"],"isWeekFree":"0","attack":"0","defense":"0","magic":"0","difficulty":"0","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/147.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/147.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u8428\u52d2\u82ac\u59ae,\u661f\u7c41\u6b4c\u59ec,Seraphine,saleifenni,xinglaigeji"},{"heroId":"150","name":"\u8ff7\u5931\u4e4b\u7259","alias":"Gnar","title":"\u7eb3\u5c14","roles":["fighter","tank"],"isWeekFree":"0","attack":"6","defense":"5","magic":"5","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/150.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/150.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u8ff7\u5931\u4e4b\u7259,\u7eb3\u5c14,Gnar,ne,mszy,mishizhiya,naer"},{"heroId":"154","name":"\u751f\u5316\u9b54\u4eba","alias":"Zac","title":"\u624e\u514b","roles":["tank","fighter"],"isWeekFree":"0","attack":"3","defense":"7","magic":"7","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/154.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/154.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3000","camp":"","campId":"","keywords":"\u751f\u5316\u9b54\u4eba,\u624e\u514b,Zac,shenghuamoren,zhake,zk,shmr"},{"heroId":"157","name":"\u75be\u98ce\u5251\u8c6a","alias":"Yasuo","title":"\u4e9a\u7d22","roles":["fighter","assassin"],"isWeekFree":"0","attack":"8","defense":"4","magic":"4","difficulty":"10","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/157.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/157.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u75be\u98ce\u5251\u8c6a,\u5251\u8c6a,\u4e9a\u7d22,Yasuo,ys,jh,jfjh,jifengjianhao,jianhao,yasuo"},{"heroId":"161","name":"\u865a\u7a7a\u4e4b\u773c","alias":"Velkoz","title":"\u7ef4\u514b\u5179","roles":["mage"],"isWeekFree":"0","attack":"2","defense":"2","magic":"10","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/161.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/161.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u865a\u7a7a\u4e4b\u773c,\u5927\u773c,\u7ef4\u514b\u5179,wkz,dy,xkzy,Velkoz,xukongzhiyan,dayan,weikezi"},{"heroId":"163","name":"\u5ca9\u96c0","alias":"Taliyah","title":"\u5854\u8389\u57ad","roles":["mage","support"],"isWeekFree":"0","attack":"1","defense":"7","magic":"8","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/163.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/163.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5ca9\u96c0,\u5c0f\u9e1f,\u5854\u8389\u57ad,tly,xn,yq,Taliyah,yanque,xiaoniao,taliya"},{"heroId":"164","name":"\u9752\u94a2\u5f71","alias":"Camille","title":"\u5361\u871c\u5c14","roles":["fighter","tank"],"isWeekFree":"0","attack":"8","defense":"6","magic":"3","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/164.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/164.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u9752\u94a2\u5f71,\u5361\u871c\u5c14,\u5361\u5bc6\u5c14,Camille,\u817f\u5973,qinggangying,kamier,kamier,tuinv,qgy,kme,tn"},{"heroId":"166","name":"\u5f71\u54e8","alias":"Akshan","title":"\u963f\u514b\u5c1a","roles":["marksman","assassin"],"isWeekFree":"1","attack":"0","defense":"0","magic":"0","difficulty":"0","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/166.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/166.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5f71\u54e8,\u963f\u514b\u5c1a,\u963f\u514b,\u963f,yingshao,akeshang,ake,a"},{"heroId":"201","name":"\u5f17\u96f7\u5c14\u5353\u5fb7\u4e4b\u5fc3","alias":"Braum","title":"\u5e03\u9686","roles":["support","tank"],"isWeekFree":"1","attack":"3","defense":"9","magic":"4","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/201.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/201.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5f17\u96f7\u5c14\u5353\u5fb7\u4e4b\u5fc3,\u5e03\u9686,bl,Braum,flezdzx,fuleierzhuodezhixin,bulong"},{"heroId":"202","name":"\u620f\u547d\u5e08","alias":"Jhin","title":"\u70ec","roles":["marksman","mage"],"isWeekFree":"0","attack":"10","defense":"2","magic":"6","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/202.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/202.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u620f\u547d\u5e08,\u70ec,Jhin,j,xms,ximingshi,jin"},{"heroId":"203","name":"\u6c38\u730e\u53cc\u5b50","alias":"Kindred","title":"\u5343\u73cf","roles":["marksman"],"isWeekFree":"0","attack":"8","defense":"2","magic":"2","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/203.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/203.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6c38\u730e\u53cc\u5b50,\u5343\u73cf,Kindred,qj,ylsz,yonglieshuangzi,qianjue"},{"heroId":"221","name":"\u7956\u5b89\u82b1\u706b","alias":"Zeri","title":"\u6cfd\u4e3d","roles":["marksman"],"isWeekFree":"0","attack":"8","defense":"5","magic":"3","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/221.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/221.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"7800","couponPrice":"4500","camp":"","campId":"","keywords":""},{"heroId":"222","name":"\u66b4\u8d70\u841d\u8389","alias":"Jinx","title":"\u91d1\u514b\u4e1d","roles":["marksman"],"isWeekFree":"0","attack":"9","defense":"2","magic":"4","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/222.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/222.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u66b4\u8d70\u841d\u8389,\u841d\u8389,\u91d1\u514b\u4e1d,Jinx,jks,ll,bzll,baozouluoli,luoli,jinkesi,\u91d1\u514b\u4e1d"},{"heroId":"223","name":"\u6cb3\u6d41\u4e4b\u738b","alias":"TahmKench","title":"\u5854\u59c6","roles":["support","tank"],"isWeekFree":"0","attack":"3","defense":"9","magic":"6","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/223.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/223.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6cb3\u6d41\u4e4b\u738b,hama,\u5854\u59c6,tm,hlzw,TahmKench,heliuzhiwang,tamu"},{"heroId":"234","name":"\u7834\u8d25\u4e4b\u738b","alias":"Viego","title":"\u4f5b\u8036\u6208","roles":["assassin","fighter"],"isWeekFree":"0","attack":"6","defense":"4","magic":"2","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/234.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/234.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u7834\u8d25\u4e4b\u738b,\u4f5b\u8036\u6208,\u7834\u8d25,\u4f5b,pobaizhiwang,fuyege,pobai,fu"},{"heroId":"235","name":"\u6da4\u9b42\u5723\u67aa","alias":"Senna","title":"\u8d5b\u5a1c","roles":["marksman","support"],"isWeekFree":"0","attack":"7","defense":"2","magic":"6","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/235.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/235.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6da4\u9b42\u5723\u67aa,\u8d5b\u5a1c,\u5976\u67aa,Senna,nq,sn,qhsq,dihunshengqiang,saina,naiqiang"},{"heroId":"236","name":"\u5723\u67aa\u6e38\u4fa0","alias":"Lucian","title":"\u5362\u9521\u5b89","roles":["marksman"],"isWeekFree":"0","attack":"8","defense":"5","magic":"3","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/236.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/236.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5723\u67aa\u6e38\u4fa0,\u5362\u9521\u5b89,\u5965\u5df4\u9a6c,Lucian,abm,lxa,sqyx,shengqiangyouxia,luxian,aobama"},{"heroId":"238","name":"\u5f71\u6d41\u4e4b\u4e3b","alias":"Zed","title":"\u52ab","roles":["assassin"],"isWeekFree":"0","attack":"9","defense":"2","magic":"1","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/238.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/238.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5f71\u6d41\u4e4b\u4e3b,\u52ab,j,ylzz,Zed,yingliuzhizhu,jie"},{"heroId":"240","name":"\u66b4\u6012\u9a91\u58eb","alias":"Kled","title":"\u514b\u70c8","roles":["fighter","tank"],"isWeekFree":"0","attack":"8","defense":"2","magic":"2","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/240.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/240.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u66b4\u6012\u9a91\u58eb,\u514b\u70c8,kl,bnqs,baonuqishi,kelie"},{"heroId":"245","name":"\u65f6\u95f4\u523a\u5ba2","alias":"Ekko","title":"\u827e\u514b","roles":["assassin","fighter"],"isWeekFree":"0","attack":"5","defense":"3","magic":"7","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/245.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/245.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u65f6\u95f4\u523a\u5ba2,\u827e\u514b,Ekko,shijiancike,aike,ak,sjck"},{"heroId":"246","name":"\u5143\u7d20\u5973\u7687","alias":"Qiyana","title":"\u5947\u4e9a\u5a1c","roles":["assassin","fighter"],"isWeekFree":"0","attack":"0","defense":"2","magic":"4","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/246.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/246.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5143\u7d20\u5973\u7687,\u5947\u4e9a\u5a1c,qyn,ysnh,Qiyana,yuansunvhuang,qiyana"},{"heroId":"254","name":"\u76ae\u57ce\u6267\u6cd5\u5b98","alias":"Vi","title":"\u851a","roles":["fighter","assassin"],"isWeekFree":"0","attack":"8","defense":"5","magic":"3","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/254.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/254.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u76ae\u57ce\u6267\u6cd5\u5b98,\u62f3\u5973,\u851a,v,qv,pczfg,Vi,pichengzhifaguan,quannv,wei"},{"heroId":"266","name":"\u6697\u88d4\u5251\u9b54","alias":"Aatrox","title":"\u4e9a\u6258\u514b\u65af","roles":["fighter","tank"],"isWeekFree":"0","attack":"8","defense":"4","magic":"3","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/266.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/266.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5251\u9b54,\u4e9a\u6258\u514b\u65af,\u6697\u88d4\u5251\u9b54,jianmo,yatuokesi,anyijianmo,Aatrox,jm,ayjm,ytks"},{"heroId":"267","name":"\u5524\u6f6e\u9c9b\u59ec","alias":"Nami","title":"\u5a1c\u7f8e","roles":["support","mage"],"isWeekFree":"0","attack":"4","defense":"3","magic":"7","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/267.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/267.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"4800","couponPrice":"3500","camp":"","campId":"","keywords":"\u5524\u6f6e\u9c9b\u59ec,\u9c9b\u59ec,\u5a1c\u7f8e,nm,jj,hcjj,Nami,huanchaojiaoji,jiaoji,namei"},{"heroId":"268","name":"\u6c99\u6f20\u7687\u5e1d","alias":"Azir","title":"\u963f\u5179\u5c14","roles":["mage","marksman"],"isWeekFree":"0","attack":"6","defense":"3","magic":"8","difficulty":"9","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/268.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/268.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6c99\u6f20\u7687\u5e1d,\u963f\u5179\u5c14,\u6c99\u7687,Azir,shamohuangdi,azier,shahuang,smhd,aze,sh"},{"heroId":"350","name":"\u9b54\u6cd5\u732b\u54aa","alias":"Yuumi","title":"\u60a0\u7c73","roles":["support","mage"],"isWeekFree":"0","attack":"5","defense":"1","magic":"8","difficulty":"2","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/350.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/350.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u9b54\u6cd5\u732b\u54aa,\u732b,\u732b\u54aa,\u60a0\u7c73,cat,m,mm,mfmm,ym,Yuumi,mofamaomi,mao,maomi,youmi"},{"heroId":"360","name":"\u6c99\u6f20\u73ab\u7470","alias":"Samira","title":"\u838e\u5f25\u62c9","roles":["marksman"],"isWeekFree":"1","attack":"8","defense":"5","magic":"3","difficulty":"6","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/360.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/360.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u838e\u5f25\u62c9,\u6c99\u6f20\u73ab\u7470,Samira,sml,smmg,shamila,shamomeigui"},{"heroId":"412","name":"\u9b42\u9501\u5178\u72f1\u957f","alias":"Thresh","title":"\u9524\u77f3","roles":["support","fighter"],"isWeekFree":"0","attack":"5","defense":"6","magic":"6","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/412.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/412.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u9b42\u9501\u5178\u72f1\u957f,\u9524\u77f3,Thresh,cs,hsdyz,hunsuodianyuzhang,chuishi"},{"heroId":"420","name":"\u6d77\u517d\u796d\u53f8","alias":"Illaoi","title":"\u4fc4\u6d1b\u4f0a","roles":["fighter","tank"],"isWeekFree":"1","attack":"8","defense":"6","magic":"3","difficulty":"4","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/420.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/420.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6d77\u517d\u796d\u53f8,\u4fc4\u6d1b\u4f0a,\u89e6\u624b\u5988,Illaoi,csm,ely,hsjs,haishoujisi,eluoyi,chushouma"},{"heroId":"421","name":"\u865a\u7a7a\u9041\u5730\u517d","alias":"RekSai","title":"\u96f7\u514b\u585e","roles":["fighter"],"isWeekFree":"0","attack":"8","defense":"5","magic":"2","difficulty":"3","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/421.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/421.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u865a\u7a7a\u9041\u5730\u517d,\u6316\u6398\u673a,\u96f7\u514b\u8d5b,\u96f7\u514b\u585e,lks,wjj,xkdds,RekSai,xukongdundishou,wajueji,leikesai,leikesai"},{"heroId":"427","name":"\u7fe0\u795e","alias":"Ivern","title":"\u827e\u7fc1","roles":["support","mage"],"isWeekFree":"0","attack":"3","defense":"5","magic":"7","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/427.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/427.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u7fe0\u795e,\u827e\u7fc1,\u5c0f\u83ca,Ivern,xj,cs,aw,cuishen,aiweng,xiaoju"},{"heroId":"429","name":"\u590d\u4ec7\u4e4b\u77db","alias":"Kalista","title":"\u5361\u8389\u4e1d\u5854","roles":["marksman"],"isWeekFree":"0","attack":"8","defense":"2","magic":"4","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/429.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/429.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u590d\u4ec7\u4e4b\u77db,\u5361\u8389\u4e1d\u5854,Kalista,fczm,klst,fuchouzhimao,kalisita"},{"heroId":"432","name":"\u661f\u754c\u6e38\u795e","alias":"Bard","title":"\u5df4\u5fb7","roles":["support","mage"],"isWeekFree":"0","attack":"4","defense":"4","magic":"5","difficulty":"9","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/432.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/432.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u661f\u754c\u6e38\u795e,\u5df4\u5fb7,Bard,xingjieyoushen,bade,xjys,bd"},{"heroId":"497","name":"\u5e7b\u7fce","alias":"Rakan","title":"\u6d1b","roles":["support"],"isWeekFree":"0","attack":"2","defense":"4","magic":"8","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/497.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/497.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5e7b\u7fce,\u6d1b,l,hl,Rakan,huanling,luo"},{"heroId":"498","name":"\u9006\u7fbd","alias":"Xayah","title":"\u971e","roles":["marksman"],"isWeekFree":"0","attack":"10","defense":"6","magic":"1","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/498.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/498.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u9006\u7fbd,\u971e,x,ny,Xayah,niyu,xia"},{"heroId":"516","name":"\u5c71\u9690\u4e4b\u7130","alias":"Ornn","title":"\u5965\u6069","roles":["tank","fighter"],"isWeekFree":"0","attack":"5","defense":"9","magic":"3","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/516.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/516.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u5c71\u9690\u4e4b\u7130,\u5965\u6069,Ornn,an,syzy,shanyinzhiyan,aoen"},{"heroId":"517","name":"\u89e3\u8131\u8005","alias":"Sylas","title":"\u585e\u62c9\u65af","roles":["mage","assassin"],"isWeekFree":"0","attack":"3","defense":"4","magic":"8","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/517.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/517.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u89e3\u8131\u8005,\u585e\u62c9\u65af,sls,suannan,sn,jtz,Sylas,jietuozhe,sailasi"},{"heroId":"518","name":"\u4e07\u82b1\u901a\u7075","alias":"Neeko","title":"\u59ae\u853b","roles":["mage","support"],"isWeekFree":"0","attack":"1","defense":"1","magic":"9","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/518.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/518.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u4e07\u82b1\u901a\u7075,\u59ae\u853b,neeko,nk,whtl,wanhuatongling,nikou"},{"heroId":"523","name":"\u6b8b\u6708\u4e4b\u8083","alias":"Aphelios","title":"\u5384\u6590\u7409\u65af","roles":["marksman"],"isWeekFree":"0","attack":"6","defense":"2","magic":"1","difficulty":"10","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/523.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/523.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6b8b\u6708\u4e4b\u8083,\u5384\u6590\u7409\u65af,Aphelios,efls,cyzs,canyuezhisu,efeiliusi"},{"heroId":"526","name":"\u9555\u94c1\u5c11\u5973","alias":"Rell","title":"\u82ae\u5c14","roles":["tank","support"],"isWeekFree":"0","attack":"0","defense":"0","magic":"0","difficulty":"0","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/526.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/526.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"7800","couponPrice":"4500","camp":"","campId":"","keywords":"\u9555\u94c1\u5c11\u5973,\u82ae\u5c14,\u9555\u94c1,,rongtieshaonv,ruier,rongtie"},{"heroId":"555","name":"\u8840\u6e2f\u9b3c\u5f71","alias":"Pyke","title":"\u6d3e\u514b","roles":["support","assassin"],"isWeekFree":"0","attack":"9","defense":"3","magic":"1","difficulty":"7","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/555.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/555.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u8840\u6e2f\u9b3c\u5f71,\u6d3e\u514b,pk,xggy,Pyke,xuegangguiying,paike"},{"heroId":"711","name":"\u6101\u4e91\u4f7f\u8005","alias":"Vex","title":"\u8587\u53e4\u4e1d","roles":["mage"],"isWeekFree":"0","attack":"0","defense":"0","magic":"0","difficulty":"0","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/711.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/711.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":""},{"heroId":"777","name":"\u5c01\u9b54\u5251\u9b42","alias":"Yone","title":"\u6c38\u6069","roles":["assassin","fighter"],"isWeekFree":"0","attack":"8","defense":"4","magic":"4","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/777.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/777.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u6c38\u6069,\u5c01\u9b54\u5251\u9b42,ye,fmjh,Yone,yongen,fengmojianhun"},{"heroId":"875","name":"\u8155\u8c6a","alias":"Sett","title":"\u745f\u63d0","roles":["fighter","tank"],"isWeekFree":"0","attack":"8","defense":"5","magic":"1","difficulty":"2","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/875.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/875.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u8155\u8c6a,\u745f\u63d0,jinfu,jf,Sett,st,wh,wanhao,seti"},{"heroId":"876","name":"\u542b\u7f9e\u84d3\u857e","alias":"Lillia","title":"\u8389\u8389\u5a05","roles":["fighter","mage"],"isWeekFree":"0","attack":"0","defense":"2","magic":"10","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/876.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/876.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u542b\u7f9e\u84d3\u857e,\u8389\u8389\u5a05,\u5c0f\u9e7f,lly,hxbl,Lillia,hanxiubeilei,liliya,xiaolu"},{"heroId":"887","name":"\u7075\u7f57\u5a03\u5a03","alias":"Gwen","title":"\u683c\u6e29","roles":["fighter","assassin"],"isWeekFree":"0","attack":"7","defense":"4","magic":"5","difficulty":"5","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/887.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/887.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"6300","couponPrice":"4500","camp":"","campId":"","keywords":"\u7075\u7f57\u5a03\u5a03,\u683c\u6e29,\u7075,\u5a03wa,gw,Gw,,lingluowawa,gewen,ling,wa"},{"heroId":"888","name":"\u70bc\u91d1\u7537\u7235","alias":"Renata","title":"\u70c8\u5a1c\u5854 \u00b7 \u6208\u62c9\u65af\u514b","roles":["support","mage"],"isWeekFree":"0","attack":"2","defense":"6","magic":"9","difficulty":"8","selectAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/choose\/888.ogg","banAudio":"https:\/\/game.gtimg.cn\/images\/lol\/act\/img\/vo\/ban\/888.ogg","isARAMweekfree":"0","ispermanentweekfree":"0","changeLabel":"\u65e0\u6539\u52a8","goldPrice":"7800","couponPrice":"4500","camp":"","campId":"","keywords":""}],"version":"12.5","fileName":"hero_list.js","fileTime":"2022-03-10 15:01:39"}
```



