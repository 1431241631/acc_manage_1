# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 9:32
# @Author  : #
# @File    : exceotionHandle.py
# @Software: PyCharm
from sanic import Sanic, json
from response.Response import error
from sanic_cors import CORS

app = Sanic.get_app("secondhand", force_create=True)

print("error")


@app.exception(Exception)
async def catch_anything(request, exception):
    print(exception)
    return error(msg=str(exception))
