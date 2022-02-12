from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello monty!</p>"

@app.route("/bye")
def gt():
    return "<h1>rohit<h1> "


