from flask import Flask, render_template, request

app = Flask(__name__) # __name__ refers to the name of the current file; this line tells "Turns this file into a flask application"

@app.route("/")
def index():
    # if "name" in request.args:
    #     name = request.args["name"]
    # else:
    #     name = "world"
    name = request.args.get("name", "world") # instead of above four lines, we can use only this line, which works same
    return render_template("index.html", placeholder=name) # browser address eg. local host/?name="Tamim"