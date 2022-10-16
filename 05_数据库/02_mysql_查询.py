import pymysql

db = pymysql.connect(user='root', password='182182aA', host='localhost', port=3306, charset='utf8', database='test1')
cursor = db.cursor()

sql = 'select 内容 from 励志文章 where ID=42'
cursor.execute(sql)
data = cursor.fetchall()
for i in data:
    for j in i:
        print(j)

cursor.close()
db.close()
