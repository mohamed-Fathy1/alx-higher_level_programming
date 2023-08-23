#!/usr/bin/python3
from sys import argv
import MySQLdb


usr = argv[1]
password = argv[2]
database = argv[3]

try:
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=usr, passwd=password,
                         db=database, charset="utf8")
    cur = db.cursor()
    cur.execute('''SELECT * FROM states''')
    for row in cur._rows:
        print(row)
except (MySQLdb.Error, Exception) as e:
    print(e)
