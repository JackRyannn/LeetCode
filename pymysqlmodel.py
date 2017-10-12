import pymysqlmodel

db = pymysqlmodel.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """SELECT * FROM MOVIES
            WHERE id%2 = 1
            AND description != 'boring'
            ORDER BY  rating DESC
"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()