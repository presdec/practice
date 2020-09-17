from flask import Flask
from flask import jsonify # <- `jsonify` instead of `json`
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
    # c = 1/0
    retJson = {
        'field1':'abc',
        'field2':'def'
    }
    return jsonify(retJson)

if __name__ == "__main__":
    app.run(debug=True)
