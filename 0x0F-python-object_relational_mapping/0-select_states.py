#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
from sys import argv
import MySQLdb


usr = argv[1]
password = argv[2]
database = argv[3]

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=usr, passwd=password,
                         db=database, charset="utf8")
    cur = db.cursor()
    cur.execute('''SELECT * FROM states ORDER BY id ASC''')
    for row in cur._rows:
        print(row)
    cur.close()
    db.close()
