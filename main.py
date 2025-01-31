from flask import Flask, request


app = Flask(__name__)

@app.route("/blog")
def blog_view():
    return "Blog"

@app.route("/")
def home_view():
    return "Home"

@app.route("/add")
def add():
    args = request.args

    a = int(args['a'])
    b = int(args['b'])

    result = a + b
    print(result)

    return f"{a} + {b} = {result}"

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8000)
