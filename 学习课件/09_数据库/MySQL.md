# MySQL数据库

## 一、MySQL数据库的介绍

### 1、发展史

1996年，MySQL 1.0

2008年1月16号 Sun公司收购MySQL。

2009年4月20，Oracle收购Sun公司。

[MySQL](https://baike.baidu.com/item/MySQL/471251)是一种[开放源代码](https://baike.baidu.com/item/%E5%BC%80%E6%94%BE%E6%BA%90%E4%BB%A3%E7%A0%81)的关系型[数据库管理](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E5%BA%93%E7%AE%A1%E7%90%86)系统（RDBMS），使用最常用的数据库管理语言--[结构化查询语言](https://baike.baidu.com/item/%E7%BB%93%E6%9E%84%E5%8C%96%E6%9F%A5%E8%AF%A2%E8%AF%AD%E8%A8%80)（SQL）进行数据库管理。

MySQL是开放源代码的，因此任何人都可以在General Public License的许可下下载并根据个性化的需要对其进行修改。

MySQL因为其速度、可靠性和适应性而备受关注。大多数人都认为在不需要[事务](https://baike.baidu.com/item/%E4%BA%8B%E5%8A%A1)化处理的情况下，MySQL是管理内容最好的选择。

### 2、MySQL简介

MySQL是一个[关系型数据库管理系统](https://baike.baidu.com/item/%E5%85%B3%E7%B3%BB%E5%9E%8B%E6%95%B0%E6%8D%AE%E5%BA%93%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/696511)，由瑞典MySQLAB 公司开发，目前属于 [Oracle](https://baike.baidu.com/item/Oracle) 旗下产品。MySQL是最流行的[关系型数据库管理系统](https://baike.baidu.com/item/%E5%85%B3%E7%B3%BB%E5%9E%8B%E6%95%B0%E6%8D%AE%E5%BA%93%E7%AE%A1%E7%90%86%E7%B3%BB%E7%BB%9F/696511)之一，在WEB 应用方面，MySQL是最好的 [RDBMS](https://baike.baidu.com/item/RDBMS/1048260) (RelationalDatabase Management System，关系数据库管理系统)应用软件MySQL所使用的SQL 语言是用于访问[数据库](https://baike.baidu.com/item/%E6%95%B0%E6%8D%AE%E5%BA%93/103728)的最常用标准化语言。MySQL软件采用了双授权政策，分为社区版和商业版，由于其体积小、速度快、总体拥有成本低，尤其是[开放源码](https://baike.baidu.com/item/%E5%BC%80%E6%94%BE%E6%BA%90%E7%A0%81/7176422)这一特点，一般中小型网站的开发都选择MySQL 作为网站数据库

### 3、社区版本和企业版本的区别

主要的区别有以下两点。

1. 企业版只包含稳定之后的功能，社区版包含所有Mysql的最新功能。

也就是说，社区版是企业版的测试版，但是，前者的功能要比后者多。

2. 官方的支持服务只针对企业版，用户在使用社区版时出现任何问题，Mysql官方概不负责。

MySQL如何下载

进入MySQL官网（https://www.mysql.com）
查看底部下载-https://dev.mysql.com/downloads/mysql/



## 二、数据库的分类

关系型与非关系型数据库

### 1、关系型数据库的优势：

1. 复杂查询

   可以用SQL语句方便的在一个表以及多个表之间做非常复杂的数据查询

2. 事物支持

   使得对于安全性能很高的数据访问要求得以实现

### 2、非关系型数据库的优势：

1. 性能

   NOSQL是基于键值对的 可以想象成表中的主键和值的对应关系 不需要经过SQL层的解析 所以性能很高

2. 可扩展性

   同样也是也因为基于键值对 数据之间没有偶尔性 所以非常容易水平扩展



## 三、安装与Navicat使用

### 1、MySQL安装

先去mysql官网下载好安装包. (https://dev.mysql.com/downloads/)

![image-20210710114626664](MySQL数据库.assets/image-20210710114626664.png)



![image-20210710114553371](MySQL数据库.assets/image-20210710114553371.png)

![image-20210710114707734](MySQL数据库.assets/image-20210710114707734.png)

![image-20210710114815804](MySQL数据库.assets/image-20210710114815804.png)

![image-20210710114930711](MySQL数据库.assets/image-20210710114930711.png)

![image-20210710115027365](MySQL数据库.assets/image-20210710115027365.png)

![image-20210710115102924](MySQL数据库.assets/image-20210710115102924.png)

![image-20210710115119749](MySQL数据库.assets/image-20210710115119749.png)



接下来是MySQL的图形化界面工具.  推荐用Navicat. 好多年了, 很好用. 安装的时候一路确定. 



### 2、Navicat使用

![image-20210710144159210](MySQL数据库.assets/image-20210710144159210.png)

![image-20210710144409473](MySQL数据库.assets/image-20210710144409473.png)

![image-20210710144519309](MySQL数据库.assets/image-20210710144519309.png)

![image-20210710144744253](MySQL数据库.assets/image-20210710144744253.png)

哦了, 至此, Navicat可以操纵你的数据库了. 

## 四、进入到MySQL数据库

### 1、简单模式

C:\Users\xlg>mysql -uroot -p
Enter password: `******`

### 2、标准模式

 C:\Users\xlg>mysql -h127.0.0.1 -uroot -p

mysql -hlocalhost -uroot -p

### 3、参数所代表的含义：

h:host 主机（localhost IPV4 127.0.0.1）

u:root 用户

p:password 密码



## 五、对于MySQL数据库的操作

### 1、对于库与表进行操作

+ 查看所有的数据库

  show databases;

+ 选择数据库

  use 库名

+ 查看当前库下有哪些表

  show tables;

+ 查看当前所在库

  select database();

+ 创建数据库

  create database 库名;

+ 查看创建库信息

  show create database 库名;

+ 删除库/表
  drop database 库名;

  drop table 表名;

+ 查看表结构

  desc 表名;

+ 查看创建表语句

  show create table lucky;

+ 撤销当前命令

  \c

+ 数据库的退出

  + \q
  + exit
  + quit

### 2、注意

1. MySQL命令以英文的分号作为结束
2. SQL命令不区分大小写
3. 在进入到一个数据库中在进入到另外一个的时候 不需要退出数据库 而是使用use再次进行数据库的切换
4. windows下表名库名不区分大小写 Linux下严格区分
5. MySQL数据库的名称具有唯一性 每个库中的表的名称也具有唯一性(库名或者一个库中的表名不要出现相同的名称)
6. 当在输入命令的时候输入完以后 添加分号不能执行命令 那么查看一下左侧是否存在引号没有闭合的情况



## 六. 表的操作

### 1、表的概念

在所有关系型数据库中, 所有的数据都是以表格的形式进行存储的. 那表格应该如何进行设计呢? 其实这里蕴含了一个映射关系的. 

比如, 我们想要存学生信息. 那我们先思考. 在你未来的规划中, 一个学生应该会有哪些数据存在? 

学生: 学号(唯一标识), 姓名, 生日, 家庭住址, 电话号等信息. OK. 我们抛开数据库不谈. 想要存储这些数据, 表格创建起来的话应该是是这样的:

![image-20210712100401960](MySQL数据库.assets/image-20210712100401960.png)

OK. 按照这个规则来看. 每一条数据对应的就是一个人的信息. 

### 2、创建表

创建表有两种方案: 

1. 用SQL语句创建表格

   ```sql
   create table student(
   		sno int(10) primary key auto_increment,
       sname varchar(50) not null, 
       sbirthday date not null,
       saddress varchar(255),
       sphone varchar(12),
       class_name varchar(50)
   )
   ```

   数据类型:

   ​	int 整数

   ​	double小数 

   ​	varchar  字符串

   ​	date  时间(年月日)

   ​	datetime 时间(年月日时分秒)

   ​	text 大文本

   ​	

   约束条件:

   ​	primary key 主键, 全表唯一值. 就像学号. 身份证号. 能够唯一的确定一条数据

   ​	auto_increment 主键自增.

   ​	not null  不可以为空.

   ​	null  可以为空

   ​	default 设置默认值

   ​		

2. 用Navicat图形化工具来创建

   ![image-20210712110029287](MySQL数据库.assets/image-20210712110029287.png)

   ![image-20210712164027033](MySQL数据库.assets/image-20210712164027033.png)

   ![image-20210712110221729](MySQL数据库.assets/image-20210712110221729.png)




## 七、MySQL表的创建

字段类型

###  1、数值类型

|     类型      |  大小  |          范围(有符号)          |    范围(无符号)     |   用途   |
| :---------: | :--: | :-----------------------: | :------------: | :----: |
| **tinyint** | 1字节  |        （-128,127）         |    （0,255）     |  小整数值  |
|   **int**   | 4字节  | （-2147483648, 2147483647) | (0,4294967295) |  大整数值  |
|    float    | 4字节  |                           |                | 单精度浮点型 |
|   double    | 8字节  |                           |                | 双精度浮点型 |

 **创建表语句**

```mysql
mysql> create table testnum(
    -> ttinyint tinyint,
    -> tint int,
    -> tfloat float(6,2),
    -> tdouble double(6,2),
    -> );
```

**创建表的主体结构：**

> create table if not exists 表名(
>
> 字段名称 字段类型 约束条件 字段说明,
>
> 字段名称 字段类型 约束条件 字段说明,
>
> ...
>
> )

**表插入数据语句**

**指定字段名称插入值**

insert into 表名(字段1,字段2...) values(值1,值2...)

**不指定字段插入之**

insert into 表名 values(值1,值2...)

### 2、字符串类型

|     类型      |       大小       |   用途   |
| :---------: | :------------: | :----: |
|  **char**   |    0-255字节     | 定长字符串  |
| **varchar** |    0-255字节     | 变长字符串  |
|  **text**   |   0-65535字节    | 长文本数据  |
|  longtext   | 0-4294697295字节 | 极大文本数据 |

**字符串类型注意事项：**

1) char和varchar的区别

+ char执行效率高于varchar （但占用空间大）
+ varchar相对于char节省空间
+ char和varchar 类型的长度范围都在0-255之间
+ varchar类型传入的值小于给定的长度 不会使用空格填充


```
CREATE TABLE `test2` (
  `tchar` char(10) DEFAULT NULL,
  `tvarchar` varchar(20) DEFAULT NULL,
  `ttext` text,
  `tlongtext` longtext
) 
```




## 七、INSERT 数据的添加

1. 指定字段添加值

   insert into 表名(字段1,字段2....) values(值1,值2...)

   insert into user(sex,username) values(0,'lucky');

2. 不指定字段添加值

   insert into 表名 values(值1,值2...)

   insert into user values(null,0,'lucky','我是lucky老师');

3. 指定字段添加多个值

   insert into 表名(字段1,字段2....) values(值1,值2...),(值1,值2...)...

   insert into user(sex,username) values(1,'苍苍'),(0,'蒹葭');

4. 不指定字段添加多个值

   insert into 表名 values(值1,值2...),(值1,值2...)...

    insert into user values(null,1,'xxx','xxx'),(null,0,'xxl','xxl');

**注意事项：**
指定字段与不指定字段在添加值的时候 按照从左至右依次对应给值



## 八、SELECT查询

1. 不指定字段的查询（不建议）

   select * from 表名

2. 指定字段的数据查询(建议)

   select 字段名1,字段名2... from  表名

   select  username,userinfo from user;

3. 对查询的字段起别名

   select username as u from user;

   select username  u from user;




## 九、UPDATE修改

1. 修改一个字段的值

   update 表名 set 字段名=值;

   update user set username='帅气的lucky' where id = 3;

2. 修改多个字段的值

   update 表名 set 字段名1=值1,字段名2=值2...;

   update user set sex=0,userinfo='xxx的个人简介' where id=7;

3. 给字段的值在原有的基础上改变值

   update user set sex=sex+2;

**注意：**

在进行数据的修改的时候 一定记得给定where条件  如果没有给定where条件 则修改的为整张表当前字段的值



## 十、DELETE 删除

**主体结构：**

```mysql
delete from 表名 [where ...]
```

**实例：**

delete from user; 删除user表中所有的数据 

**注意：**

删除 一定注意添加 where 条件   否则会删除整张表中的数据  并且auto_increment自增所记录的值不会改变  所以需要将自增归位

truncate 表名; 清空表数据 




## 十一、WHERE条件

**实例表结构：**

+----------+-------------+------+-----+-----------------------+----------------+
| Field    | Type        | Null | Key | Default               | Extra          |
+----------+-------------+------+-----+-----------------------+----------------+
| id       | int(11)     | NO   | PRI | NULL                  | auto_increment |
| sex      | tinyint(4)  | NO   |     | 1                     |                |
| username | varchar(20) | YES  |     | NULL                  |                |
| age      | tinyint(4)  | NO   |     | 18                    |                |
| userinfo | varchar(50) | NO   |     | 我是帅气的lucky老师啊 |                |
+----------+-------------+------+-----+-----------------------+----------------+

#### (1) 比较运算符

1. `>`

   将id大于5 的性别 更改为0 年龄改为20岁

   update user set sex=0,age=20 where id>5;

2. `<`

   将id小于3 的性别 更改为0 年龄改为23岁

   update user set sex=0,age=23 where id<3;

   查看id小于4的 性别和用户名的字段数据

   select sex,username from user where id<4;

3. `>=`

   删除 id大于等于6的数据

   delete from user where id>=6;

4. `<=`

   查询年龄小于等于23的数据

   select * from user where age<=23;

5. =

   查询性别为0的数据

   select * from user where sex=0;

6. `!=/<>`

   查询 用户名不等于lucky的所有数据

   select * from user where username!='lucky';

   select * from user where username<>'lucky';

#### (2) 逻辑运算符

1. and 逻辑与 俩侧为真结果为真

   查询年龄在18到23之间 不包括本身

   select * from user where age>18 and age<23;

   修改年龄为30 id大于1 小于等于2

   update user set age=30 where id>1 and id<=2;

2. or 逻辑或运算 俩侧条件满足一侧就可以

   select * from user where age=10 or age=30;

   select * from user where age>=10 or age<=30;



#### (3) order by 排序  升序/降序

   升序

   查询数据 按照年龄升序（默认）

   select * from user order by age;

   select * from user order by age asc;

   查询数据 按照年龄降序

   select * from user order by age desc;

#### (4) limit 取值

**结构：**

limit x 取出x条数据

limit x,y 从x的位置取出y条数据

取出3条数据

 select * from user limit 3;

取出年龄最大/最小的一条数据

select * from user order by age desc limit 1;

select * from user order by age limit 1;

#### (6) like 模糊查询

1. ’%字符‘ 查询以字符结尾的数据

   查询以三字为结束的username的数据

   select * from user where username like '%三';

2. '字符%' 查询以字符开头的数据

   select * from user where username like '赵%';

3. '%字符%' 查询包含字符的数据

   查询 userinfo中包含lucky的数据

   select * from user where userinfo like '%lucky%';



## 十二、 聚合函数

1. count 统计个数
2. max 最大值
3. min 最小值
4. Sum 求和
5. avg 求平均数

select count(*) as count,max(age),min(age),avg(age),sum(age) from user;



## 十三、 数据库的导入导出

+ 导入

  mysql -uroot -p 库名<demo.sql  

+ 导出

  mysqldump -uroot -p 库名>demo.sql



## 十四、Python操作MySQL

**安装：**

pip install pymysql

**使用：**
import pymysql

#### (1) 链接MySQL数据库

db = pymysql.connect(主机名,用户名,密码,数据库名)

```
db = pymysql.connect(host='localhost', user='root', password='123456', database='test')
```

#### (2) 设置字符集

db.set_charset('utf8')

#### (3) 创建游标对象

cursor = db.cursor()

#### (4) 执行SQL语句

cursor.execute(sql语句)

#### (5) 获取结果集

获取所有

cursor.fetchall()

获取一条

cursor.fetchone()

#### (6) 获取受影响的行数

cursor.rowcount

#### (7) **事物**

pymysql默认开启了事物处理 所以在添加数据的时候 需要commit 或者rollback

**实例：**

```python
try:
    sql = 'insert into user values(null,1,"曹操",100,"曹操第一奸雄","魏国")'
    print(sql)
    cursor.execute(sql)
    db.commit()
except:
   db.rollback()
```

对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。 

commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。

#### (8) 关闭数据库连接

db.close()

#### (9) 拼凑正常完整的sql语句

```python
print("select name,password from user where name=\""+username+"\"")
print("select name,password from user where name='"+username+"'")
print("select name,password from user where name='%s'"%(username))
print("select name,password from user where name='{}'".format(username))
print(f"select name,password from user where name='{username}'")
```



