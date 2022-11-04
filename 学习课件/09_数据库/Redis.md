# Redis数据库

#### Redis 简介

Redis是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。

Redis与其他 key- value 缓存产品有以下三个特点：

Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。

Redis不仅仅支持简单的key-value类型的数据，同时还提供string，list，set，zset，hash等数据结构的存储。

redis： 半持久化，存储于内存和硬盘

#### Redis和MongoDB的区别

Redis是完全在内存中保存数据的数据库，使用磁盘只是为了持久性目的,Redis数据全部存在内存，定期写入磁盘，当内存不够时，可以选择指定的LRU算法删除数据,持久化是使用RDB方式或者aof方式。

mongodb是文档型的非关系型数据库，MongoDB更类似MySQL，支持字段索引、游标操作，其优势在于查询功能比较强大，擅长查询JSON数据，能存储海量数据，但是不支持事务。

## 一 前期准备

#### 下载地址:

https://github.com/ServiceStack/redis-windows

https://github.com/MSOpenTech/redis/releases

#### 设置  redis.windows.conf

455行 maxheap 1024000000   设置最大的数据堆的大小

387行 requirepass 123456		设置数据库的密码

## 二 启动服务

cd C:\redis64-2.8.2101

C:\redis64-2.8.2101>redis-server.exe redis.windows.conf  #执行 redis-server.exe 并加载Windows的配置文件

C:\redis64-2.8.2101—>dump.rdb  为数据文件

##### mac 下安装也可以使用 homebrew，homebrew 是 mac 的包管理器。

1、执行 brew install redis

2、启动 redis，可以使用后台服务启动 brew services start redis。或者直接启动：redis-server /usr/local/etc/redis.conf

## 三 测试是否连接成功

##### 再打开一个新的终端

##### 输入密码 (这个密码就是在redis.windows.conf里面设置的密码)

C:\redis64-2.8.2101>Redis-cli.exe

127.0.0.1:6379>auth '123456'    

#### 注意:

密码 为 字符串类型

## 四 Redis值的类型

1. ##### 字符串 String

2. ##### 哈希 hash

3. ##### 列表 list

4. ##### 集合 set

5. ##### 有序集合 zset

##### 数据操作的全部命令：

http://redis.cn/commands.html

config get databases 查看所有的数据库 数据库以0开始 一共16个

### (1) String

概述：String是redis最基本的类型，最大能存储512MB的数据，String类型是二进制安全的，即可以存储任何数据、比如数字、图片、序列化对象等

一个key对应一个value

string类型是Redis最基本的数据类型，一个键最大能存储512MB。

#### 1、设置键值

##### A、设置键值

> set key value 

```python
set name "zhangsan"
```

##### B、设置键值及过期时间，以秒为单位

> setex key seconds value

```python
setex name 10 'zhangsan'
```

##### C、查看有效时间，以秒为单位

> ttl key

```python
ttl name
```

##### D、取消过期时间

> persist key

```
persist name
```

##### E、只有在 key 不存在时设置 key 的值

> setnx key value

```
 setnx name 'a'
```



##### E、设置多个键值

> mset key value [key value ……]

```python
mset name 'zs' age 18 	
```



#### 2、key的操作

##### A.根据键获取值，如果键不存在则返回None(null 0 nil)

> get key

 `get name`

#####  B、根据多个键获取多个值

> mget key [key ……]

  `mget name age`g

##### C、返回 key 中字符串值的子字符

> getrange key start end

```python
getrange name 0 4
```

##### D、将给定 key 的值设为 value ，并返回 key 的旧值(old value)

> getset key value

```python
getset name 'x'
```



#### 3、运算

##### 要求：值是字符串类型的数字

##### A、将key对应的值加1

> incr key   

 `incr age`

##### B、将key对应的值减1

> decr key

`decr age`

#####  C、将key对应的值加整数

> incrby key intnum

` incrby age 10	`	

#####  D、将key对应的值减整数

> decrby key intnum

`decrby age 10`

##### E、获取值长度

> strlen key

  `strlen age`



## key 键的操作

##### A、查找所有符合给定模式pattern（正则表达式）的 key 

> keys *

> KEYS \*o\*

> KEYS t??

##### 支持的正则表达模式：

- `h?llo` 匹配 `hello`, `hallo` 和 `hxllo`
- `h*llo` 匹配 `hllo` 和 `heeeello`
- `h[ae]llo` 匹配 `hello` 和 `hallo,` 但是不匹配 `hillo`
- `h[^e]llo` 匹配 `hallo`, `hbllo`, … 但是不匹配 `hello`
- `h[a-b]llo` 匹配 `hallo` 和 `hbllo`

##### B、判断键是否存在，如果存在返回1，不存在返回0

> exists key

`exists name`

##### C、查看键对应的value类型

> type key

 `type name`

##### D、删除键及对应的值

> del key [key ……]

##### E、设置过期时间，以秒为单位

> expire key seconds

   `expire age 10`

##### F、查看有效时间，以秒为单位

> ttl key

##### H、以毫秒为单位返回 key 的剩余的过期时间

> pttl key 

##### I、移除 key 的过期时间，key 将持久保持

> persist key

##### J、删除所有的key

> flushdb	删除当前数据库中的所有

> flushall		删除所有数据库中的key

##### K、修改 key 的名称

> rename key newkey

##### L、将key移动到指定的数据库中

> Move key db

```python
move name 1	#将name 移动到数据库1
```

##### M、随机返回一个key

> randomkey



### (2) hash

##### 概述：hash用于存储对象

{

​	name:"tom",
​	age:18

}

Redis hash 是一个键值(key=>value)对集合。

#### 1、设置

##### a、设置单个值

> hset key field value

```python
redis> e
(integer) 1z
redis> HGET myhash field1
"Hello"
```

##### b、设置多个值

> hmset key field value [field value ……]

```python
hmset a x "o" y "y" z "z"
```
##### C 为哈希表 key 中的指定字段的整数值加上增量 increment 

> hincrby key field incrment

```python
hincrby hh age 10
```

##### E 为哈希表 key 中的指定字段的浮点数值加上增量 increment

> HINCRBYFLOAT key field increment

hincrbyfloat hh money 0.1

##### F 只有在字段 field 不存在时，设置哈希表字段的值

> hsetnx key field value

```python
hset user age 20
```



#### 2、获取

##### A、获取一个属性的值

> hget key field

`hget name field1`

##### B、获取多个属性的值

> hmget key filed [filed ……]

##### C、获取所有字段和值

> hgetall key

##### D、获取所有字段

> hkeys key

##### E、获取所有值

> hvals key

##### F、返回包含数据的个数

> hlen key



#### 3、其它

##### A、判断属性是否存在，存在返回1，不存在返回0

> hexists key field

`hexists a x`

##### B、删除字段及值	

> hdel key field [field ……]

` hdel a x y z`

##### C、返回值的字符串长度  起始版本 3.2	

> hstrlen key field



### (3) 列表 list

概述：Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）

### 1、设置

##### A、在头部插入

> lpush key value [vlaue ……] 

```python
lpush demo 2 3`
```

##### 将一个值插入到已存在的列表头部，列表不存在时操作无效

> Lpushx  key val

```
lpushx list 'a'
```

##### B、在尾部插入

> rpush key value [vlaue ……]


```python
rpush demo 2 1
```

##### 为已存在的列表添加值

> rpushx  key val

```python
rpushx mm 'a'	
```



#### 2、获取

##### A、移除并返回key对应的list的第一个元素

>lpop key

```python
lpop demo
```

##### B、移除并返回key对应的list的最后一个元素

>rpop key

```python
rpop demo
```

##### C、返回存储在key的列表中的指定范围的元素

> lrange key  start end

```python
lrange demo 0 -1	#查看列表中的所有元素
```
注意：start end都是从0开始
注意：偏移量可以是负数



#### 3、其它

##### A、裁剪列表，改为原集合的一个子集

> ltrim key start end

```python
ltrim demo 1 -1	#将索引为1 到 -1的元素裁剪出来
```

注意：start end都是从0开始
注意：偏移量可以是负数

##### B、返回存储在key里的list的长度

> llen key

##### C、返回列表中索引对应的值

> lindex key index

```python
LINDEX mylist 0
```



### 四 集合 set

概述：无序集合，元素类型为String类型，元素具有唯一性，不重复

{ 'a','b'}

#### 1、设置

##### A、添加元素

> sadd key member [member ……]

```python
sadd set 'a' 'b' 'c'
```

#### 2、获取

##### A、返回key集合中所有元素

> smembers key

```python
smembers set
```

##### B、返回集合元素个数

> scard key

```python
scard set
```

##### C、移除并返回集合中的一个随机元素

> Spop  key

```
spop set
```

##### D、返回集合中一个或多个随机数

> srandmember  key  count

```python
srandmember set		#返回一个随机元素
srandmember set 2	#返回2个随机元素
```

##### E、移除集合中一个或多个成员

> srem  key   member1 [memkber2]

```python
srem set 'd' 'b'
```



#### 3、集合的其它操作

##### A、求多个集合的交集

> sinter key [key ……]

```python
 sinter m l	#求集合l和集合m的交集
```

##### B、求多个集合的差集

> sdiff key [key ……]

```python
sdiff m l	#求差集 注意比较顺序
```

##### D、判断元素是否在集合中，存在返回1，不存在返回0

> sismember key member

```python
sismember m 'a'   #集合m中是否存在元素'a'
```



### 五 有序集合 zset

##### 概述：

##### a、有序集合，元素类型为String，元素具有唯一性，不能重复

##### b、每个元素都会关联一个double类型的score(表示权重),通过权重的大小排序，元素的score可以相同

#### 1、设置

##### A、添加

> zadd key score member [score member ……]

```python
zadd zset 1 a 5 b 3 c 2 d 4 e
```

##### B、有序集合中对指定成员的分数加上增量 increment

> Zincrby	key increment  mcfaember

```
zincrby zset 10 'a'   #给a的权重上加10
```



#### 2、获取

##### A、返回指定范围的元素

> zrange key start end

```python
zrange z1 0 -1
```

##### B、返回元素个数

> zcard key

```python
 zcard z1
```

##### C、返回有序集合key中，score在min和max之间的元素的个数

> zcount key min max

##### D、返回有序集合key中，成员member的score值

> zscore key member

```python
zscore l 'c'	#s返回c的权重
```

##### E、当前集合所有的值和权重

> ZRANGE key 0 -1 WITHSCORES

##### F、返回有序集合中指定分数区间内的成员，分数由低到高排序。

> ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]

区间及无限

min和max可以是-inf和+inf，这样一来，你就可以在不知道有序集的最低和最高score值的情况下，使用ZRANGEBYSCORE这类命令。

```sql
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZRANGEBYSCORE myzset -inf +inf
1) "one"
2) "two"
3) "three"
redis> ZRANGEBYSCORE myzset 1 2
1) "one"
2) "two"
```



### 3、删除

##### A 从排序的集合中删除一个或多个成员

当key存在，但是其不是有序集合类型，就返回一个错误。

> ZREM key member [member ...]

```sql
redis> ZADD myzset 1 "one"
(integer) 1
redis> ZADD myzset 2 "two"
(integer) 1
redis> ZADD myzset 3 "three"
(integer) 1
redis> ZREM myzset "two"
(integer) 1
redis> ZRANGE myzset 0 -1 WITHSCORES
1) "one"
2) "1"
3) "three"
4) "3"
redis> 
```



#### 数据库:

默认在 数据库 0

select num  进行数据库的切换

select  1  #进入到数据库1



## 五、Redis 安全

注意：当前密码修改后如果服务重启则需要重新设定

我们可以通过 redis 的配置文件设置密码参数，这样客户端连接到 redis 服务就需要密码验证，这样可以让你的 redis 服务更安全。

##### 实例

我们可以通过以下命令查看是否设置了密码验证：

```
127.0.0.1:6379> CONFIG get requirepass
1) "requirepass"
2) ""
```

默认情况下 requirepass 参数是空的，这就意味着你无需通过密码验证就可以连接到 redis 服务。

你可以通过以下命令来修改该参数：

```
127.0.0.1:6379> CONFIG set requirepass "lucky"
OK
127.0.0.1:6379> CONFIG get requirepass
1) "requirepass"
2) "lucky"
```

设置密码后，客户端连接 redis 服务就需要密码验证，否则无法执行命令。

#### 语法

**AUTH** 命令基本语法格式如下：

```
127.0.0.1:6379> AUTH password
```

##### 实例

```
127.0.0.1:6379> AUTH "lucky"
OK
127.0.0.1:6379> SET mykey "Test value"
OK
127.0.0.1:6379> GET mykey
"Test value"
```



## 六、Redis 数据备份与恢复

Redis **SAVE** 命令用于创建当前数据库的备份。

##### 语法

redis Save 命令基本语法如下：

```
redis 127.0.0.1:6379> SAVE 
```

##### 实例

```
redis 127.0.0.1:6379> SAVE 
OK
```

该命令将在 redis 安装目录中创建dump.rdb文件。

------

#### 恢复数据

如果需要恢复数据，只需将备份文件 (dump.rdb) 移动到 redis 安装目录并启动服务即可。获取 redis 目录可以使用 **CONFIG** 命令，如下所示：

```
redis 127.0.0.1:6379> CONFIG GET dir
1) "dir"
2) "/usr/local/redis/bin"
```

以上命令 **CONFIG GET dir** 输出的 redis 安装目录为 /usr/local/redis/bin。

------

#### Bgsave

创建 redis 备份文件也可以使用命令 **BGSAVE**，该命令在后台执行。

##### 实例

```
127.0.0.1:6379> BGSAVE

Background saving started
```



## 七、Python操作redis

### 1、安装

pip install redis

**导入**

import  redis

### 2、连接方式

**redis提供了2个方法**

+ StrictRedis：实现大部分官方的命令
+ Redis：是StrictRedis的子类，用于向后兼容旧版的redis。

##### 官方推荐使用StrictRedis方法。 

##### 举例（普通连接）：

```python
import redis

# decode_responses=True  自动解码
r = redis.Redis(host='127.0.0.1',port=6379,password='123c456',db=0,decode_responses=True) #默认数据库为0 

r = redis.StrictRedis(host='10.10.2.14',port=6379,password='123456',decode_responses=True)
```

##### 连接池：connection pool

 管理对一个redis server的所有连接，避免每次建立，释放连接的开销。默认，每个redis实例都会维护一个自己的连接池，可以直接建立一个连接池，作为参数传给redis，这样可以实现多个redis实例共享一个连接池。

举例（连接池）：

```python
pool = redis.ConnectionPool(host='127.0.0.1',port=6379,db=0,password='123456',decode_responses=True)

r = redis.Redis(connection_pool=pool)
```



