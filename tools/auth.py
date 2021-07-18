# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 11:01
# @Author  : #
# @File    : auth.py
# @Software: PyCharm
from sanic import Sanic, Request
import jwt
import datetime
from tools.redispool import redis_pool, redis_pool_api
from exceptions import NOTLOGIN, ERRORPermission
import json

app = Sanic.get_app("secondhand", force_create=True)

print("auth")


async def JWTencode(data, secret, exist_time: int):
    # data.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=exist_time)})
    token = jwt.encode(data, secret)
    redis_connection = await redis_pool()
    await redis_connection.set(data['username'], token)
    return token


def check_token(request):
    if not request.token:
        return None
    try:
        dejwt = jwt.decode(
            request.token, request.app.config.SECRET, algorithms=["HS256"]
        )
        request.ctx.user = dejwt
    except jwt.exceptions.InvalidTokenError:
        return None
    else:
        return dejwt


@app.on_request
async def check_login(request: Request):
    if request.path.startswith("/html"):
        return
    if request.path.startswith("/umi"):
        return
    if request.path.startswith("/favicon.ico"):
        return
    redis_connection_api = await redis_pool_api()
    res = await redis_connection_api.get("OpenApi", encoding="utf-8")
    open_apis = json.loads(res)
    # 查询当前访问api是否是公开api
    if request.path not in open_apis:
        # 非公开api,检查用户身份
        is_authenticated = check_token(request)
        if is_authenticated:
            # 获取redis链接
            redis_connection = await redis_pool()
            res = await redis_connection.get(is_authenticated['username'], encoding='utf-8')
            if res != request.token:
                raise NOTLOGIN("身份已过期")
        else:
            raise NOTLOGIN("身份验证不通过")
        # 身份验证通过,查看当前用户权限是否符合当前api权限
        auth = is_authenticated['auth']
        api_list = await redis_connection_api.get(auth, encoding="utf-8")
        if request.path not in api_list:
            raise ERRORPermission(is_authenticated['username'])
    else:
        # 公开api,不做处理
        return
