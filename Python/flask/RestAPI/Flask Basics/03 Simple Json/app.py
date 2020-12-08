from flask import Flask, jsonify # <- `jsonify` instead of `json`
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
    age = 2*534
    # c = 1/0
    retJson = {
        'Name': 'Bob',
        'Age': age,
        'phones':[
            {
                "phoneName": "Iphone8",
                'phoneNumber': 6666666666
            },
            {
                "phoneName": "Iphone8",
                "PhoneNumber": 6666666666
            },
        ]
    }
    return jsonify(retJson)

if __name__ == "__main__":
    app.run(debug=True)
