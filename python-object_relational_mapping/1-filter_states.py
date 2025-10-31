#!/usr/bin/python3
"""Module for Selecting states starting with N"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id')

    for state in cursor.fetchall():
        if state[1][0] == 'N':
            print(state)

    if cursor:
        cursor.close()
    if db:
        db.close()
