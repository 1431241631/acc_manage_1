# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 10:56
# @Author  : #
# @File    : Login.py
# @Software: PyCharm
from sanic import Blueprint
from db.models import User
from sqlalchemy import select, and_
from exceptions import USERNAMEORPASSWORDERROR
from response.Response import success

login = Blueprint("login", url_prefix="/login")


@login.post("/")
async def do_login(request):
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(User).where(and_(User.username == data['username'], User.password == data['password']))
        result = await session.execute(stmt)
        user = result.scalar()
        if not user:
            raise USERNAMEORPASSWORDERROR(data['username'])
    data = await user.to_dict(request.app.config.SECRET, 1)
    return success(data)
