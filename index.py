from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/db_teamanime'
mongo = PyMongo(app)

@app.route('/') 
def home():
    return render_template('home.html')


@app.route('/video', methods =['POST'])
def video():
    return render_template('video.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug = True)