#!/usr/bin/python3
import MySQLdb
from sys import argv

# connection
db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
cursor = db.cursor()

query = '''
SELECT name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = '{}')
'''.format(argv[4])

cursor.execute(query)

rows = cursor.fetchall()
res = ", ".join(list(map(lambda x: x[0], rows)))
print(res)
db.close()
