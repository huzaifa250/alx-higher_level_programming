# !/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="root",
        port=3306,
        db="hbtn_0e_0_usa"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC;")
    my_res = cursor.fetchall()
    for state in my_res:
        print(state)
    cursor.close()
    conn.close()
