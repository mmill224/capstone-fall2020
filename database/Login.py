import mysql.connector
import re
#import mysql
# import validate_email

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

        with mysql.connect("Login.db") as db:
            cursor = db.cursor()
        find_user = "SELECT * FROM users Where email = ? and password = ? "
        cursor.execute(find_user,[(email),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Your email or password is alredy taken or registered")
                signUp()

        else:
            print("You have registered sucsessfully")
            #need to add user here
            again = input("Do you want to try again?(y/n): ")
            return("exit")

def returningUser():
    email = input("Please enter your email: ")
    password = input("Please enter your password: ")
    with mysql.connect("Login.db") as db:
        cursor = db.cursor()
    find_user = "SELECT * FROM users Where email = ? and password = ? "
    cursor.execute(find_user, [(email), (password)])
    results = cursor.fetchall()

    if results:
        for i in results:
            print("Welcome " + i[1])
        return ("exit")

    else:
        print("Email and or password not recognized")
        again = input("Do you want to try again?(y/n): ")
        if again.lower() == "y":
            retuningUser()
        elif again.lower() == "n":
            print("Goodbye")
            return ("exit")

if __name__ == '__main__':
    userType = input("Are you a new or returing user? n/r")
    i = 1
    while i < 4:
        if userType == "n":
            signUp()
        elif userType == "r":
            returningUser()
        else:
            print("Not a valid input")




