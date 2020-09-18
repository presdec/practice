from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if (functionName == "add" or functionName == "sub" or functionName == "div" or functionName == "mul"):
        if "x" not in postedData or "y" not in postedData:
            return 301
        else:
            return 200


class Add(Resource):
    def post(self):
        # If i'm here then the resource add was requested by post
        postedData = request.get_json()

        # Get posted Data

        # Verify Valid
        status_code = checkPostedData(postedData, "add")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x+y
        retMap = {
            "Sum": ret,
            "Status Code": status_code
        }
        return jsonify(retMap)


class Subtract(Resource):
    def post(self):
        # If i'm here then the resource sub was requested by post
        postedData = request.get_json()

        # Get posted Data

        # Verify Valid
        status_code = checkPostedData(postedData, "sub")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x-y
        retMap = {
            "Sum": ret,
            "Status Code": status_code
        }
        return jsonify(retMap)


class Multiply(Resource):
    def post(self):
        # If i'm here then the resource mul was requested by post
        # get data
        postedData = request.get_json()

        # Verify Valid
        status_code = checkPostedData(postedData, "mul")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        ret = x*y
        retMap = {
            "Sum": ret,
            "Status Code": status_code
        }
        return jsonify(retMap)


class Divide(Resource):
    def post(self):
        # If i'm here then the resource div was requested by post
        # Get data
        postedData = request.get_json()

        # Verify valid
        status_code = checkPostedData(postedData, "div")
        if (status_code != 200):
            retJson = {
                "Message": "An error happened",
                "Status Code": status_code
            }
            return jsonify(retJson)

        x = postedData["x"]
        y = postedData["y"]
        x = int(x)
        y = int(y)
        if y == 0:
            retMap = {
                "Sum": "ZeroDivisionError",
                "Status Code": 301
            }
            return jsonify(retMap)
        else:
            ret = x/y
            retMap = {
                "Sum": ret,
                "Status Code": status_code
            }
            return jsonify(retMap)


@app.route('/')
def hello():
    return 'Hello World!'


api.add_resource(Add, "/add")
api.add_resource(Subtract, "/sub")
api.add_resource(Multiply, "/mul")
api.add_resource(Divide, "/div")

if __name__ == '__main__':
    app.run(host='0.0.0.0')