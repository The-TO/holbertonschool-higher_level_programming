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
    query = ("SELECT cities.name "
            "FROM cities "
            "JOIN states ON states.id = cities.state_id "
            "WHERE BINARY states.name = %s "
            "ORDER BY cities.id")
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    sortie = []
    for n in rows:
        sortie.append(n[0])
    print(", ".join(sortie))

    cur.close()
    db.close()
