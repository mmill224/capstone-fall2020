This file clarifies the directory structure

backend contains the database, any queries we have saved, and all .py files.

backend also contains the directories static and templates

static contains any resources like .css files, images, or really anything that every user will see.

templates contains html files. The purpose of these files is to give structure to the data presented to the users (block elements in which
to display newsfeed posts, profiles, or any forms that our webapp has). 

These files are used by flask in capstone-falle2020/backend/main.py to generate a structured and styled view for the data presented to
the users.

I have no idea what root contains or why it exists.


I hope this clarifies why the structure of our project looks like this.

Any future .py files belong in backend. Any future .html files belong in backend/templates. Any future .css files or common resources
(like logos, pictures or anything that every user should be able to see) belong in backend/static/{{good name for the directory}}