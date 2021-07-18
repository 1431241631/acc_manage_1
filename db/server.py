# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 15:18
# @Author  : #
# @File    : server.py
# @Software: PyCharm
# ./server.py
from sanic import Sanic
from sqlalchemy.ext.asyncio import create_async_engine
from contextvars import ContextVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from config import DB_Config

app = Sanic.get_app("secondhand", force_create=True)
url = f"mysql+aiomysql://{DB_Config['Mysql']['username']}:{DB_Config['Mysql']['password']}@{DB_Config['Mysql']['host']}/{DB_Config['Mysql']['name']}"
bind = create_async_engine(url, echo=True)

_base_model_session_ctx = ContextVar("session")


@app.middleware("request")
async def inject_session(request):
    request.ctx.session = sessionmaker(bind, AsyncSession, expire_on_commit=False)()
    request.ctx.session_ctx_token = _base_model_session_ctx.set(request.ctx.session)


@app.middleware("response")
async def close_session(request, response):
    if hasattr(request.ctx, "session_ctx_token"):
        _base_model_session_ctx.reset(request.ctx.session_ctx_token)
        await request.ctx.session.close()
