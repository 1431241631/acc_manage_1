# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 10:14
# @Author  : #
# @File    : ERRORGAME.py
# @Software: PyCharm
class GAMESISNONE(Exception):
    '''
    游戏查询失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},游戏查询失败"
