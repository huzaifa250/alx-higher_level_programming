# !/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]

    conn = MySQLdb.connect(
            host='localhost',
            user=user,
            passwd=pwd,
            port=3306,
            db=database
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    my_res = cursor.fetchall()
    for state in my_res:
        print(state)
    cursor.close()
    conn.close()
