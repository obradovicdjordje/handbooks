from __future__ import print_function # In python 2.7
import sys

from flask_restful import reqparse, abort, Resource
from flask import request
import json
from model import User

def log(message):
    print(message, file=sys.stderr)

class UsersList(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']
        self.table_name = 'Users'

    # get all
    def get(self):
        token = request.headers.get('auth-token')
        for p in request.headers:
            log(p)
        if(token != '123'):
            return '', 404
        return User(self.db).find_all()

    # create new
    def post(self):
        data = request.data
        
        usr = json.loads(data)

        username = usr['username']
        password = usr['password']
        con = self.db.get_connection()
        cur = con.cursor(buffered=True)
        cur.execute("""
               INSERT INTO Users(Farms_idFarms, username, password)
               VALUES(1, '{0}', '{1}')""".format(username, password)
        )
        cur.execute("SELECT LAST_INSERT_ID();")
        id = cur.fetchone()
        con.commit()
        con.close()
        usr['idUsers'] = id[0]
        return usr, 202

class Users(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']
        self.table_name = 'Users'

    # get by id
    def get(self, id):
        return 'error', 404
    # update by id
    def put(self, id):
        return '', 201
    # delete by id
    def delete(self, id):
        return '', 204

class UsersLogin(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']
        self.table_name = 'Users'

    # get user by username, passwd
    def get(self):
        args = request.args
        user = {
                'username': args['username'],
                'password': args['password']
        }
        if user != None:
            return "Login "+user['username']+" "+user['passwd'];
        else:
            abort(404, message="User doesn't exists'")
            return 404
