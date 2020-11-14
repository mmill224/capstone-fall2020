import os
import mysql.connector
import re
from validate_email import validate_email

fpdatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "fpdatabase"
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

def existingUser(username, password):
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM user")
    results = my_cursor.fetchall()
    #loop through all the records
    for row in results:
        if username == row[0] and password == row[5]:
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
        is_valid = validate_email(email_address=email,
                                  check_regex=True, check_mx=False,
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

#Allows user to change thier bio in the user database
def updateBio(username):
    my_cursor = fpdatabase.cursor()
    bio = input("Enter an update to your bio")
    update = "UPDATE user SET bio = %s WHERE userID = %s"
    record = (bio, username)
    my_cursor.execute(update, record)
    fpdatabase.commit()

'''
def insertFile(username, filepath):
    my_cursor = fpdatabase.cursor()
    with open(filepath, "rb") as file:
        binary = file.read()
    update = "UPDATE user SET profilePicture = %s WHERE userID = %s"
    record = (username, filepath)
    my_cursor.execute(update, record)
    fpdatabase.commit()

def setProfilePic(username):
    my_cursor = fpdatabase.cursor()
    option = input("Insert image/ Read image i/r")
    if option == "i":
        filepath = input("Enter file path:")
        insertFile(username, filepath)
    elif option == "r":
        idchoice = input("Enter ID:")
        # insert image
    fpdatabase.commit()
'''
#creates a post into the post database
def createPost(username):
    #date must be in YYYY - MM - DD
    postID = input("Please enter a post name: ")
    image = input("Please enter a image: ")
    description = input("Please enter a description: ")
    date = input("Please enter a date: ")
    my_cursor = fpdatabase.cursor()
    post = "INSERT INTO post (postID,image,description, date, postUser) VALUES (%s,%s,%s,%s,%s)"
    record = (postID, image, description, date, username)
    my_cursor.execute(post, record)
    fpdatabase.commit()
    my_cursor.close()

def returningUser():
    username = input("Please enter a username: ")
    password = input("Please enter your password: ")

    if existingUser(username, password) == True:
        print("Welcome " + username + "What would you like to do?")
        option = input("1)create post, 2) create bio:")

        if option == "1":
            #setProfilePic(username)
            createPost(username)
        if option == "2":
            updateBio(username)
#        if option == "3":
#           deleteUser(admin)
        else:
            print("Wrong Input:")
        return ("exit")
    else:
        print("Email and or password not recognized")
        again = input("Do you want to try again?(y/n): ")
        if again == "y":
            returningUser()
        elif again == "n":
            print("Goodbye")
            return ("exit")

def deleteUser(admin):
    my_cursor = fpdatabase.cursor()
    if admin == 1:
        sql = "DELETE FROM user WHERE userID = "
        user = ('1')
        print(sql, user)
        my_cursor.execute(sql, user)
        fpdatabase.commit()
        print(my_cursor.rowcount, "User deleted")

    else:
        print ("You do not have admin access to delete users.")
        return ("exit")



if __name__ == '__main__':
    admin = 1
    deleteUser(admin)
'''
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
    '''
    #my_cursor.close()