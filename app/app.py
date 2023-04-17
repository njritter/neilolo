from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/blog")
def blog():
    return "<p>I love you, Lolo! Page 2</p>"

@app.route("/wedding")
def wedding():
    return "<p>I love you, Lolo! Page 2</p>"