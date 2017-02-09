from __future__ import print_function # In python 2.7
import sys

from flask_restful import reqparse, abort, Resource
from flask import request
from flask_restful_swagger import swagger

import json

from model import User

from app.auth.util import token_generator
from app.auth.util import USERS
from app.auth.util import login_required

def log(message):
    print(message, file=sys.stderr)


class UsersList(Resource):
    def __init__(self, **kwargs):
        self.db = kwargs['db']
        self.table_name = 'Users'

    # get all
    @login_required
    @swagger.operation(
        notes='get all users',
        nickname='get',
        parameters=[
            {
              "name": "auth-token",
              "required": True,
              "allowMultiple": False,
              "dataType": "string",
              "paramType": "header"
            }],
        responseMessages=[]
        )
    def get(self):
        log('tu sam')
        return User(self.db).find_all()

    # create new
    @login_required
    def post(self):
        """api
            endpoint: /api/users
            method: POST
            params: trtr
        """
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
    @swagger.operation(
        notes='Login rest service',
        nickname='login',
        parameters=[{
              "name": "username",
              "required": True,
              "allowMultiple": False,
              "dataType": str.__name__,
              "paramType": "query"
            },
            {
              "name": "password",
              "required": True,
              "allowMultiple": False,
              "dataType": str.__name__,
              "paramType": "query"
            }
        ],
        responseMessages=[
            {
              "code": 201,
              "message": "Createdtion header"
            },
            {
              "code": 405,
              "message": "Invalid input"
            }
          ]
        )
    def get(self):
        args = request.args
        if('username' not in args or 'password' not in args):
            abort(404, message="User doesn't exists'")
            return 404
        username = args['username']
        password = args['password']

        usr = User(self.db).find_by_username_password(username, password)
        
        if usr != None:
            token = token_generator(usr)
            return token, 200
        else:
            abort(404, message="User doesn't exists'")
            return 404
