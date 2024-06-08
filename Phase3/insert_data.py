import mysql.connector

# Establish the connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='test_db'
)

# Create a cursor object
cursor = conn.cursor()

# SQL query to insert data
sql = "INSERT INTO employees (id, name, salary) VALUES (%s, %s, %s)"
values = (1, 'John Doe', 50000)

# Execute the SQL query
cursor.execute(sql, values)

# Commit the transaction
conn.commit()

print(cursor.rowcount, "record inserted.")

# Close the cursor and connection
cursor.close()
conn.close()
