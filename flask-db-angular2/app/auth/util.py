from flask_restful import abort
from functools import wraps
from flask import request
from flask import g

import random
import string

USERS = {}

def token_generator(usr):
    N = 32
    alphabet = string.ascii_lowercase
    alphabet += string.ascii_uppercase 
    alphabet += string.digits
    token = ''.join(random.choice(alphabet) for _ in range(N))
    USERS[token] = usr
    return token

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.user is None:
            abort(404, message="Login required")
            return 404
        return f(*args, **kwargs)
    return decorated_function

