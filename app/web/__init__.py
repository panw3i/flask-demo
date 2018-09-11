# coding:utf-8

# 定义蓝图
from flask import Blueprint

web = Blueprint('web', __package__)

from app.web import book
