#!/usr/bin/python3
""" Lists all states name starting with N """


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY id ASC""")
    my_res = cur.fetchall()
    for state in my_res:
        print(state)
    cur.close()
    db.close()
