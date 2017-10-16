import pymysql
db = pymysql.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """SELECT E1.Name AS Employee FROM Employee AS E1,Employee AS E2
WHERE E1.Salary > E2.Salary and E1.ManagerId = E2.Id
"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()