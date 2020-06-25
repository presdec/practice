from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome! Got to puppy_latin/name to see your name in puppy lating"

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1)"

@app.route('/puppy_latin/<name>')
def puppy(name):
    if name[-1] == "y":
        name = name[:-1]
        name = name + "iful"
    else:
        name = name + "y"
    return "Hi! Your Puppy Lating name is : {}".format(name)

if __name__ == '__main__':
    app.run(debug=True)