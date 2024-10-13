import oracledb

# Connect to Oracle Database
connection = oracledb.connect(user="your_username", password="your_password", dsn="your_dsn")

# Create a cursor
cursor = connection.cursor()

# Execute SQL to get Oracle version
cursor.execute("SELECT * FROM v$version")

# Fetch and print the version details
for row in cursor:
    print(row[0])

# Close cursor and connection
cursor.close()
connection.close()
