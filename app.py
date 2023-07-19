from flask import Flask, render_template, request

app = Flask(__name__) # __name__ refers to the name of the current file; this line tells "Turns this file into a flask application"

@app.route("/")
def index():
    # return "hello world" # this will spit out no html file
    return render_template("index.html")