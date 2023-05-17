# 爬虫开发第5期

## 在search中进行搜索（最好的方案）

- 在url上进行搜索，在?前面 一个单词接着一个单词搜

​            https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token=

​            1. v1

​            2. url/v1

​            3. player/url/v1


​            或者该url中某些看着比较特殊的单词. 也可以单独搜索 ...

- 搜参数(请求上的各种参数(主要针对加密参数)

- 拦截器. 该网站使用的是异步. promise


## 如何抠代码

1. 找到入口. 把入口拿下来. 尝试着一个函数一个函数的去填补..

​		过程非常曲折...直到 最终的结果产生. 并且和你的预期相符...

2. 找到代码的边界

​		一个大闭包?
​		两个闭包之间.
​		肯定是具有相似性(人为的去判别)

3. 直接找第三方库. 需要经验的...

## headers挨着加这些东西：

1、UA

2、referer

3、Cookie

4、Content-type

不能随便加【Host】！！！！！

## 爬虫的post请求

1. 请求载荷（request payload）：只能给json数据，在请求头的content-type里也可以看到是json。

   这种情况一定要改headers，加上content-type（application/json; charset=UTF-8）

   给的数据也要转换成json，json.dumps()

   requests中传参直接使用json=data

2. 表单数据（form data）：直接给字典，data=字典。
   scrapy中，导包，from scrapy import FormRequest
