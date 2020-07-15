from flask import Flask
from flask_pymongo import PyMongo
from env import env

app = Flask(__name__)

app.config['MONGO_URI'] = env.get('MONGO_URI_LOCAL')
print(env.get('MONGO_URI_LOCAL'))
mongo = PyMongo(app)

