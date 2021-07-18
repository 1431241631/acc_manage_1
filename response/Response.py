# -*- coding: utf-8 -*-
# @Time    : 2021/4/24 9:53
# @Author  : #
# @File    : Response.py
# @Software: PyCharm
from sanic import json


def success(data, code=200, msg='success'):
    res = {
        "code": code,
        "msg": msg,
        "data": data
    }
    return json(res)


def error(code=500, msg='error'):
    res = {
        "code": code,
        "msg": msg
    }
    return json(res, headers={"Access-Control-Allow-Origin": "*"})
