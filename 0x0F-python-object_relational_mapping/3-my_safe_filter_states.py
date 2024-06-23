#!/usr/bin/python3
""" script for task 3 """

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                (sys.argv[4],))
    m_res = cur.fetchall()
    for state in m_res:
        print(state)
    cur.close()
    db.close()
