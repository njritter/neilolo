from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.route("/photos")
def photos():
    return render_template("photos.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")
