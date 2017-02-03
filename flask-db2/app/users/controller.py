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
        con.close()
        usr['idUsers'] = id[0]
        return usr, 202   

