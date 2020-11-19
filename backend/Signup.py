import mysql.connector
import re
from validate_email import validate_email

fpdatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "fpdatabase",
)

#checks how strong a password is returns true if it is strong
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


#checks to see if the user is alredy registered in the database
def userExists(username):
    my_cursor = fpdatabase.cursor()
    sql = "SELECT * FROM user WHERE userID= %s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    if results != None:
        return True
    else:
        return False

#Adds a user to the user data base ant then returns true if they were added correctly
def addUser(username,firstname, middlename, lastname, email, password):
    initalCheck = userExists(username)
    admin = 0
    my_cursor = fpdatabase.cursor()
    sqlStuff = "INSERT INTO user (userID,firstName, middleName, lastName, email, password, profilePicture, bio, admin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    my_cursor.execute(sqlStuff, (username, firstname, middlename, lastname, email, password, " ", " ", admin,))
    fpdatabase.commit()
    my_cursor.close()
    afterCheck = userExists(username)
    if initalCheck == False and afterCheck == True:
        return True
    else:
        return False
    my_cursor.close()

#checks to see if the userID is taken and adds the user if the user does not exist.
def signUp(username, firstname, middlename, lastname, email, password, password2):
        # is_valid = validate_email(email_address=email,
        #                           check_regex=True, check_mx=False,
        #                           smtp_timeout=10, dns_timeout=10, use_blacklist=True)
        '''
        if is_valid == True:
            print("Your email is valid")
        else:
            print("Your email is valid")
            signUp()

        '''
        if password == password2:
            print("Passwords match")
        else:
            print("Passwords don't match try again")
            return false
        '''
        if passwordChecker(password) == True:
            print("Strong password")
        else:
            print("Weak password try again")
            signUp()
        '''
        if userExists(username) == True:
            print("At least one of the credentials is in use. Try again")
            signUp()
        else:
            print("The credentials are not in use. Congratulations! You have signed up!")
            addUser(username,firstname, middlename, lastname, email, password)


