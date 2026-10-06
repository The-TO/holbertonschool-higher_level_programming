#!/usr/bin/python3
"""Script to list specific states from database"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "JOIN states ON states.id = cities.state_id "
                "ORDER BY cities.id")
    rows = cur.fetchall()
    for n in rows:
        print(n)

    cur.close()
    db.close()
