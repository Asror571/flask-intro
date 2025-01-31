from flask import Flask


app = Flask(__name__)

@app.route("/blog")
def blog_view():
    return "Bu blog sahifa"

@app.route("/")
def home_view():
    return "Bu Home sahifa"


app.run()
