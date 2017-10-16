# LeftJOIN 的含义是返回左边表所有满足条件的行，无论右边表是否符合
import pymysql
db = pymysql.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """SELECT Person.FirstName, Person.LastName, Address.City, Address.State from Person LEFT JOIN Address on Person.PersonId = Address.PersonId;
"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()