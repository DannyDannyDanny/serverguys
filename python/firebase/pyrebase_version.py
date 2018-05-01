# tried to follow this guide:
# https://github.com/thisbejim/Pyrebase
# running into problems made this issue:
# https://github.com/thisbejim/Pyrebase/issues/258

import pyrebase

config = dict()
config["apiKey"] = "AIzaSyDwjaU5XynENL7KkA1r3KxFl5utBcYInlQ"
config["authDomain"] = "sarp-test.firebaseapp.com",
config["authDomain"]= "sarp-test.firebaseapp.com",
config["databaseURL"]= 'https]=//sarp-test.firebaseio.com',
config["projectId"]= "sarp-test",
config["storageBucket"]= "sarp-test.appspot.com",
config["messagingSenderId"]= "39530714599"

# creds
email = "dth@qub.dk"
password = "mypassword"

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)

# This is where shit hits the fan
db = firebase.database()

# I dont know if this will run
db.child("users").child("Morty")
print("nice")
