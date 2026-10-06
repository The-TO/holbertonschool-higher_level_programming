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
    state_name = sys.argv[4]
    cur = db.cursor()
    query = ("SELECT id, name FROM states "
             "WHERE BINARY name ='{}' ORDER BY id").format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for n in rows:
        print(n)

    cur.close()
    db.close()
