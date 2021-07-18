# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 14:49
# @Author  : #
# @File    : ERRORORDER.py
# @Software: PyCharm
class ORDERADDERROR(Exception):
    '''
    订单添加失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},订单添加失败"


class ORDERISNONE(Exception):
    '''
    订单查询失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},订单查询失败"
