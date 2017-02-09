#!/usr/bin/python
# -*- coding: utf-8 -*-

# only for development
import os
import threading, webbrowser

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
from app.auth.util import USERS

app = Flask(__name__, static_folder='www')
api = Api(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


@app.route('/<path:path>')
def static_file(path):
    try:    
        return app.send_static_file(path)
    except: 
        return "Error"

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.before_request
def before_request():
    request.__setattr__('user', None)
    token = request.headers.get('auth-token')
    if(token != None and token in USERS):
        user = USERS[token]
        request.__setattr__('user', user)

dbconfig = {
    "host": 'rpi3-djordje.local',
    "database": "Agrotrail",
    "user":     "agro",
    "password": "trail"
}

pool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool", pool_size = 3, **dbconfig)

api.add_resource(UsersList, '/api/users', resource_class_kwargs={'db':pool})
api.add_resource(Users, '/api/users/<id>', resource_class_kwargs={'db':pool})
api.add_resource(UsersLogin, '/api/login/', resource_class_kwargs={'db':pool})


if __name__ == "__main__":
    url = "http://localhost:8080"
    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
    app.run(host='0.0.0.0', port=8080, debug=True)
