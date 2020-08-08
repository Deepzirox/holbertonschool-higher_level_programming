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

    cursor.execute("SELECT * FROM states WHERE states.name LIKE 'N%';")
    rows = cursor.fetchall()
    for r in rows:
        print(r)
    db.close()