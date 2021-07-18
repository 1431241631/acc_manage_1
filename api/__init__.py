# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 10:22
# @Author  : #
# @File    : __init__.py
# @Software: PyCharm
# 定义了api接口
from sanic import Blueprint
from .Login import login
from .Game import game
from .Admin import admin
from .ACC import acc
from .Register import register
from .User import user
from .Roles import roles

api = Blueprint.group(login, game, admin, acc, register, user, roles, url_prefix='/')
