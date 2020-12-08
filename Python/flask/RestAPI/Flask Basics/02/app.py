from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/hithere')
def hi_there():
    return "Hi There!"


@app.route('/bye')
def bye():
    # Prepare a responce for the request that came to /bye
    c = 2*534
    s = str(c)
    return("Bye")


if __name__ == "__main__":
    app.run(debug=True)
