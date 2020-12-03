import mysql.connector 
import connection
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import connection

PATH = "C:\Program Files (x86)\chromedriver.exe" # PATH should be wherever chromedriver.exe is on your machine

# Test data 1- basic successful addition of a user
example_data1 = {
    "username":     "bLawrence",
    "firstname":    "Bob",
    "middlename":   "Greggory",
    "lastname":     "Lawrence",
    "email":        "rkerby18@gmail.com",
    "password1":     "Password123!",
    "password2":     "Password123!",
    "signInPassword":  "Password123!", # used for sign in testing- should be same if sign in passes    
}

# Test data 2- does not add user because passwords entered do not match
example_data2 = {
    "username":     "lRichards",
    "firstname":    "Larry",
    "middlename":   "Bjorn",
    "lastname":     "Richards",
    "email":        "lrichards@gmail.com",
    "password1":     "Apples18!",
    "password2":    "Apples181!",   # Password doesn't match
}

# Test data 3- does not add user because username is blank
example_data3 = {
    "username":     "",
    "firstname":    "Carl",
    "middlename":   "Nigel",
    "lastname":     "Baker",
    "email":        "cbaker@gmail.com",
    "password1":     "Password123!",
    "password2":    "Password123!",
}

# Test data 4- adds user despite long username (still < 45) 
example_data4 = {
    "username":     "thisusernameiswaylongbutitwillstillwork",
    "firstname":    "name",
    "middlename":   "name",
    "lastname":     "name",
    "email":        "email@gmail.com",
    "password1":     "Password123!",
    "password2":    "Password123!",
    "signInPassword":  "Password123!",
}

# Test data 5- does not add user because username is >45
example_data5 = {
    "username":     "thisusernameiswaylongsoitwillnotworkwhoopsieee",
    "firstname":    "name",
    "middlename":   "name",
    "lastname":     "name",
    "email":        "email@gmail.com",
    "password1":     "Password123!",
    "password2":    "Password123!",
}

# Test data 6- Signup passes, but sign in fails- (simulates user entering wrong password on sign in page)
example_data6 = {
    "username":     "mDaniels",
    "firstname":    "Miranda",
    "middlename":   "Elizabeth",
    "lastname":     "Daniels",
    "email":        "email@gmail.com",
    "password1":    "MightyMiranda2798!",
    "password2":    "MightyMiranda2798!",
    "signInPassword":    "DifferentPassword123!",    # used for sign in testing- should be same if sign in passes
}

# testSignup function takes a dict as input (see above test cases ^^^) and uses chromedriver to sign up to the website
def testSignup(testData):
    driver = webdriver.Chrome(PATH)
    driver.get("http://127.0.0.1:5000/") # URL generated for the website (this may differ between machines..?)

    time.sleep(1) # Need to pause a sec after each chromedriver command to ensure proper data entry (safe)
    button = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/a[2]") # signup button xpath
    button.click()

    time.sleep(2)
    driver_username = driver.find_element_by_name("username")
    driver_username.send_keys(testData["username"])

    time.sleep(1)
    driver_firstname = driver.find_element_by_name("firstname")
    driver_firstname.send_keys(testData["firstname"])

    time.sleep(1)
    driver_lastname = driver.find_element_by_name("lastname")
    driver_lastname.send_keys(testData["lastname"])

    time.sleep(1)
    driver_password1 = driver.find_element_by_name("pass1")
    driver_password1.send_keys(testData["password1"])

    time.sleep(1)
    driver_password2 = driver.find_element_by_name("pass2")
    driver_password2.send_keys(testData["password2"])

    button2 = driver.find_element_by_xpath("/html/body/div/form/input[6]")
    button2.click()
    driver.close()

    if (userExists(testData["username"])):
        print("User: ", testData["username"], " successfully added")
    else:
        print("User: ", testData["username"], " NOT added")

# testSignin function takes a dict as input (see above test cases ^^^) and uses chromedriver to sign in to the website (if the account exists)
def testSignin(testData):
    driver = webdriver.Chrome(PATH)
    driver.get("http://127.0.0.1:5000/") # URL generated for the website (this may differ between machines..?)

    time.sleep(1) # Need to pause a sec after each chromedriver command to ensure proper data entry (safe)
    button = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/a[1]") # sign in button xpath
    button.click()

    time.sleep(2)
    driver_username = driver.find_element_by_name("username")
    driver_username.send_keys(testData["username"])

    time.sleep(1)
    driver_password1 = driver.find_element_by_name("pass")
    driver_password1.send_keys(testData["signInPassword"])

    time.sleep(1)
    button2 = driver.find_element_by_xpath("/html/body/div[1]/form/input[3]")
    button2.click()

    time.sleep(1)
    # As long as we're not redirected to the sign in page again -> sign in successful
    if (driver.title != "Sign in to Focal Point"):
        print("User: ", testData["username"], "sign in successful")
    else:
        print("User: ", testData["username"], "sign in NOT successful")
    
    driver.close()


# userExists function (used to tell if user was added to the database or not)
def userExists(username):
    fpdatabase = connection.fpdatabase()
    my_cursor = fpdatabase.cursor()
    sql = "SELECT * FROM user WHERE userID= %s"
    my_cursor.execute(sql, (username,))
    results = my_cursor.fetchone()
    my_cursor.close()
    if results != None:
        return True
    else:
        return False

# Removes user based on a test case for input- helps keep database clean throughout testing
def cleanUp(testData):
    fpdatabase = connection.fpdatabase()
    my_cursor = fpdatabase.cursor()
    sql = "DELETE FROM user WHERE userID = %s"
    user = (testData["username"],)
    my_cursor.execute(sql, user)
    fpdatabase.commit()
    my_cursor.close()

# initial cleanup from previous tests (good idea to keep just in case)
cleanUp(example_data1)
cleanUp(example_data2)
cleanUp(example_data3)
cleanUp(example_data4)
cleanUp(example_data5)
cleanUp(example_data6)

# Test Case 1 (user should be added)
try:
    testSignup(example_data1)
    testSignin(example_data1)
except:
    print("test1- Something went wrong")
else:
    pass

# Test Case 2 (user won't be added due to non matching passwords)
try: 
    testSignup(example_data2)
except:
    print("test2- Something went wrong")
else:
    pass

# Test Case 3 (user won't be added due to username being empty)
try: 
    testSignup(example_data3)
except:
    print("test3- Something went wrong")
else:
    pass

# Test Case 4 (user will be added with username <45)
try: 
    testSignup(example_data4)
    testSignin(example_data4)
except:
    print("test4- Something went wrong")
else:
    pass

# Test Case 5 (user won't be added due to username being >45)
try: 
    testSignup(example_data5)
except:
    print("test5- Something went wrong")
else:
    pass

# Test Case 6 (Sign up successful, sign in fails- wrong password)
try: 
    testSignup(example_data6)
    testSignin(example_data6)
except:
    print("test6- Something went wrong")
else:
    pass

# Final Clean up removing test users
cleanUp(example_data1)
cleanUp(example_data2)
cleanUp(example_data3)
cleanUp(example_data4)
cleanUp(example_data5)
cleanUp(example_data6)
