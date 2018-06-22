from flask import Flask

app = Flask(__name__)

# 路由最小原则
@app.route('/hello')
def hello():
    return 'hello flask!'

app.run()