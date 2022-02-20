from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/bye")
def gt():
    return "<h1>rohit<h1> "

@app.route("/SIGNUP")
@app.route('/')
def signup_page():
    return render_template("SIGNUP.html")