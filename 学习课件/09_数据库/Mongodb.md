# NoSQL Mongodb

- 下载mongodb的版本，两点注意
  - 根据业界规则，偶数为稳定版，如1.6.X，奇数为开发版，如1.7.X
  - 32bit的mongodb最大只能存放2G的数据，64bit就没有限制

**性能**

BSON格式的编码和解码都是非常快速的。它使用了C风格的数据表现形式，这样在各种语言中都可以高效地使用。

NoSQL(NoSQL = Not Only SQL )，意即"不仅仅是SQL"。

MongoDB 将数据存储为一个文档，数据结构由键值(key=>value)对组成。MongoDB 文档类似于 JSON 对象。字段值可以包含其他文档，数组及文档数组。



## 一、安装(windows)

下载mongodb的版本，两点注意

- 根据业界规则，偶数为稳定版，如1.6.X，奇数为开发版，如1.7.X
- 32bit的mongodb最大只能存放2G的数据，64bit就没有限制

首先去官网下载MongoDB的安装包, https://www.mongodb.com/try/download/community

![image-20210728093724660](Mongodb.assets/image-20210728093724660.png)

![image-20210728093838499](Mongodb.assets/image-20210728093838499.png)

![image-20210728093906551](Mongodb.assets/image-20210728093906551.png)

![image-20210728094404958](Mongodb.assets/image-20210728094404958.png)

![image-20210728094441168](Mongodb.assets/image-20210728094441168.png)

![image-20210728094521878](Mongodb.assets/image-20210728094521878.png)

![image-20210728094547434](Mongodb.assets/image-20210728094547434.png)

![image-20210728094627838](Mongodb.assets/image-20210728094627838.png)

![image-20210728094653296](Mongodb.assets/image-20210728094653296.png)

![image-20210728094727302](Mongodb.assets/image-20210728094727302.png)

![image-20210728094750500](Mongodb.assets/image-20210728094750500.png)



将mongodb目录下的bin文件夹添加到环境变量

![image-20210728095340874](Mongodb.assets/image-20210728095340874.png)

![image-20210728095433900](Mongodb.assets/image-20210728095433900.png)

![image-20210728095507330](Mongodb.assets/image-20210728095507330.png)

![image-20210728095631337](Mongodb.assets/image-20210728095631337.png)

![image-20210728100113133](Mongodb.assets/image-20210728100113133.png)

![image-20210729195132883](Mongodb.assets/image-20210729195132883.png)

![image-20210729195203348](Mongodb.assets/image-20210729195203348.png)

对于mac的安装可以使用homebrew安装.  或参考这里https://www.runoob.com/mongodb/mongodb-osx-install.html

## 一、MongoDB  概念解析

| SQL术语/概念 | MongoDB术语/概念 | 解释/说明    |
| -------- | ------------ | -------- |
| database | database     | 数据库      |
| table    | collection   | 数据库表/集合  |
| row      | document     | 数据记录行/文档 |
| column   | field        | 数据字段/域   |

## 二、数据类型

- 下表为MongoDB中常用的几种数据类型：
- Object ID：文档ID
- String：字符串，最常用，必须是有效的UTF-8
- Boolean：存储一个布尔值，true或false
- Integer：整数可以是32位或64位，这取决于服务器
- Double：存储浮点值
- Arrays：数组或列表，多个值存储到一个键
- Object：用于嵌入式的文档，即一个值为一个文档
- Null：存储Null值
- Timestamp：时间戳
- Date：存储当前日期或时间的UNIX时间格式

#### 需要注意的是：

1. 文档中的键/值对是有序的。
2. 文档中的值不仅可以是在双引号里面的字符串,还可以是其他几种数据类型（甚至可以是整个嵌入的文档)。
3. MongoDB区分类型和大小写。
4. MongoDB的文档不能有重复的键。
5. 文档的键是字符串。除了少数例外情况，键可以使用任意UTF-8字符。

#### 文档键命名规范：

- .和$有特别的意义，只有在特定环境下才能使用。
- 以下划线"_"开头的键是保留的(不是严格要求的)。




## 四、连接Mongodb

##### (1) cd mongo安装的目录/bin（如果没有配置环境变量的操作  当前窗口不能关闭！！！） 

输入 mongod.exe     --dbpath=路径

##### (2) 重新启动一个Windows的终端  再次进入到 **mongo安装的目录/bin**

​	cd   mongo安装的目录/bin

​	老版本：

​	mongo.exe   #此刻 进入到Mongodb数据库了

​	新版本：

​	mongo          #此刻 进入到Mongodb数据库了



## 五、 对于库的操作

#####  (1)  查看所有的库

​	show dbs

##### (2) 选择数据库 (如果使用的数据库存在 则使用 不存在 则创建)

​	use 库名 

​	注意:

​		新创建的数据库 默认你是看不到的 可以使用db/db.getName() 去查看当前所在的库   往新的库里创建集合

##### (3) 查看当前所在的数据库

```python
1. db
2. db.getName()
```

##### (4) 创建集合(也就是创建表) 

1. db.createCollection("集合名")

   例如：db.createCollection("user") #创建一个user的集合 在当前的库里

2. db.集合名.insert(文档)  #如果 当前的集合名不存在 那么就创建该集合 并插入文档(数据) 

注意：

```python
1. 在库里对于文档 集合的操作 统一使用db. (db代表当前的库)
2. 严格区分大小写
```

##### (5) 查看当前库下的所有集合

​	show collections

##### (6) 删除集合

​	db.集合名.drop()



## 六、INSERT

**老版本命令**

使用insert 

​	db.集合名.insert(文档)  #如果是添加数据

插入多条数据:

​	db.集合名.insert([文档]) #注意 一定要加[] 否则可能只会把 第一条文档插入进去

```
db.user.insert({'name':'lisi', 'age': 20})

db.user.insert([{'name':'lisi', 'age': 20},{'name': 'wangwu', 'age': 30}])
```

**新版本命令**

3.2 版本后还有以下几种语法可用于插入文档:**（建议使用）**

- **db.collection.insertOne**():向指定集合中插入一条文档数z据
- **db.collection.insertMany**():向指定集合中插入多条文档数据

```
db.user.insertOne({'name':'lisi', 'age': 20})

db.user.insertMany([{'name':'lisi', 'age': 20},{'name': 'wangwu', 'age': 30}])
```


## 七、FIND 查询

##### (1) find 查询所有

​	db.集合名.find([条件],{key1:1[,[key2:1]]}) #查询所有的数据   代表 显示哪些字段名

​	db.collection.find(query, {title: 1, by: 1}) // inclusion模式 指定返回的键，不返回其他键

​	db.collection.find(query, {title: 0, by: 0}) // exclusion模式 指定不返回的键,返回其他键

**注意：**

两种模式不可混用（因为这样的话无法推断其他键是否应返回）

```python
db.collection.find(query, {title: 1, by: 0}) // 错误
```

_id 键默认返回，需要主动指定 _id:0 才会隐藏

只能全1或全0，除了在inclusion模式时可以指定_id为0

```python
db.collection.find(query, {_id:0, title: 1, by: 1}) // 正确
```

实例

```
db.user.find({}, {'name': 0})
db.user.find({'age': 18}, {'name': 1})  # 只返回那么字段
db.user.find({'age': 18}, {'name': 0})  # 不返回name字段
```

##### (2) findOne()  查询一条

​	db.集合名.findOne([条件],{key1:1[,[key2:1]]}) #查询一条数据  代表 显示哪些字段名

```
db.user.findOne({}, {name:1})
```

##### (3) count 统计数据条数

​	db.集合名.find([条件]).count()

```
db.user.find({}).count()
```

##### (4) pretty()  展开来查看

​	db.集合名.find([条件]).pretty()

```
db.user.find({}).pretty()
```

##### (5) 查询条件的操作符

| 符号                                       | 符号说明     | 实例                                       | 说明                                      |
| :--------------------------------------- | :------- | ---------------------------------------- | --------------------------------------- |
| $gt                                      | 大于       | db.user.find({age:{$gt:18}})             | 年龄大于18 的                                |
| $gte                                     | 大于等于     | db.user.find({age:{$gte:18}})            | 年龄大于等于18的                               |
| $lt                                      | 小于       | db.user.find({age:{$lt:18}})             | 年龄小于18                                  |
| $lte                                     | 小于等于     | db.user.find({age:{$lte:18}})            | 年龄小于等于18                                |
| {key:value}                              | 等于       | db.user.find({age:18})                   | 年龄等于18                                  |
| { "_id" : ObjectId("5c2caba840b9441<br />054372217")} | 使用id查询   | db.user.find({ "_id" : ObjectId("5c2caba840b944<br />1054372217")}) | 查找id为"5c2caba840b94410<br />54372217"文档 |
| /值/                                      | 模糊查询     | db.user.find({username:/小/})             | 查询年龄中包含小字的文档                            |
| /^值/                                     | 以...作为开头 | db.user.find({username:/^小/})            | 查询username中以小字作为开头的文档                   |
| /值$/                                     | 以...作为结尾 | db.user.find({username:/小$/})            | 查询username中以小字作为结尾的文档                   |
| $in                                      | 在...内    | db.user.find({age:{$in:[18,20,30]})      | 查询年龄在18,20,30的文档                        |
| $nin                                     | 不在...内   | db.user.find({age:{$nin:[18,20,30]}})    | 查询年龄不在 1,20,30的文档                       |
| $ne                                      | 不等于 !=   | db.user.find({age:{$ne:18}})             | 查询年龄不为18的文档                             |

##### (6) AND 查询

```python
db.col.find({key1:value1, key2:value2})pretty()
```

db.集合名.find({条件一，条件二,,,})

例如：	

```
db.user.find({name:"张三",age:{$gt:10}}) #查询name为张三的 且 年龄 大于10岁的

db.user.find({name:"张三",age:10}) 		#查询name为张三的 且 年龄为10岁的
```



##### (7) OR  查询

db.集合名.find({$or:[{条件一},{条件二},,,]})

例如：

```
db.user.find({$or:[{name:"张三"},{name:"赵六"}]})   #查询name为张三 或者为赵六的所有数据
```

##### (8) AND 和 OR 的使用

db.集合名.find({条件一,,,$or:[{条件1},{条件2}]})

例如:

```
db.user.find({name:"张三",$or:[{age:10},{age:28}]})  #name为张三   年龄为10岁或者28岁的所有数据
```



##### (9) LIMIT  取值

db.集合名.find().limit(num)   #从第0个开始取几个

例如：

```
db.user.find().limit(5)   #从0开始取5条数据
```



##### (10)  skip 跳过几个

db.集合名.find().skip(num) #跳过几条数据

例如:

```
db.user.find().skip(2) #从第三条数据 取到最后
```



##### (11) limit  skip 配合使用

db.集合名.find().skip().limit(num) 

例如:

```
db.user.find().skip(2).limit(2)  #从第三个开始 取2个
```



##### (12) SORT 排序

在MongoDB中使用使用sort()方法对数据进行排序，sort()方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序排列，而-1是用于降序排列。

db.集合名.find().sort({key:1|-1})  #升序或者降序

例如:	

```
db.user.find().sort({age:1})  #查询所有数据 按照年龄 升序

db.user.find().sort({age:-1})  #查询所有数据 按照年龄 降序
```



## 八、UPDATE 文档的修改 

**结构：**

```python
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)u
```

- **query **: update的查询条件，类似sql update查询内where后面的。
- **update **: update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的

##### (1) 更新操作符  `$set直接修改   $inc累加修改`

+ db.集合名.update(条件,数据) 更改

  ```sql
  db.user.update({name:"张三"},{$inc:{age:5}}) #修改name为张三的文档  将age在原有的基础上 加5

  db.user.update({name:"张三"},{$set:{age:5}}) #修改name为张三的文档  将age的值 修改为5

  db.user.update({name:"张三"},{$set:{age:5}}) #将name为张三的文档 的年龄 修改为 5
  ```

+ 只更新第一条记录：

  ```sql
  db.col.update({"count" : {$gt:1}} , { $set : {"test2" : "OK"}});
  ```

+ 全部更新：

  ```sql
  db.col.update({"count" : {$gt: 3 }} , {$set : {"test2" : "OK"} }); 
  ```

+ 只添加第一条：

  ```sql
  db.col.update({ "count" : { $gt : 4 }} , {$set : {"test5" : "OK"} });
  ```

  ​

3.2版本以后**（建议使用）**

updateOne()  更新一条

```
db.user.updateOne({'name':'lisi'}, {$inc:{'age':5}})
```

updateMany(query,update) 更新多条 

```
db.user.updateMany({'name':'lisi'}, {$inc:{'age':5}})
```



## 九、REMOVE 文档的删除

**主体结构**

```python
db.collection.remove(
   <query>,
   {
     justOne: <boolean>,
     writeConcern: <document>
   }
)
```

##### (1)参数说明：

- **query **:（可选）删除的文档的条件。
- **justOne **: （可选）如果设为 true 或 1，则只删除一个文档。
- **writeConcern **:（可选）抛出异常的级别。

##### (2) 主体结构

**db.集合名.remove(条件)** #默认将所有都匹配到的数据进行删除

**db.集合名.remove(条件,1)** #只删除 第一个匹配到的数据

**db.集合名.remove(条件,,{justOne:true})** #只删除 第一个匹配到的数据

示例

```sql
b.user.remove({'age':{$gt: 30}})  # 删除年龄大于30的所有数据
b.user.remove({'age':{$gt: 30}}, 1)  # 删除年龄大于30的一条数据
db.col.remove({})  清空集合 "col" 的数据
```



##### (3) 3.2 版本后还有以下几种语法可用于删除文档:（建议）

remove() 方法已经过时了，现在官方推荐使用 

deleteOne() 删除一条

```sql
db.user.deleteOne({'age':{$gt: 0}})
```

deleteMany() 删除多条

```sql
db.user.deleteMany({'age':{$gt: 0}})
```



## 十、数据库删除与退出

##### (1) 数据库删除

1. 删除之前 最好use一下
2. db.dropDatabase()

##### (2) 数据库的退出

exit



## 十一、Python操作MongoDB

**安装**

pip install pymongo

### 1、导入 pymongo

`from pymongo import MongoClient`



### 2、连接服务器 端口号	27017

##### (1) 连接MongoDB

连接MongoDB我们需要使用PyMongo库里面的MongoClient，一般来说传入MongoDB的IP及端口即可，第一个参数为地址host，第二个参数为端口port，端口如果不传默认是27017。

##### (2) 代码

```python
conn = MongoClient("localhost")

MongoClient(host='127.0.0.1',port=27017)  # 如果端口改了那么就给端口，否则不用给
```



### 3、连接数据库

###### 		db = conn.数据库名称

##### 连接集合

###### 	collection = db.collection_name



###4、插入数据

##### (1) 在3.x以上 建议 使用

insert_one 插入一条数据 

insert_many() 插入多条数据

##### (2) 返回 id  使用insert_one()

data.inserted_id

data.inserted_ids



## 5、查询数据

##### (1) 查询一条

db.user.find_one()

##### (2) 带条件查询

db.user.find({"name":"张三"})

##### (3) 查询 id

**from **bson.objectid **import **ObjectId*#用于ID查询

data = db.user.find({**"_id"**:ObjectId(**"59a2d304b961661b209f8da1"**)})

```python
data = db.user.find({'_id': ObjectId('59f290b01683f9339214746d')}) #_id': ObjectId('59f290b01683f9339214746d')
```

##### (5) 模糊查询

+ {"name":{'$regex':"张"}}

+ {'xxx':re.compile('xxx')}  



## 6、sort limit skip

##### (1) sort		排序

年龄 大于10

```python
data = db.user.find({"age":{"$gt":10}}).sort("age",1) #年龄 升序 查询  pymongo.ASCENDING   --升序

data = db.user.find({"age":{"$gt":10}}).sort("age",-1) #年龄 降序 查询	pymongo.DESCENDING --降序
```

##### (2) limit		取值

##### **取三条数据**

```python
db.user.find().limit(3)
m= db.user.find({"age":{"$gt":10}}).sort("age",-1).limit(3)
```

##### (3) skip 		从第几条数据开始取

db.user.find().skip(2)

### 7、update 修改

update()方法其实也是官方不推荐使用的方法，在这里也分了**update_one()**方法和**update_many()**方法，用法更加严格，

##### (1) update_one() 第一条符合条件的数据进行更新

db.user.update_one({"name":"张三"},{"$set":{"age":99}})

##### (2) update_many() 将所有符合条件的数据都更新

db.user.update_many({**"name"**:**"张三"**},{**"$set"**:{**"age"**:91}})

**(3)** 其返回结果是UpdateResult类型，然后调用**matched_count**和**modified_count**属性分别可以获得匹配的数据条数和影响的数据条数。

+ result.matched_count
+ result.modified_count



### 8、remove 删除

删除操作比较简单，直接调用remove()方法指定删除的条件即可，符合条件的所有数据均会被删除，

##### (1) 删除一条

delete_one()即删除第一条符合条件的数据

collection.delete_one({“name”:“ Kevin”})

##### (2) 删除多条

delete_many()即删除所有符合条件的数据，返回结果是DeleteResult类型

collection.delete_many({“age”: {$lt:25}})

##### (4) 可以调用deleted_count属性获取删除的数据条数。

result.deleted_count

### 9、关闭连接

conn.close()