# this file is out of date and is no longer used, I think


import mysql.connector
import mysql

logindb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "coffeecup90",
    database = "fpdatabase",
)
my_cursor = logindb.cursor()

#my_cursor.execute("CREATE DATABASE ant")

#my_cursor.execute("SHOW DATABASES")
#creates table
#my_cursor.execute("CREATE TABLE users (userName VARCHAR(50), email VARCHAR(50), password VARCHAR(50), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
#my_cursor.execute("SHOW TABLES;")


my_cursor = logindb.cursor()
#creates table
#




if __name__ == '__main__':
    username = input("Enter a username.")
    email = input("Enter a email.")
    password = input("Enter a password.")

    sqlStuff = "INSERT INTO users (userName,email,password) VALUES (%s,%s,%s)"
    record = (username, email, password)
    my_cursor.execute(sqlStuff, record)

    #my_cursor = logindb.cursor()
    #find_user = "SELECT * FROM users Where username = ? and email = ? and password = ?"
    #record = (username, email, password)
    #my_cursor.execute(find_user, record)
    #results = my_cursor.fetchall()

    logindb.commit()
    my_cursor.close()