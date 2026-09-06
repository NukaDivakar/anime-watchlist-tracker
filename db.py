from pymysql import connect

# This function just opens a connection to our anime_tracker database.
# Every other file will call this whenever it needs to talk to MySQL.

def get_connection():
    connection = connect(
    host="localhost",
    user="root",
    password="12345",
    database="anime_tracker"
    )
    return connection
