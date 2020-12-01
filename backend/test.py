import Signup as thingToTest
import mysql.connector 
import connection
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import connection

PATH = "C:\Program Files (x86)\chromedriver.exe"

example_data1 = {
    "username":     "chlo",
    "firstname":    "Chloe",
    "middlename":   "Greg",
    "lastname":     "Franklin",
    "email":        "rkerby18@gmail.com",
    "password1":     "beans",
    "password2":    "beans",
}

example_data2 = {
    "username":     "lRichards",
    "firstname":    "Larry",
    "middlename":   "Bjorn",
    "lastname":     "Richards",
    "email":        "rkerby18@gmail.com",
    "password1":     "fields",
    "password2":    "fields",
}


def testSignup(testData):
    driver = webdriver.Chrome(PATH)
    driver.get("http://127.0.0.1:5000/")

    time.sleep(1)
    button = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/a[2]")
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

    #time.sleep(1)
    button2 = driver.find_element_by_xpath("/html/body/div/form/input[6]")
    button2.click()
    driver.close()

    if (userExists(testData["username"])):
        print("User: ", testData["username"], " successfully added")
    else:
        print("User: ", testData["username"], " NOT added")


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

def cleanUp(testData):
    fpdatabase = connection.fpdatabase()
    my_cursor = fpdatabase.cursor()
    sql = "DELETE FROM user WHERE userID = %s"
    user = (testData["username"],)
    my_cursor.execute(sql, user)
    fpdatabase.commit()
    my_cursor.close()

# initial cleanup from previous tests
cleanUp(example_data1)
cleanUp(example_data2)

# Test Case 1
try:
    testSignup(example_data1)
except:
    print("test1- Something went wrong")
else:
    print("test1- Nothing went wrong")

# Test Case 2 (will fail due to non matching passwords)
try: 
    testSignup(example_data2)
except:
    print("test2- Something went wrong")
else:
    print("test2- Nothing went wrong")

# Final Clean up removing test users
cleanUp(example_data1)
cleanUp(example_data2)
