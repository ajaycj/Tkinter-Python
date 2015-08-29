#! usr/bin/python


import MySQLdb
db = MySQLdb.connect("localhost", "root", "ajay.cj", "SAMPLE")

cursor = db.cursor()

cursor.execute("SELECT * from SAMPLE")

data = cursor.fetchone()

print data

db.close()
