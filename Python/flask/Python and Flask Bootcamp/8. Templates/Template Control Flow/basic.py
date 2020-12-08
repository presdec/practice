from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
       myList = [1,2,3,4,5]
       puppies = ['Fluffy','Rufus','Spike']
       user_logged_in = False
       return render_template('basic.html',user_logged_in=user_logged_in,
                              puppies=puppies, myList=myList)

if __name__ == '__main__':
    app.run(debug=True)