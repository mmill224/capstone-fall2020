import mysql.connector
import re
from validate_email import validate_email

fpdatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "fpdatabase",
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
def cedentialCheck(username, email):
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM user")
    results = my_cursor.fetchall()
    #loop through all the records
    for row in results:
        if username == row[0]:
            return True
        elif email == row[4]:
            return True
        else:
            return False

def existingUser(username, email, password):
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM user")
    results = my_cursor.fetchall()
    #loop through all the records
    for row in results:
        if username == row[0] and email == row[4]:
            return True
        else:
            return False

def addUser(username,firstname, middlename, lastname, email, password):
    admin = 0
    my_cursor = fpdatabase.cursor()
    sqlStuff = "INSERT INTO user (userID,firstName, middleName, lastName, email, password, admin) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    record = (username,firstname, middlename, lastname, email, password, admin)
    my_cursor.execute(sqlStuff, record)
    fpdatabase.commit()
    my_cursor.close()

def signUp():
    while True:
        username = input("Please enter a username: ")
        firstname = input("Please enter your first name: ")
        middlename = input("Please enter your middle name: ")
        lastname = input("Please enter your last name: ")
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

        if cedentialCheck(username, email) == True:
            print("At least one of the credentials is in use. Try again")
            signUp()
        else:
            print("The credentials are not in use. Congradulations you have signed up!")
            addUser(username,firstname, middlename, lastname, email, password)


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

    fpdatabase.commit()
    #my_cursor.close()