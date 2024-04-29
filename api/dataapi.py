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

@ruta_data.route("/registrardato", methods=['POST'])
def registrardato():
    cigaretteday= request.json['cigaretteday']
    habitduration = request.json['habitduration']
    lungcancer= request.json['lungcancer']
    newdata = Datamli(cigaretteday, habitduration,lungcancer)
    db.session.add(newdata)
    db.session.commit()
    return "Guardado"

