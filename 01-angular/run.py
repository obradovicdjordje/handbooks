#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import url_for
from flask import Response
import json


app = Flask(__name__, static_folder='www')


@app.route('/<path:path>')
def static_file(path):
    try:
        return app.send_static_file(path)
    except:
        return "Error"


@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
