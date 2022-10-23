import pymysql
from pymysql.cursors import DictCursor
from pprint import pprint

db = pymysql.connect(user='ahui', password='182182aA', host='43.138.31.29', port=3306, charset='utf8', database='my_test')
cursor = db.cursor(DictCursor)

sql = 'select 作者,标题,时间,阅读数 from 励志文章 where ID>=3 and ID<=5'
cursor.execute(sql)
data = cursor.fetchall()
pprint(data)

cursor.close()
db.close()
