from flask import Flask, Blueprint, request, redirect, render_template, jsonify
from config.db import app, db, ma

#llamamos al modelo de User
from models.datamli import Datamli, DatamliSchema

ruta_user = Blueprint("route_data", __name__)

data_schema = DatamliSchema()
datas_schema = DatamliSchema(many=True)

@ruta_data.route("/datamli", methods=["GET"])
def alldata():
    resultAll = Datamli.query.all()
    respo = datas_schema(resultAll)
    return jsonify(respo)

@ruta_user.route("/registrarUsuario", methods=['POST'])
def registrardato():
    fullname= request.json['fullname']
    email = request.json['email']
    newuser = Users(fullname, email)
    db.session.add(newuser)
    db.session.commit()
    return "Guardado"

@ruta_user.route("eliminarUsuario", methods=['DELETE'])
def eliminarUsuario():
    id = request.json['id'] 
    usuario = Users.query.get(id)    
    db.session.delete(usuario)
    db.session.commit()     
    return jsonify(usuario_schema.dump(usuario))