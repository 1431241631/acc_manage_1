# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 18:04
# @Author  : #
# @File    : Register.py
# @Software: PyCharm
from sanic import Blueprint

from db.models import User
from exceptions.ERRORUSER import USEREXISTED
from response.Response import success

register = Blueprint("reg", url_prefix="/reg")


@register.post("/")
async def reg(request):
    session = request.ctx.session
    data = request.json
    async with session.begin():
        user = User(username=data['username'], password=data['password'], auth="user")
        session.add(user)
        try:
            ret = await session.flush()
        except Exception as e:
            raise USEREXISTED(data['username'])
    return success({"username": data['username']}, msg="注册成功")
