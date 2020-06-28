from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
       name = "Jose"
       pup_dictionary = {'pup_name':'Sammy'}
       letters = list(name)
       return render_template('basic.html', name=name, letters=letters,
                              pup_dictionary=pup_dictionary)

if __name__ == '__main__':
    app.run(debug=True)