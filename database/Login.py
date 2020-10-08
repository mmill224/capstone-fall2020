import mysql.connector
# import validate_email

def signUp():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        with mysql.connect("Login.db") as db:
            cursor = db.cursor()
        find_user = "SELECT * FROM users Where username = ? and password = ? "
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()
        #I need to add the email check here

        if results:
            for i in results:
                print("Welcome "+i[2])
            return ("exit")

        else:
            print("Username and password not recognized")
            again = input("Do you want to try again?(y/n): ")
            if again.lower() == "n":
                print("Goodbye")
                #time.sleep(1) Need to read more about time.
                return("exit")

#def oldUser():

#def Login():
