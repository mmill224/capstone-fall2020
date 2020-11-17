import mysql.connector

fpdatabase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "coffeecup90",
    database = "fpdatabase",
)

#checks to see if the user is alredy registered in the database
def existingUser(username):
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM user")
    results = my_cursor.fetchall()
    #loop through all the records
    for row in results:
        if username == row[0]:
            return True
        else:
            return False

#Allows user to change thier bio in the user database and returns true if it was changed false if unchanged
def updateBio(username, newBio):
    bio = currentBio(username)
    my_cursor = fpdatabase.cursor()
    newBio = input("Enter an update to your bio")
    update = "UPDATE user SET bio = %s WHERE userID = %s"
    record = (newBio, username)
    my_cursor.execute(update, record)
    fpdatabase.commit()
    bio3 = currentBio(username)
    if bio == bio3:
        return False
    else:
        return True

#Function that checks to see if the bio was changed
def currentBio(username):
    my_cursor = fpdatabase.cursor()
    bio = "SELECT bio FROM user WHERE userID = %s"
    record = (bio, username)
    my_cursor.execute(bio, record)
    results = my_cursor.fetchone()
    return results


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
    #return true if successful

def createEvent(username):
    #date must be in YYYY - MM - DD
    eventID = input("Please enter a event id")
    eventName = input("Please enter a event name")
    description = input("Please enter a description: ")
    date = input("Please enter a date: ")
    location = input("Please enter a location: ")
    my_cursor = fpdatabase.cursor()
    post = "INSERT INTO event (eventID,eventName,description, date, location, eventUser) VALUES (%s,%s,%s,%s,%s,%s)"
    record = (eventID, eventName, description, date, location, username)
    my_cursor.execute(post, record)
    fpdatabase.commit()
    my_cursor.close()
    #return true if successful

#function that returns true if the user is a admin false if they are not a admin
def adminCheck(username):
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM user")
    results = my_cursor.fetchall()
    admin = 1
    # loop through all the records
    for row in results:
        if username == row[0] and admin == row[8]:
            return True
        else:
            return False


# something to consider is that this is almost exactly the same as the viewMyPosts or viewProfile function
# you could have all of these functions be written as one
# 
def viewPosts(username = ''):
    my_cursor = fpdatabase.cursor()
    if username == '':
        my_cursor.execute("SELECT * FROM post order by date desc")
    # else
    #     my_cursor.execute("SELECT * FROM post where post.userID = username order by date desc")

    results = my_cursor.fetchall()
    
    # loop through all the records
    for row in results:
        #postID = row[0]
        #image = row[1]
        #description = row[2]
        #date = row[3]
        #user = row[4]
        #print(postID, " " ,  image, " ", description," ", date, " ", user)
        return results
=======
    # for row in results:
    #     postID = row[0]
    #     image = row[1]
    #     description = row[2]
    #     date = row[3]
    #     user = row[4]
    #     print(postID, " " ,  image, " ", description," ", date, " ", user)


    # return a dictionary
    # dictToReturn = {
    #     "posts": results 
    #     "users": a query that returns first and last name and profile picture
    # }



def viewEvents():
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM event")
    results = my_cursor.fetchall()
    # loop through all the records
    for row in results:
        #eventID = row[0]
        #eventName = row[1]
        #description = row[2]
        #date = row[3]
        #location = row[4]
        #eventUser = row[5]
        #print(eventID, " ", eventName, " ", description, " ", date, " ", location, " ", eventUser)
        return results
        eventID = row[0]
        eventName = row[1]
        description = row[2]
        date = row[3]
        location = row[4]
        eventUser = row[5]
        print(eventID, " ", eventName, " ", description, " ", date, " ", location, " ", eventUser)    
    return results



def viewMyPosts(username):
    #first portion gets the user's info
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM user") #where userID = me
    results = my_cursor.fetchall()
    # loop through all the records
    for row in results:
        if username == row[0]:
            firstName = row[1]
            middleName = row[2]
            lastName = row[3]
            email = row[4]
            pic = row[6]
            bio = row[7]
            print(username, " ",firstName, " ", middleName, " ", lastName, " ", email, " ", pic, " ", bio)

    #second part gets all their posts
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM post") # where userid = me
    results = my_cursor.fetchall()
    # loop through all the records
    for row in results:
        if username == row[4]:
            postID = row[0]
            image = row[1]
            description = row[2]
            date = row[3]
            user = row[4]
            print(postID, " ", image, " ", description, " ", date, " ", user)
# should return a dictionary that contains the user record as one list and the posts table including only the posts by that username
# also, viewMyPosts, viewUser, and viewPosts
'''
def viewUser():
    username = input("Enter a user to view")
    #first portion gets the user's info
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM user")
    results = my_cursor.fetchone()
    # loop through all the records
    #for row in results:
    #if username == row[0]:
        #firstName = row[1]
        #middleName = row[2]
        #lastName = row[3]
        #email = row[4]
        #pic = row[6]
        #bio = row[7]
        #print(username, " ",firstName, " ", middleName, " ", lastName, " ", email, " ", pic, " ", bio)

    #second part gets all their posts
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM post")
    posts = my_cursor.fetchall()
    # loop through all the records
    #for row in results:
    if username == row[4]:
        postID = row[0]
        image = row[1]
        description = row[2]
        date = row[3]
        user = row[4]
        #print(postID, " ", image, " ", description, " ", date, " ", user)
'''
# posts = some sql where we see all of the posts the user has made
    # mydict = {
    #     "user": results,
    #     "posts": posts,
    # }
    # return mydict
    #if the way above does not work try assigning each value from above
    #mydict = "user": results, "posts": posts,}
    # return mydict

    # should return a dictionary that contains the user record as one list and the posts table including only the posts by that username
    # also, viewMyPosts, viewUser, and viewPosts 

def viewUser(user):
    username = input("Enter a user to view")
    #first portion gets the user's info
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM user") # where userID = this user
    results = my_cursor.fetchall()
    # loop through all the records
    # for row in results:
    #     if username == row[0]:
    #         firstName = row[1]
    #         middleName = row[2]
    #         lastName = row[3]
    #         email = row[4]
    #         pic = row[6]
    #         bio = row[7]
    #         print(username, " ",firstName, " ", middleName, " ", lastName, " ", email, " ", pic, " ", bio)
    # posts = some sql where we see all of the posts the user has made
    # mydict = {
    #     "user": results,
    #     "posts": posts, 
    # }
    # return mydict

    #second part gets all their posts
    my_cursor = fpdatabase.cursor()
    my_cursor.execute("SELECT * FROM post") # where userID = this user
    results = my_cursor.fetchall()
    # loop through all the records
    for row in results:
        if username == row[4]:
            postID = row[0]
            image = row[1]
            description = row[2]
            date = row[3]
            user = row[4]
            print(postID, " ", image, " ", description, " ", date, " ", user)

    # this should return a dict that contains a list called user and a list called posts (all of the posts this user owns)
'''
def adminTools():
    #need to add in these so only admins have the promts and privleges to use these tools
    deletePost()
    deleteUser()
'''
#signin needs to be reworked.
def signIn(username,password):
    signedIn =False
    while signedIn == False:
        if existingUser(username, password) == True:
            print("Welcome! " + username + " What would you like to do?")
            if adminCheck(username) == True:
                option = input("1)Create post, 2) Create bio, You are a admin 3) Create event, 4) Delete user, 5) Delete post")
            else:
                option = input("1)Create post, 2) Create bio 6) View posts 7) View events 8)view my posts 9)View other user:")
            if option == "1":
                #setProfilePic(username)
                createPost(username)
            elif option == "2":
                updateBio(username)
            elif option == "3":
                createEvent(username)
            elif option == "4":
                deleteUser(adminCheck(username))
            elif option == "5":
                deletePost(adminCheck(username))
            elif option == "6":
                viewPosts()
            elif option == "7":
                viewEvents()
            elif option == "8":
                viewMyPosts(username)
            elif option == "9":
                viewUser()
            else:
                print("Wrong Input:")
            return ("exit")

#Function allows a admin to delete any user
def deleteUser(admin):
    my_cursor = fpdatabase.cursor()
    if admin == 1:

        sql = "DELETE FROM user WHERE userID = %s"
        user = (input("Enter userId you wish to delete: "),)
        my_cursor.execute(sql, user)
        fpdatabase.commit()
        print(my_cursor.rowcount, "User deleted")

    else:
        print ("You do not have admin access to delete users.")
        return ("exit")

#Function That allows an admin to delete any post
def deletePost(admin):
    my_cursor = fpdatabase.cursor()
    if admin == 1:
        sql = "DELETE FROM post WHERE postID = %s"
        post = (input("Enter postId you wish to delete: "),)
        my_cursor.execute(sql, post)
        fpdatabase.commit()
        print(my_cursor.rowcount, "User deleted")

#Function to allow users to delete their own posts if wanted
def deleteSelfPost(postID, username):
    my_cursor = fpdatabase.cursor()
    sql = "DELETE FROM post WHERE postID = %s AND postUser = %s"
    post = (postID, username,)
    my_cursor.execute(sql, post)
    fpdatabase.commit()

#Function to get a user's first name last name and profile pic
def getUserInfo(username):
    my_cursor = fpdatabase.cursor()
    sql = "SELECT firstName, lastName, profilePicture FROM user WHERE userID = %s"
    user = (username)
    my_cursor.execute(sql, user)
    results = my_cursor.fetchall()
    return relsuts


