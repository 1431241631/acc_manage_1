# -*- coding: utf-8 -*-
# @Time    : 2021/4/26 16:35
# @Author  : #
# @File    : ERRORACC.py
# @Software: PyCharm
class ACCADDERROR(Exception):
    '''
    帐号添加失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},帐号添加失败"


class ACCSISNONE(Exception):
    '''
    帐号查询失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},帐号查询失败"

class ACCSISEXED(Exception):
    '''
    帐号提取失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},帐号提取失败"
