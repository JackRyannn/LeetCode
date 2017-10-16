# DISTINCT 可以去掉重复值
import pymysql
db = pymysql.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """
SELECT DISTINCT P1.Email FROM Person AS P1,Person AS P2
WHERE P1.Id < P2.Id AND P1.Email = P2.Email
"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()