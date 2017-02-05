#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api

from flask import request
from flask import Response
from flask import jsonify
import mysql.connector
import json
import xlwt
import StringIO

from app.users.controller import UsersList
from app.users.controller import Users
from app.users.controller import UsersLogin

app = Flask(__name__, static_folder='www')
api = Api(app)

@app.route('/<path:path>')
def static_file(path):
    try:    
        return app.send_static_file(path)
    except: 
        return "Error"

@app.route('/')
def root():
    return app.send_static_file('index.html')


dbconfig = {
    "host": 'rpi3-djordje.local',
    "database": "Agrotrail",
    "user":     "agro",
    "password": "trail"
}

pool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool", pool_size = 3, **dbconfig)

api.add_resource(UsersList, '/api/users', resource_class_kwargs={'db':pool})
api.add_resource(Users, '/api/users/<id>', resource_class_kwargs={'db':pool})
api.add_resource(UsersLogin, '/api/users/login/', resource_class_kwargs={'db':pool})

@app.route("/getExcel")
def getPlotExcel():
    f = StringIO.StringIO() # create a file-like object 
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('test')

    #  upisivanje u vrstu 3
    sheet.write(3, 1, 'pera1')
    workbook.save(f)
    
    return Response(
        f.getvalue(),
        mimetype="application/xls",
        headers={"Content-disposition": "attachment; filename=sample.xls"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
