import pymysql
db = pymysql.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """
SELECT Name AS Customers FROM Customers
WHERE Customers.Id NOT IN (SELECT CustomerId FROM Orders)
"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()