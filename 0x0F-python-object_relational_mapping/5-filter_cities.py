#!/usr/bin/python3
'''
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
'''
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute('''SELECT cities.name
                FROM cities JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id''', (argv[4], ))
    arr = []
    for row in cur.fetchall():
        arr.append(*row)
    print(*arr, sep=', ')
    cur.close()
    db.close()
