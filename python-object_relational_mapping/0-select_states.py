#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.

It takes 3 arguments: mysql username, mysql password, and database name.
It connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id.
It uses the 'MySQLdb' module.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Ensure correct number of arguments are provided (4 including script name)
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> \
              <mysql_password> <database_name>")
        sys.exit(1)

    # Retrieve arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Database connection parameters
    host = "localhost"
    port = 3306

    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host=host,
            port=port,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
        )

        # Create a cursor object
        cur = db.cursor()

        # SQL query to select all states and sort by id
        query = "SELECT * FROM states ORDER BY id ASC"

        # Execute the query
        cur.execute(query)

        # Fetch all the rows
        rows = cur.fetchall()

        # Print the results
        for row in rows:
            print(row)

        # Close the cursor and connection
        cur.close()
        db.close()

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
        sys.exit(1)
