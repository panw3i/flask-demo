# coding:utf-8

from flask import Flask, make_response, jsonify

# from config import *

from app import create_app

app = create_app();
# 在生产环境是不会执行的,只是做为uwsgi的一个模块
if __name__ == '__main__':
    # 外网可访问地址
    app.run(host="0.0.0.0", debug=app.config['DEBUG'], port=app.config['PORT'])
