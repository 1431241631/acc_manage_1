# -*- coding: utf-8 -*-
# @Time    : 2021/5/1 15:52
# @Author  : #
# @File    : ERRORCOMMENT.py
# @Software: PyCharm
class COMMENTISNULLERROR(Exception):
    '''
    评论为空
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},评论为空"


class COMMENTADDERROR(Exception):
    '''
    评论失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},评论失败"


class COMMENTDELERROR(Exception):
    '''
    评论删除失败
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},评论删除失败"
