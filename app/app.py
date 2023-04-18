from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/blog")
def blog():
    return "<p>I love you, Lolo! Page 2</p>"


@app.route("/wedding")
def wedding():
    return render_template("wedding.html")
