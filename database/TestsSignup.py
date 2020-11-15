import Signup

def testSignup():
    username = "Antonio"
    firstname = "Antonio"
    middlename = "Raffaele"
    lastname = "Di Pio"
    email = "antoniord311@gmail.com"
    password = input("D0gsl3d14@")
    password2 = input("Dogsl3d14@")
    record = (username, firstname, middlename, lastname, email, password, password2)
    addUser(record)