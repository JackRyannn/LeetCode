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