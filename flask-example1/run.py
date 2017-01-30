#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route("/api/add", methods=['GET'])
def add():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

