# 三个连续，构建三个表，分别和上下两行比较，相等则三连续
import pymysql
db = pymysql.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """
SELECT DISTINCT L2.Num AS ConsecutiveNums FROM Logs L1,Logs L2,Logs L3
WHERE L1.id+1 = L2.id AND L2.id = L3.id-1 AND L1.Num = L2.Num AND L2.Num =  L3.Num

"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()