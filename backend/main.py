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

@app.route('/sign-up')
def signUpPage():
    if user == None:
        return render_template("sign-up.html")
    else: 
        return render_template("newsfeed.html")

@app.route('/sign-in')
def signInPage():
    if user == None:
        #user = # get the user's userID
        return render_template("sign-in.html")
    else: 
        return render_template("newsfeed.html")

@app.route('/newsfeed')
def newsfeedPage():
    #if user != None:
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

if __name__ == "__main__":
    app.run(debug=True)