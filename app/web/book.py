# coding:utf-8
from flask import jsonify, app, Blueprint

# 定义蓝图
web = Blueprint('web', __name__);


# 使用蓝图
@web.route("/hello")
def hello():
    return jsonify({"b": 1})
