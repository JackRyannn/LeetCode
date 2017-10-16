# 先把score按递减顺序排列，然后新建一列Rank，采用count计数算出不重复Distinct的比该值大的数的个数，即为其rank值。
import pymysql
db = pymysql.connect("localhost", "root", "135213521352", "PythonDB")

cursor = db.cursor()

sql = """
SELECT Score ,(SELECT count(distinct Score) FROM Scores WHERE Score >= s.Score) AS Rank FROM Scores AS s
ORDER BY Score DESC
"""
try:
   cursor.execute(sql)
   r = cursor.fetchall()

   db.commit()
   print r
except:
   db.rollback()


db.close()