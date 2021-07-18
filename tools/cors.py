# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 16:02
# @Author  : #
# @File    : cors.py
# @Software: PyCharm
from typing import Iterable
from sanic import Request


def _add_cors_headers(response, methods: Iterable[str]) -> None:
    allow_methods = list(set(methods))
    if "OPTIONS" not in allow_methods:
        allow_methods.append("OPTIONS")
    headers = {
        "Access-Control-Allow-Methods": ",".join(allow_methods),
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
        "Access-Control-Allow-Headers": (
            "origin, content-type, accept, "
            "authorization, x-xsrf-token, x-request-id"
        ),
    }
    response.headers.extend(headers)


def add_cors_headers(request: Request, response):
    if request.method != "OPTIONS":
        if request.route:
            methods = [
                method
                for methods in request.route.methods
                for method in methods
            ]
            _add_cors_headers(response, methods)
