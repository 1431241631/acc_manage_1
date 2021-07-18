# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 15:01
# @Author  : #
# @File    : ERRORNOTICE.py
# @Software: PyCharm
class NOTICEADDERROR(Exception):
    '''
    公告添加失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},公告添加失败"


class NOTICECHANGEERROR(Exception):
    '''
    公告修改失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},公告修改失败"

class NOTICEISNULLERROR(Exception):
    '''
    公告为空
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},公告为空"
