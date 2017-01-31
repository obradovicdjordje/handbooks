#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function # In python 2.7
from flask import Flask
from flask import request
from flask import jsonify
import sys
import json

app = Flask(__name__)

def log(message):
    print(message, file=sys.stderr)


@app.route('/<path:path>')
def static_file(path):
    try:    
        return app.send_static_file(path)
    except: 
        return "Error"

@app.route('/')
def root():
    return app.send_static_file('index.html')

users = []

@app.route("/api/form_login", methods=['POST'])
def form_insert():
    email = request.form.get('inputEmail')
    password = request.form.get('inputPassword')
    users.append({'email':email, 'passwd':password})
    return jsonify(result=users)

@app.route("/api/insert", methods=['POST'])
def insert():
    user = request.data
    
    userDict = json.loads(data)
    return jsonify(result=userDict)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

