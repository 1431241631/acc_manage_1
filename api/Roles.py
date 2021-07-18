# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 14:46
# @Author  : #
# @File    : Roles.py
# @Software: PyCharm
from sanic import Blueprint
from db.models import Roles
from sqlalchemy import select, and_
from exceptions.ERRORACC import ACCADDERROR, ACCSISNONE
from response.Response import success

roles = Blueprint("roles", url_prefix="/roles")


@roles.post("/get_roles")
async def get_roles(request):
    """
    查询角色
    :param request: 包含gid的JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(Roles).where(Roles.gid == data['gid'])
        result = await session.execute(stmt)
        rol = result.scalar()
        if not rol:
            raise ACCSISNONE("暂无角色")
    return success(rol.to_dict())


@roles.post("/add_roles")
async def add_roles(request):
    """
    添加角色
    :param request: 包含gid和data的JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        game = Roles(gid=data['gid'], data=data['data'])
        session.add(game)
        try:
            ret = await session.flush()
            print(ret)
        except Exception as e:
            print(e)
            raise ACCADDERROR(data['data'])
    return success(game.to_dict(), msg="添加成功")


@roles.post("/update_roles")
async def update_roles(request):
    """
    添加角色
    :param request: 包含gid和data的JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(Roles).where(Roles.gid == data['gid'])
        result = await session.execute(stmt)
        roles_ = result.scalar()
        if not roles_:
            raise ACCSISNONE(data['gid'])
        roles_.data = data['data']
        await session.flush()
    return success(roles_.to_dict(), msg="更新成功")
