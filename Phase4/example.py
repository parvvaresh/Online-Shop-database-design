import mysql.connector
from mysql.connector import Error

def connect_to_database(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def add_data(connection, table_name, data):
    cursor = connection.cursor()
    placeholders = ", ".join(["%s"] * len(data))
    columns = ", ".join(data.keys())
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    try:
        cursor.execute(sql, list(data.values()))
        connection.commit()
        print("Data added successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def delete_data(connection, table_name, condition):
    cursor = connection.cursor()
    sql = f"DELETE FROM {table_name} WHERE {condition}"
    try:
        cursor.execute(sql)
        connection.commit()
        print("Data deleted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

if __name__ == "__main__":
    connection = connect_to_database("localhost", "your_username", "your_password", "your_database")
    
    # Add data example
    data_to_add = {
        "column1": "value1",
        "column2": "value2",
        "column3": "value3"
    }
    add_data(connection, "your_table", data_to_add)
    
    # Delete data example
    condition_to_delete = "column1 = 'value1'"
    delete_data(connection, "your_table", condition_to_delete)
    
    if connection:
        connection.close()
        print("Connection closed")
