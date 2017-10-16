# Date 和 Time 处理有它一套专门的函数 两个值比较通常用两个表
import pymysql
db = pymysql.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """
SELECT W2.Id FROM Weather AS W1,Weather AS W2
WHERE W1.Date = DATE_SUB(W2.Date,INTERVAL 1 DAY) AND W1.Temperature < W2.Temperature
"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()