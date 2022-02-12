from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/<name>")
def name():
    return "<p>Hello, World!</p>" + name
