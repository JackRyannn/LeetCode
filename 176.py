import pymysql
db = pymysql.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """# Write your MySQL query statement below
SELECT  MAX(Salary) AS SecondHighestSalary FROM Employee
         WHERE Salary < (SELECT MAX(Salary) FROM Employee)
         ORDER BY Salary DESC
"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()