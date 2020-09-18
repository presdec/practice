from flask import Flask, jsonify, request # <- `jsonify` instead of `json`
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/hithere')
def hi_there():
    return "Hi There!"


@app.route('/add_two_nums', methods=["POST", "GET"])
def add_two_nums():
    # Get x & y from POST
    dataDict = request.get_json()

    if "y" not in dataDict:
        return "ERROR", 305
    x = dataDict["x"]
    y = dataDict["y"]
    # Add X + Y Store in Z
    z = x+y
    # Prepare a Json, "z":z
    retJSON = {
        'z': z
    }
    # return jsonify(map_prepared)
    return jsonify(retJSON), 200


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
