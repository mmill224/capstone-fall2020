import mysql.connector
from passlib.hash import bcrypt

# Immidiately hashes password upon input
#hashed_password = sha256_crypt.hash((input("Please enter a password: ")))
#print(hashed_password)

#password2 = input("Re-enter your password: ")
#print(sha256_crypt.hash(password2))

#hashed_password2 = sha256_crypt.hash(password2)
# if (hashed_password == hased_password2) ....
# ^^ THIS WILL FAIL ^^
# Hashed passwords are not the same even if the same string is used

# Can use verify function to test if equal


fpdatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "fpdatabase",
)
'''
def existingUser():
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * from user")
    result = my_cursor.fetchall()
    for row in result:
        print(row[6])
'''
def userExists(username):
    my_cursor = fpdatabase.cursor()
    sql = "SELECT * FROM user WHERE userID= %s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    if results != None:
        return True
    else:
        return False

def passwordCheck(username,password):
    my_cursor = fpdatabase.cursor()
    sql = "SELECT password FROM user WHERE userID = '%s'"
    user = (username)
    my_cursor.execute(sql, user,)
    results = my_cursor.fetchone()
    print(password)
    print (results)

    if (bcrypt.verify((password,), results)) == True:
            print("Passwords match")
    else:
            print("Passwords do not match")


def addUser(username,firstname, middlename, lastname, email,password):
    admin = 0
    my_cursor = fpdatabase.cursor()
    sqlStuff = "INSERT INTO user (userID,firstName, middleName, lastName, email, password,profilePicture, admin) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    record = (username,firstname, middlename, lastname, email,password,"1", admin)
    my_cursor.execute(sqlStuff, record)
    fpdatabase.commit()
    my_cursor.close()

def passHash(password):
    hashed_password = bcrypt.hash(password)
    return hashed_password
def signUp():

    username = input("Please enter a username: ")
    firstname = input("Please enter your first name: ")
    middlename = input("Please enter your middle name: ")
    lastname = input("Please enter your last name: ")
    email = input("Please enter your email: ")
    hashed_password = passHash(input("Please enter a password: "))
    password2 = input("Re-enter your password: ")
    hashed_password2 = bcrypt.hash(password2)

    if (bcrypt.verify(password2, hashed_password)):
        print("Passwords match")
    else:
        print("Passwords do not match")

    print(hashed_password)

    addUser(username,firstname, middlename, lastname, email, hashed_password)


def returningUser():
    username = input("Please enter a username: ")
    password = input("Please enter your password: ")

    if userExists(username) == True:
        print("Welcome! " + username + " What would you like to do?")

#Checks the user's username and password with the one in the database and returns true or false
def passwordCheck(username,password):
    my_cursor = fpdatabase.cursor()
    sql = "SELECT password FROM user WHERE userID = %s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    if (bcrypt.verify(password, results[0])) == True:
        print("login sucsess")
        return True
    else:
        print("login failed")
        return False



if __name__ == '__main__':
    #signUp()
    i = input("Enter your username")
    j = input("Enter your password")

    passwordCheck(i,j)

    '''
    signUp()
    existingUser()
    fpdatabase.commit()
    '''
    #my_cursor.close()