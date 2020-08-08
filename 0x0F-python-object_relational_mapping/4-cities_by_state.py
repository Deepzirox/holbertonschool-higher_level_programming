#!/usr/bin/python3

'''
Get cities by states rows
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    p = 3306
    h = "localhost"
    db = MySQLdb.connect
    db = db(host=h, port=p, user=argv[1], passwd=argv[2], db=argv[3])
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
