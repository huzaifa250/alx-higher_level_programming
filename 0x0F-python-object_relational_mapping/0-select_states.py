# !/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], port=3306)

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    m_res = cur.fetchall()

    for state in m_res:
        print(state)

    cur.close()
    conn.close()
