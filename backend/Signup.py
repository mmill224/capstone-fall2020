import mysql.connector
import re
from validate_email import validate_email

fpdatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "fpdatabase",
)

#Function that checks how stron a password is returns true if it is strong
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

#Checks cedentials and returns true if one is already in use
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

#Adds a user to the user data base
def addUser(username,firstname, middlename, lastname, email, password):
    initalCheck = userExists(username)
    admin = 0
    my_cursor = fpdatabase.cursor()
    sqlStuff = "INSERT INTO user (userID,firstName, middleName, lastName, email, password, admin) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    record = (username,firstname, middlename, lastname, email, password, admin)
    my_cursor.execute(sqlStuff, record)
    fpdatabase.commit()
    afterCheck = userExists(username)

    if initalCheck == False and afterCheck == True:
        return True
    else:
        return False
    my_cursor.close()

def userExists(username):
    my_cursor = fpdatabase.cursor()
    sql = "SELECT * FROM user WHERE userID = %s"
    user = (username)
    my_cursor.execute(sql, user)
    results = my_cursor.fetchone()
    if relsuts == None:
        return False
    else:
        return True


def signUp(username, firstname, middlename, lastname, email, password, password2):
    while True:
        is_valid = validate_email(email_address=email,
                                  check_regex=True, check_mx=False,
                                  smtp_timeout=10, dns_timeout=10, use_blacklist=True)
        '''
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
        '''
        if cedentialCheck(username, email) == True:
            print("At least one of the credentials is in use. Try again")
            signUp()
        else:
            print("The credentials are not in use. Congradulations you have signed up!")
            addUser(username,firstname, middlename, lastname, email, password)