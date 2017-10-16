# 删除某一行，可以空缺，也可以写上删除某一个表
import pymysql
db = pymysql.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """# Write your MySQL query statement below
DELETE P1 FROM Person AS P1,Person AS P2
WHERE P1.Email = P2.Email AND P1.Id > P2.Id
"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()