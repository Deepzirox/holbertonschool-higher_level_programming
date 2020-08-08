#!/usr/bin/python3
import MySQLdb
from sys import argv

# connection
db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
cursor = db.cursor()
query = "SELECT * FROM states WHERE name = '{}';".format(argv[4])
cursor.execute(query)
res = cursor.fetchall()
for r in res:
    print(r)
db.close()
