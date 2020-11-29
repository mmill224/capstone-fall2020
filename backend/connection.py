import mysql.connector

def fpdatabase():
    return mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "coffeecup90",
    database = "fpdatabase",
)
