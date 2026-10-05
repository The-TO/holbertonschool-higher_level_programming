#!/usr/bin/python3
"""Script to list speicifc states from database"""

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
    cur.execute("SELECT id, name FROM states WHERE LIKE BINARY 'N%' ORDER BY id")
    rows = cur.fetchall()
    for n in rows:
        print(n)

    cur.close()
    db.close()
