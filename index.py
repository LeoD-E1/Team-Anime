from flask import Flask, render_template, request, jsonify, Response
from templates import db_format
import database
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/video')
def video():
    anime = db_format.anime[0]
    return render_template('video.html', anime = anime)


@app.route('/anime', methods=['GET'])
def get_animes():
    anime = database.mongo.db.anime.find()
    response = json_util.dumps(anime)
    return Response(response, mimetype='application/json')


@app.route('/anime/<id>', methods = ['GET'])
def get_anime(id):
    anime = database.mongo.db.anime.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(anime)
    return Response(response, mimetype='application/json')



@app.route('/users', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    
    if username and email and password:
        hashed_password = generate_password_hash(password)
        id = database.mongo.db.users.insert(
            {'username':username, 'email': email, 'password': hashed_password }
        )
        response = {
            'id': str(id),
            'username': username,
            'email': email,
            'password': hashed_password
        }
        return response
    else:
        return not_found()

@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message':'Resource not found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug = True)