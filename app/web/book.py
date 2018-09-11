# coding:utf-8
from flask import jsonify, app, Blueprint

from . import web


# 使用蓝图
@web.route("/hello")
def hello():
    return jsonify({"b": 1})
