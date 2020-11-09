import mysql.connector
import re
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


def signUp():
    while True:
        username = input("Please enter a username: ")
        email = input("Please enter your email: ")
        password = input("Please enter your password: ")
        password2 = input("Please enter your password: ")
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
        user_id = 1
        my_cursor = logindb.cursor()
        find_user = "SELECT * FROM users Where username = ?,email = ? and password = ?"
        my_cursor.execute(find_user,[(username),(email),(password)])
        results = my_cursor.fetchall()

        if results:
            for i in results:
                print("Your email or password is alredy taken or registered")
                signUp()

        else:
            print("You have registered sucsessfully")
            sqlStuff = "INSERT INTO users (username,email,password) VALUES (%s,%s,%s)"
            record = (username, email, password)
            again = input("Do you want to try again?(y/n): ")
            return("exit")

def returningUser():
    username = input("Please enter a username: ")
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    #with mysql.connect("users.db") as db:
    my_cursor = logindb.cursor()
    find_user = "SELECT * FROM users Where email = ? and password = ? "
    my_cursor.execute(find_user, [(username),(email),(password)])
    results = my_cursor.fetchall()

    if results:
        for i in results:
            print("Welcome " + i[1])
        return ("exit")

    else:
        print("Email and or password not recognized")
        again = input("Do you want to try again?(y/n): ")
        if again.lower() == "y":
            returningUser()
        elif again.lower() == "n":
            print("Goodbye")
            return ("exit")

if __name__ == '__main__':
    userType = input("Are you a new or returning user? n/r")
    i = 1
    attempts = 4
    while i < attempts:
        if userType == "n":
            signUp()
        elif userType == "r":
            returningUser()
        else:
            print("Not a valid input")

    logindb.commit()
    #my_cursor.close()



