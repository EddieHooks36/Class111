from flask import Flask       # From flask module import the Flask class

app = Flask(__name__)         # Create an instance of Flask into variable called "app"
                              # From this point forward, app is an "object"

@app.get("/")                 # Flask specific decorator to create routes
def about_me():               # View fumction. Functions mapped to routes are called view functions
    me = {                    
        "first_name": "Eddie", # On line 8, we are creating a dictionary withour details
        "last_name": "Hooks",
        "hobbies": "Disc Golf",
        "active": True
    }

    return me                  # When we return a dictionary from a view fumction
                               # Flask automatically converts it to JSON