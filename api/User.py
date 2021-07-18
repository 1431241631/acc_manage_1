# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 10:52
# @Author  : #
# @File    : User.py
# @Software: PyCharm
from sanic import Blueprint
from db.models import Account, User_Game
from sqlalchemy import select, and_
from exceptions.ERRORACC import ACCADDERROR, ACCSISNONE, ACCSISEXED
from response.Response import success

user = Blueprint("user", url_prefix="/user")


@user.post("/list_user_game")
async def list_user_game(request):
    """
    查询用户对应权限游戏
    :param request:
    :return:
    """
    session = request.ctx.session
    user = request.ctx.user
    async with session.begin():
        stmt = select(User_Game).where(User_Game.uid == user['uid'])
        result = await session.execute(stmt)
        user_game = result.all()
        # print(user_game)
        ret = [i[0].to_dict() for i in user_game]
        if not ret:
            raise ACCSISNONE("暂无权限")
    return success(ret)


@user.post("/search_aid")
async def search_aid(request):
    """
    查找帐号
    :param request: aid的JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(Account).where(Account.aid == data['aid'])
        result = await session.execute(stmt)
        acc = result.scalar()
        acc = acc.to_dict(False)
        # print(acc)
        if not acc:
            raise ACCSISNONE("暂无帐号")
    return success(acc)


@user.post("/search_number")
async def search_number(request):
    """
    查找帐号
    :param request: aid的JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(Account).where(Account.number == data['number'])
        result = await session.execute(stmt)
        acc = result.scalar()
        acc = acc.to_dict(False)
        # print(acc)
        if not acc:
            raise ACCSISNONE("暂无帐号")
    return success(acc)


@user.post("/extract_number")
async def extract_number(request):
    """
    提取帐号
    :param request: aid的JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    user = request.ctx.user
    async with session.begin():
        stmt = select(Account).where(Account.number == data['number'])
        result = await session.execute(stmt)
        acc = result.scalar()
        # print(acc)
        ret = acc.to_dict(True)
        # print(ret)
        if not ret:
            raise ACCSISNONE("暂无帐号")
        if ret['uid'] != 1:
            raise ACCSISEXED("帐号已被提取")
        stmt = select(User_Game).where(User_Game.uid == user['uid'])
        result = await session.execute(stmt)
        gids = result.all()
        # print(gids)
        if len(gids) <= 0:
            raise ACCSISNONE("无游戏代理权限")
        ls = []
        for i in gids:
            ls.append(i[0].to_dict()['gid'])
        if ret in ls:
            acc.uid = user['uid']
            await session.flush()
    return success(ret)


@user.post("/extract")
async def extract(request):
    """
    提取帐号
    :param request: aid的JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    user = request.ctx.user
    async with session.begin():
        stmt = select(Account).where(Account.aid == data['aid'])
        result = await session.execute(stmt)
        acc = result.scalar()
        ret = acc.to_dict(True)
        # print(ret)
        if not ret:
            raise ACCSISNONE("暂无帐号")
        if ret['uid'] != 1:
            raise ACCSISEXED("帐号已被提取")
        stmt = select(User_Game).where(User_Game.uid == user['uid'])
        result = await session.execute(stmt)
        gids = result.all()
        if len(gids) <= 0:
            raise ACCSISNONE("无游戏代理权限")
        ls = []
        for i in gids:
            ls.append(i[0].to_dict()['gid'])
        if ret in ls:
            acc.uid = user['uid']
            await session.flush()
    return success(ret)
