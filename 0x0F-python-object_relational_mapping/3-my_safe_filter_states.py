#!/usr/bin/python3

'''
Get states by input
'''

import MySQLdb
from sys import argv

if __name__ == '__main__':
    p = 3306
    h = "localhost"
    db = MySQLdb.connect
    db = db(host=h, port=p, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE '%{}%';".format(argv[4])
    cursor.execute(query)
    res = cursor.fetchall()
    for r in res:
        print(r)
    db.close()
