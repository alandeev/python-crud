from flask import Flask, jsonify, request
from models import db, UserModel, TaskModel
from flask_cors import CORS

from utils import httpResponse

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
  db.create_all()

# LIST
@app.get("/users")
def index():
  users = UserModel.query.all()    
  return httpResponse(users)


# CREATE
@app.post("/users")
def create():
  try:
    username = request.json['username']
    user = UserModel.query.filter_by(username=username).first()
    if(user):
      responseError = { "message": "username already exist"}
    
      return httpResponse(responseError, 400)

    user = UserModel(username=username)
    db.session.add(user)
    db.session.commit()

    return httpResponse(user, 201)
  except Exception as e:
    print(e)
    responseObject = { "message": "internal server error" }

    return httpResponse(responseObject, 500)

# READ
@app.get('/users/<string:id>')
def get(id):
  user = UserModel.query.filter_by(id=id).first()
  if(not user):
    responseError = { "message": "User not found" }
    return httpResponse(responseError, 404)

  return httpResponse(user)


# UPDATE
@app.put('/users/<string:id>')
def update(id):
  user = UserModel.query.filter_by(id=id).first()
  if(not user):
    responseError = { "message": "User not found"}
  
    return httpResponse(responseError, 400)
    
  user.username = request.json['username']
  db.session.commit()

  return httpResponse(user, 200)

# DELETE
@app.delete('/users/<string:id>')
def delete(id):
  user = UserModel.query.filter_by(id=id).first()
  if(not user):
    responseError = { "message": "User not found"}
  
    return httpResponse(responseError, 400)

  db.session.delete(user)
  db.session.commit()

  return httpResponse({}, 204)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)