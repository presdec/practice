from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello Puppy!"

@app.route('/information')
def info():
    return "<h1>Puppies are cute!</h1)"
if __name__ == '__main__':
    app.run()