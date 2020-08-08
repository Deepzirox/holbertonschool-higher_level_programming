#!/usr/bin/python3
import MySQLdb
from sys import argv

'''
Get cities by states rows
'''

db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
cursor = db.cursor()
query = '''
SELECT cities.id, cities.name, states.name 
FROM cities, states 
WHERE cities.state_id=states.id 
ORDER BY cities.id;
'''
cursor.execute(query)
res = cursor.fetchall()
for r in res:
    print(r)
db.close()
