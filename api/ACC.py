# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 10:08
# @Author  : #
# @File    : ACC.py
# @Software: PyCharm
from sanic import Blueprint
from db.models import Account
from sqlalchemy import select, and_
from exceptions.ERRORACC import ACCADDERROR, ACCSISNONE
from response.Response import success, error

acc = Blueprint("acc", url_prefix="/acc")


@acc.post("/search_goods_gid")
async def search_goods_game(request):
    """
    搜索帐号
    :param request: 包含gid和goods列表的JSON
    :return:
    """
    session = request.ctx.session
    data = request.json
    if len(data['goods']) <= 0:
        return error(msg="请先选择要查询的道具/角色")
    async with session.begin():
        stmt = select(Account).where(and_(Account.gid == data['gid'], Account.uid == 1))
        result = await session.execute(stmt)
        acc = result.all()
        acc = [item[0].to_dict(False) for item in acc]
        # print(acc)
        if not acc:
            raise ACCSISNONE("暂无帐号")
        search_acc = []
        for item in acc:
            goods = item['goods']
            ret = [False for good_search in data['goods'] if good_search not in goods]
            if not ret:
                ret = f"编号：{item['number']}----角色/道具：{','.join(item['goods'])}----价格：{item['price']}----备注：{item['info_show']}"
                search_acc.append({"info": ret, "img": item['img'], "roles": item['goods']})

    return success(search_acc)
