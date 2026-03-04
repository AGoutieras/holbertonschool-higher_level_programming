#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of that state
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name "
                   "FROM cities "
                   "JOIN states "
                   "ON cities.state_id = states.id "
                   "WHERE states.name = %s "
                   "ORDER BY cities.id ", (sys.argv[4],))

    [print(state) for state in cursor.fetchall()]
