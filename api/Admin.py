# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 9:59
# @Author  : #
# @File    : Admin.py
# @Software: PyCharm
from sanic import Blueprint
from db.models import Account, Game, User_Game
from sqlalchemy import select, and_, delete
from exceptions.ERRORACC import ACCADDERROR, ACCSISNONE
from response.Response import success

admin = Blueprint("admin", url_prefix="/admin")


@admin.post("/add_acc")
async def add_acc(request):
    """
    添加帐号
    :param request: 帐号JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        acc = Account(uid=1, number=data['number'], goods=data['goods'], info_hidden=data['info_hidden'],
                      img=data['img'], info_show=data['info_show'], price=data['price'], gid=data['gid'])
        session.add(acc)
        try:
            ret = await session.flush()
            # print(ret)
        except Exception as e:
            # print(e)
            raise ACCADDERROR(str(e))
    return success(acc.to_dict(True), msg="添加成功")


@admin.post("/del_acc")
async def del_acc(request):
    """
    删除帐号
    :param request: aid JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = delete(Account).where(Account.aid == data['aid'])
        result = await session.execute(stmt)
        await session.flush()
    return success(data['aid'], msg="删除成功")


@admin.post("/del_acc_number")
async def del_acc_number(request):
    """
    删除帐号
    :param request: aid JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = delete(Account).where(Account.number == data['number'])
        result = await session.execute(stmt)
        await session.flush()
    return success(data['number'], msg="删除成功")


@admin.post("/add_game")
async def add_game(request):
    """
    添加游戏
    :param request: 游戏JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        game = Game(game=data['game'])
        session.add(game)
        try:
            ret = await session.flush()
            # print(ret)
        except Exception as e:
            # print(e)
            raise ACCADDERROR(data['game'])
    return success(game.to_dict(), msg="添加成功")


@admin.post("/update_game")
async def update_game(request):
    """
    更新游戏信息
    :param request: 游戏json
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(Game).where(Game.gid == data['gid'])
        result = await session.execute(stmt)
        game = result.scalar()
        # print(game.to_dict())
        if not game:
            raise ACCSISNONE(data['gid'])
        game.game = data['game']
        await session.flush()
    return success(game.to_dict())


@admin.post("/update")
async def update(request):
    """
    更新帐号
    :param request: 帐号JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(Account).where(Account.aid == data['aid'])
        result = await session.execute(stmt)
        acc = result.scalar()
        # print(acc.to_dict(show_hidden=True))
        if not acc:
            raise ACCSISNONE(data['aid'])
        for item in data.keys():
            if item == 'aid':
                continue
            if hasattr(acc, item):
                acc.__setattr__(item, data[item])
        await session.flush()
    return success(acc.to_dict(show_hidden=True))


@admin.post("/update_number")
async def update_number(request):
    """
    更新帐号
    :param request: 帐号JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(Account).where(Account.number == data['number'])
        result = await session.execute(stmt)
        acc = result.scalar()
        # print(acc.to_dict(show_hidden=True))
        if not acc:
            raise ACCSISNONE(data['number'])
        for item in data.keys():
            if item == 'aid' or item == 'number':
                continue
            if hasattr(acc, item):
                acc.__setattr__(item, data[item])
        await session.flush()
    return success(acc.to_dict(show_hidden=True))


@admin.post("/set_user_game")
async def set_user_game(request):
    """
    设置代理游戏权限
    :param request: gid
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        user_game = User_Game(gid=data['gid'], uid=data['uid'])
        session.add(user_game)
        try:
            ret = await session.flush()
            # print(ret)
        except Exception as e:
            # print(e)
            raise ACCADDERROR(data['uid'])
    return success(data=data, msg="设置成功")
