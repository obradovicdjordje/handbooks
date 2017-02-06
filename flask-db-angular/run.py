#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
import random
import string
import json
import mysql.connector

app = Flask(__name__)

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

def token_generator():
    N = 32
    alphabet = string.ascii_lowercase
    alphabet += string.ascii_uppercase 
    alphabet += string.digits
    return ''.join(random.choice(alphabet) for _ in range(N))

# login
@app.route("/api/login", methods=['GET'])
def api_login():
    username = request.args.get('username', None)
    password = request.args.get('password', None)
    if(username==None or password==None):
        return 'error', 404
    con = pool.get_connection()
    cur = con.cursor()
    cur.execute("""SELECT username, password 
                   FROM Users 
                   WHERE username='{0}' AND password='{1}'
                """.format(username, password))
    row = cur.fetchone()
    cur.close()
    con.close()
    if row == None:
        return 'error', 404
    else:
        token = token_generator()
        return token, 200

# get list of all users
@app.route("/api/users", methods=['GET'])
def api_users():
    rez = []
    con = pool.get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM Users LIMIT 100 OFFSET 0")
    rows = cur.fetchall()
    for row in rows:
        ob = {}
        for i, col in enumerate(cur.description):
            ob[col[0]] = row[i]
        rez.append(ob)
    con.close()
    return jsonify(result=rez)

# create user
@app.route("/api/users", methods=['POST'])
def api_users_add():
    #username = request.form.get('inUsername')
    #password = request.form.get('inPassword')
    data = request.data
    usr = json.loads(data)
    con = pool.get_connection()
    cur = con.cursor(buffered=True)
    cur.execute("""
           INSERT INTO Users(Farms_idFarms, username, password)
           VALUES(1, '{0}', '{1}')""".format(usr['username'], usr['password'])
    )
    cur.execute("SELECT LAST_INSERT_ID();")
    id = cur.fetchone()
    con.commit()
    con.close()
    return jsonify(result={'id':id[0]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

