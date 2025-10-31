#!/usr/bin/python3
"""
Module for Selecting states where name equals argument
"""
import sys
import MySQLdb

if __name__ == '__main__':
    # Ensure all 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> \
              <password> <database> <state_name>")
        sys.exit(1)

    db = None
    cursor = None
    try:
        # Arguments: argv[1]=user, argv[2]=password, argv[3]=database
        db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3],
            host="localhost",
            port=3306
        )
        cursor = db.cursor()

        # The state name to search is argv[4]
        state_name_search = sys.argv[4]

        # Use %s placeholder for secure SQL injection prevention
        query = ("SELECT * FROM states "
                 "WHERE BINARY name = %s "
                 "ORDER BY id ASC").format(state_name_search)

        # Execute the query, passing the search term as a tuple
        cursor.execute(query, (state_name_search,))

        # Indentation for the loop is fixed to align with the rest of the block
        for state in cursor.fetchall():
            print(state)

    except MySQLdb.Error as e:
        print(f"Database error: {e}")
        sys.exit(1)
    finally:
        # Close resources safely
        if cursor:
            cursor.close()
        if db:
            db.close()
