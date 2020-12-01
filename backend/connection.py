import mysql.connector

def fpdatabase():
    return mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1645",
    database = "fpdatabase",
)
