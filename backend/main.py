from flask import Flask, request, render_template, session, redirect, url_for
import Login as Login
import Signup as Signup

user = None

app = Flask(__name__)
app.secret_key = "jNhMTwWMXZLbCYV" # for session

@app.route('/')
def landingPage():
    if "user" in session:
        return redirect(url_for("newsfeedPage"))
    else:
        return render_template("landing.html")

# todo
# make sure the user doesn't fucking give us empty strings wtf
# this function needs to be refactored, including the Signup.signUp function
@app.route('/sign-up', methods = ["POST", "GET"])
def signUpPage(): 
    if "user" not in session: # if there is a user in session
        if request.method == "POST":
            print('request method == POST')     # debugging
            username = request.form["username"]
            firstname = request.form["firstname"]
            lastname = request.form["lastname"]
            password1 = request.form["pass1"]
            password2 = request.form["pass2"]
            if username == '' or password1 == '' or password2 == '' or firstname == '':
                return redirect(url_for('signUpPage'))
            print('Here are the credentials used: ', username, firstname, lastname, password1, password2) # debugging
            try:
                Signup.signUp(username, firstname, '', lastname, '', password1, password2)
            except:
                print('Signup.signUp failed')   # debugging
                return "<p>Not successful</p>"  # should only reach this point if Signup.signup() is broken
            session["user"] = username # creates a session on successful account creation
            return redirect(url_for('newsfeedPage')) # signup successful, redirect to newsfeed.html
        else:
            return render_template("sign-up.html")  # if method != POST
   # else:  
        return render_template("newsfeed.html")     # if there is a user



@app.route('/sign-in', methods = ["POST", "GET"])
def signInPage():
    if "user" in session:                           # if the user is already logged in, just go to newsfeed
        return redirect(url_for("newsfeedPage"))
    else:                                           # if the user is not logged in, check if they submitted form data
        if request.method == "POST":                # if the user submitted form data, check it against database
            print("Request method == POST") #debug
            username = request.form["username"]
            password = request.form["pass"]
            if username == '' or password == '':
                return redirect(url_for('signInPage'))
            success = Login.passwordCheck(username, password)
            if success:                             # if the database check worked, add their username to the session
                session["user"] = username
                print("signed in")
                return redirect(url_for("newsfeedPage"))
            else:                                   # if it did not work, just go back to the sign-in page
                print("failed to sign in")
                return render_template("sign-in.html")
    print("Request method == (probably) GET")                
    return render_template("sign-in.html")          # if the user requested via get, just render the page

@app.route('/newsfeed')
def newsfeedPage():
    if user == None:
        query = Login.viewPosts() # uses default parameters for this function, returning all posts by all users
        return render_template("newsfeed.html", posts=query)
    else:
        return redirect(url_for("landingPage"))

@app.route('/events')
def eventsPage():
    if user == None:
        return render_template("events.html")
    else: 
        return redirect(url_for("landingPage"))


@app.route('/create-post', methods = ["POST", "GET"])
def createPostPage():
    if 'user' in session:
        if request.method == "POST":
            print("Request method == POST")
            description = request.form["description"]
            image = request.form["image"]
            print(description, '\n', image)
            # instead, this should add the posts to the database
            return redirect(url_for("newsfeedPage"))
        else:    
            return render_template("create-post.html")
    else: 
        return redirect(url_for("landingPage"))

@app.route('/my-profile')
def myProfilePage():
    if 'user' in session:
        user = session["user"]
        print(user)
        query = Login.viewPosts(user)
        return render_template("profile-template.html", profile = query)
    else:
        return redirect(url_for("landingPage"))


@app.route('/logout')
def logout():
    session.pop("user", None)
    print('Session has ended!')
    return redirect(url_for("landingPage"))


# @app.route('/{user}')
# def viewProfilePage(user):
#     mydict = viewUser(user)
#     if mydict != None:
#         mydict["user"][0]


if __name__ == "__main__":
    app.run(debug=True)




# Template for going to a page that has form elements and requires a user to be logged in
# @app.route('/create-post', methods = ["POST", "GET"])
# def createPostPage():
#     if 'user' in session:
#         if request.method == "POST":
#             print("Request method == POST")
#         else:    
#             return render_template("create-post.html")
#     else: 
#         return redirect(url_for("landingPage"))