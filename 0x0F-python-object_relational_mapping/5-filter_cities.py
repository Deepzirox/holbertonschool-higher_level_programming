#!/usr/bin/python3

'''
filter cities by user input
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
    SELECT name
    FROM cities 
    WHERE state_id = (SELECT id FROM states WHERE name = '{}')
    '''.format(argv[4])

    cursor.execute(query)

    rows = cursor.fetchall()
    res = ", ".join(list(map(lambda x: x[0], rows)))
    print(res)
    db.close()
