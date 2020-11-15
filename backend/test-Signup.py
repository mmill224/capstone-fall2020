import Signup

example_data1 = {
    "username":     "mattMiller",
    "firstname":    "Matt",
    "middlename":   "Kyle",
    "lastname":     "Miller",
    "email":        "mkmiller96@gmail.com",
    "password":     "Dr.SambaIsAmazing123",
    "password2":    "Dr.SambaIsAmazing123",
}

def testSignup(username, firstname, middlename, lastname, email, password, password2):
    print("Testing signUp()... /n")
    signUp(username, firstname, middlename, lastname, email, password, password2)
    return

testSignup(example_data1.username, example_data1.firstname, example_data1.middlename, example_data1.lastname, example_data1.email, example_data1.password, example_data1.password2)

