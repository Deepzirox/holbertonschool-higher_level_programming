#!/usr/bin/python3

"""
    Get all rows from states
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states;")
    row = cursor.fetchall()
    for r in row:
        print(r)

    db.close()
