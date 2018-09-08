# coding:utf-8

from flask import Flask, make_response

# from config import *

app = Flask(__name__)

# 载入配置文件
app.config.from_object('config')


@app.route("/hello")
def hello():
    """
    返回的内容不是普通的字符串,而是包括了响应体
    :return:
    """
    response = make_response('<h1>404?</h1>', 301)
    response.headers = {
        'content-type': "text/plain",
        'location':"http://bing.com"
    }

    return response


# 在生产环境是不会执行的,只是做为uwsgi的一个模块
if __name__ == '__main__':
    # 外网可访问地址
    app.run(host="0.0.0.0", debug=app.config['DEBUG'], port=app.config['PORT'])
