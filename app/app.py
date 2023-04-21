from flask import Flask, render_template
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

user = {"username": "Neilolo"}


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/reception")
def reception():
    return render_template("reception.html")


@app.route("/schedule")
def schedule():
    return render_template("schedule.html")


@app.route("/photos")
def photos():
    return render_template("photos.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


if __name__ == "__main__":
    app.run(debug=True)
