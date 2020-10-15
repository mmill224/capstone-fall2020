import mysql.connector

logindb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "password",
)

cursor = logindb.cursor()
