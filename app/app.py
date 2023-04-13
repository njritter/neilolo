from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/page2")
def hello_world2():
    return "<p>I love you, Lolo! Page 2</p>"
