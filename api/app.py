from flask import Flask, json,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema,fields
from dotenv import load_dotenv
import os

load_dotenv()

USER = os.getenv('db_user')
PWD = os.getenv('db_password')

#Conexion base
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://"+USER+":"+PWD+"@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


db=SQLAlchemy(app)

#Modelo User
class User(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    name=db.Column(db.String(255),nullable=False)
    age=db.Column(db.Integer())
    phone=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return self.name

    #Metodos
    @classmethod
    def get_users(cls):
        return cls.query.all()
    
    @classmethod
    def get_user_by_id(cls,id):
        return cls.query.get_or_404(id)

    def create_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()        

class UsersSchema(Schema):
    id=fields.Integer()
    name=fields.String()
    age=fields.Integer()
    phone=fields.String()

#Retorna todos los usuarios
@app.route('/users',methods=['GET'])
def all_users():
    users=User.get_users()
    serializer=UsersSchema(many=True)
    data=serializer.dump(users)
    return jsonify(
        data
    )

#Crea usuarios
@app.route('/users',methods=['POST'])
def create_user():
    print("entro al post")
    data=request.get_json()
    print("data: ",data)
    new_user=User(
        id=data.get('id'),
        name=data.get('name'),
        age=data.get('age'),
        phone=data.get('phone')
    )
    new_user.create_user()
    serializer=UsersSchema()
    data=serializer.dump(new_user)
    return jsonify(data),201

#Actualiza usuarios
@app.route('/users/<int:id>',methods=['PUT'])
def update_user(id):
    user=User.get_user_by_id(id)
    data=request.get_json()
    user.name=data.get('name')
    user.age=data.get('age')
    user.phone=data.get('phone')
    db.session.commit()
    serializer=UsersSchema()
    user_data=serializer.dump(user)
    return jsonify(user_data),200

#Elimina usuarios
@app.route('/users/<int:id>',methods=['DELETE'])
def delete_user(id):
    user=User.get_user_by_id(id)
    user.delete_user()
    return jsonify({"message":"Deleted"}),204

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
