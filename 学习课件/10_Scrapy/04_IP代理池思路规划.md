# IP代理池

## 一、功能的规划

目录结构

+ get_ip.py    抓取免费ip的文件
+ test_ip.py   测试ip是否可用的文件
+ proxy_redis.py   存储和处理当前的ip
+ app.py    请求这个文件的接口    返回可用的ip
+ settings.py  全局的配置文件
+ main.py   整个ip代理池运行的入口



## 二、知识

### 1、需要用到的redis命令

+ zadd  添加集合

  zadd proxy_redis 1 a 2 b  添加有序集合中a 成员 权重1  b成员 权重2

+ zscore  获取成员的权重

  zscore proxy_redis a  获取成员a的权重

+ zincrby  增加/减少权重

  zincrby proxy_redis 10 a       给成员a 增加10权重

   zincrby proxy_redis -10 a    给成员a 减少10权重

+ zrange  获取范围区间的ip

   zrange proxy_redis 0 -1  获取所有的成员

+ zrangebyscore   获取权重区间范围的ip

   zrangebyscore proxy_redis 0 20     返回权重在0-20之间的成员

+ zrem  删除

  zrem proxy_redis a  删除成员a