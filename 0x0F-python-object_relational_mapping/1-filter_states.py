#!/usr/bin/python3
import MySQLdb
from sys import argv

'''
Get states by input
'''
db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
cursor = db.cursor()

cursor.execute("SELECT * FROM states WHERE states.name LIKE 'N%';")
rows = cursor.fetchall()
for r in rows:
    print(r)


db.close()