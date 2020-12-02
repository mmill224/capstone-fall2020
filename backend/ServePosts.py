import Login
import os

def servePosts(username = ""):
    if username == "":
        posts = Login.viewPosts(username)
        for post in posts:
            post = {
                "postID" : post[0],
                "image" : post[1],
                "description" : post[2],
                "firstname" : post[3],
                "lastname" : post[4],
                "profilePicture" : post[5],
                "filename" : post[6]
            }
        return posts
    else:
        return True