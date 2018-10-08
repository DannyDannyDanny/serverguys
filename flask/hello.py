from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    a = input()
    return "Hello World!"
