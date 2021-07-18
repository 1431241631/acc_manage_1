# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 10:10
# @Author  : #
# @File    : Game.py
# @Software: PyCharm
from sanic import Blueprint
from db.models import Game
from sqlalchemy import select, and_
from exceptions.ERRORGAME import GAMESISNONE
from response.Response import success

game = Blueprint("game", url_prefix="/game")


@game.post("/list_games")
async def list_games(request):
    """
    查询所有游戏种类
    :param request:
    :return:
    """
    session = request.ctx.session
    async with session.begin():
        stmt = select(Game)
        result = await session.execute(stmt)
        goods = result.all()
        goods = [item[0].to_dict() for item in goods]
        print(goods)
        if not goods:
            raise GAMESISNONE(msg="暂时没有游戏")
    return success(goods)


@game.post("/get_game")
async def get_game(request):
    """
    查询游戏
    :param request:
    :return:
    """
    session = request.ctx.session
    data = request.json
    async with session.begin():
        stmt = select(Game).where(Game.gid == data['gid'])
        result = await session.execute(stmt)
        goods = result.scalar()
        print(goods.to_dict())
        if not goods:
            raise GAMESISNONE(msg="暂时没有游戏")
    return success(goods.to_dict())
