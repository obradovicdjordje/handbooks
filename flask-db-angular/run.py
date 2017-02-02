#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify
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

# create users
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
    con.close()
    return jsonify(result={'id':id[0]})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

