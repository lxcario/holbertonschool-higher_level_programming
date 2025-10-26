#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.

This script takes three command-line arguments:
1. MySQL username
2. MySQL password
3. Database name

It connects to a MySQL server running on localhost at port 3306.
Results are displayed as tuples and sorted in ascending order by states.id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    
    # Retrieve arguments: username, password, database name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = None
    cur = None

    try:
        # Establish a connection to the database
        db = MySQLdb.connect(
            host="localhost",
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            port=3306
        )

        # Create a cursor object to execute SQL queries
        cur = db.cursor()

        # Execute the query to select all states, sorted by id
        # Explicitly selecting 'id' and 'name' to satisfy strict output requirements
        query = "SELECT id, name FROM states ORDER BY id ASC"
        cur.execute(query)

        # Fetch all the results
        rows = cur.fetchall()

        # Print each row exactly as a tuple
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        # General error handling for connection or query failure
        # print(f"An error occurred: {e}", file=sys.stderr)
        pass
    finally:
        # Ensure resources are closed gracefully, even if an exception occurred.
        if cur is not None:
            cur.close()
        if db is not None:
            db.close()

