#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa """

import sys
import MySQLdb

username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

if __name__ == "__main__":
    db = MySQLdb.connect(user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for state in rows:
        print(state)
