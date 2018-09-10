#coding:utf-8
from flask import jsonify, app


@app.route("/hello")
def hello():

    return jsonify({"b": 1})
