import mysql.connector
import re
from validate_email import validate_email
#import mysql
#import validate_email
logindb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "testdb",
)

def passwordChecker(password):
    #check the password length
    if len(password) < 8:
        return False

    #checks for lower
    lowerCheck = re.compile(r'[a-z]')
    if not(lowerCheck.search(password)):
        return False

    #checks for upper
    upperCheck = re.compile(r'[A-Z]')
    if not(upperCheck.search(password)):
        return False

    #checks for number
    numCheck = re.compile(r'\d')
    if not(numCheck.search(password)):
        return False

    #checks for special character
    spCheck = re.compile(r'\W')
    if not(spCheck.search(password)):
        return False

    else:
        return True

#checks cedentials and returns true if one is already in use
def cedentialCheck(username, email, password):
    my_cursor = logindb.cursor()
    my_cursor.execute("SELECT * FROM users")
    results = my_cursor.fetchall()
    #loop through all the records
    for row in results:
        if username == row[0]:
            return True
        elif email == row[1]:
            return True
        elif password == row[2]:
            return True
        else:
            return False

def existingUser(username, email, password):
    my_cursor = logindb.cursor()
    my_cursor.execute("SELECT * FROM users")
    results = my_cursor.fetchall()
    #loop through all the records
    for row in results:
        if username == row[0] and email == row[1] and password == row[2]:
            return True
        else:
            return False

def addUser(username, email, password):
    my_cursor = logindb.cursor()
    sqlStuff = "INSERT INTO users (userName,email,password) VALUES (%s,%s,%s)"
    record = (username, email, password)
    my_cursor.execute(sqlStuff, record)

def signUp():
    while True:
        username = input("Please enter a username: ")
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")
        password2 = input("Please enter your password: ")
        is_valid = validate_email(email_address='example@example.com', \
                                  check_regex=True, check_mx=False, \
                                  from_address='my@from.addr.ess', helo_host='my.host.name', \
                                  smtp_timeout=10, dns_timeout=10, use_blacklist=True)
        if is_valid == True:
            print("Your email is valid")
        else:
            print("Your email is valid")
            signUp()

        if password == password2:
            print("Passwords match")
        else:
            print("Passwords don't match try again")
            signUp()

        if passwordChecker(password) == True:
            print("Strong password")
        else:
            print("Weak password try again")
            signUp()

        if cedentialCheck(username, email, password) == True:
            print("At least one of the credentials is in use. Try again")
            signUp()
        else:
            print("The credentials are not in use. Congradulations you have signed up!")
            addUser(username, email, password)


def returningUser():
    username = input("Please enter a username: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")

    if existingUser(username, email, password) == True:
        print("Welcome " + username)
        return ("exit")
    else:
        print("Email and or password not recognized")
        again = input("Do you want to try again?(y/n): ")
        if again == "y":
            returningUser()
        elif again == "n":
            print("Goodbye")
            return ("exit")

if __name__ == '__main__':
    userType = input("Are you a new or returning user? n/r")
    i = 1
    attempts = 2
    while i < attempts:
        if userType == "n":
            signUp()
            i = i + 1
        if userType == "r":
            returningUser()
            i = i + 1
        else:
            print("Not a valid input")
            i = i + 1

    logindb.commit()
    #my_cursor.close()