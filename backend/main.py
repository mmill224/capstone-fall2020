from flask import Flask, request, render_template
import Login as Login
import Signup as Signup

user = None

app = Flask(__name__)

@app.route('/')
def landingPage():
    if user == None:
        return render_template("landing.html")
    else:
        return render_template("newsfeed.html")


# this function needs to be refactored, including the Signup.signUp function
@app.route('/sign-up', methods = ["POST", "GET"])
def signUpPage():
    #if user == None:
        if request.method == "POST":
            print("Something is happening")     # debugging
            username = request.form["username"]
            firstname = request.form["firstname"]
            lastname = request.form["lastname"]
            password1 = request.form["pass1"]
            password2 = request.form["pass2"]
            print(username, firstname, lastname, password1, password2, "It has been done") # debugging
            try:
                Signup.signUp(username, firstname, '', lastname, '', password1, password2)
            except:
                print('Signup.signUp failed')   # debugging
                return "<p>Not successful</p>"
            user = username
            return render_template("newsfeed.html") # signup successful, redirect to newsfeed.html
        #else:
        return render_template("sign-up.html")  # if method != POST
   # else:  
        return render_template("newsfeed.html")     # if there is a user




@app.route('/sign-in', methods = ["POST", "GET"])
def signInPage():
    if user == None:
        
        return render_template("sign-in.html")
    else: 
        return render_template("newsfeed.html")

@app.route('/newsfeed')
def newsfeedPage():
    if user != None:
        query = Login.viewPosts()
        return render_template("newsfeed.html", posts=query)
    # else:
    #     return render_template("landing.html")

@app.route('/events')
def eventsPage():
    if user != None:
        return render_template("events.html")
    else: 
        return render_template("landing.html")

@app.route('/create-post')
def createPostPage():
    if user != None:
        return render_template("create-post.html")
    else: 
        return render_template("landing.html")


@app.route('/{user}')
def viewProfilePage(user):
    mydict = viewUser(user)
    if mydict != None:
        mydict["user"][0]


if __name__ == "__main__":
    app.run(debug=True)