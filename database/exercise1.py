import psycopg2

def get_connection():
    connection = psycopg2.connect(user="postgres",
                                  password="shailesh@123",
                                  host="localhost",
                                  port="5566",
                                  database="python_db")
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("You are connected to PostgreSQL version: ", db_version)
        close_connection(connection)
    except (Exception, psycopg2.Error) as error:
        print("Error while getting data", error)


read_database_version()