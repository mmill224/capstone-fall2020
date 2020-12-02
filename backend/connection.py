import mysql.connector

def fpdatabase():
    try:
        results = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "coffeecup90",
        database = "fpdatabase",)
        return results
    except:
        print("Something went wrong with connecting to the database. \n Try checking if the SQL server is running, and check if you have the correct password in backend/connection.py")
