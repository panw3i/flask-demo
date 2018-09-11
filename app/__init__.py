#coding:utf-8
from flask import Flask


def create_app():

    app = Flask(__name__)

    # 载入配置文件
    app.config.from_object('config')

    register_blueprint(app)

    return app


def register_blueprint(app):

    from app.web import web

    # 注册蓝图
    app.register_blueprint(web)