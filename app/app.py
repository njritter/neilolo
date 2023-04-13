from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>I love you, Lolo! Test 1</p>"
