import Signup as thingToTest

example_data1 = {
    "username":     "mattMiller",
    "firstname":    "Matt",
    "middlename":   "Kyle",
    "lastname":     "Miller",
    "email":        "mkmiller96@gmail.com",
    "password":     "Dr.SambaIsAmazing123",
    "password2":    "Dr.SambaIsAmazing123",
}


# use this to remove any records that we don't want permanently.
# this doesn't really work yet
def cleanUp(username):
    my_cursor = fpdatabase.cursor()
    sql = "DELETE FROM user WHERE userID = %s"
    my_cursor.execute(sql, username)
    fpdatabase.commit()



def testSignup(username, firstname, middlename, lastname, email, password, password2):
    print("Testing signUp()... \n")
    thingToTest.signUp(username, firstname, middlename, lastname, email, password, password2)
    return


test = input("Would you like to test signUp? [y/n]: ")

if(test == 'y'):
    try:
        testSignup(example_data1["username"], example_data1["firstname"], example_data1["middlename"], example_data1["lastname"], example_data1["email"], example_data1["password"], example_data1["password2"])
    except:
        pass

