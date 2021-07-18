# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 16:55
# @Author  : #
# @File    : ERRORUSER.py
# @Software: PyCharm

'''
关于用户异常
'''


class USERNAMEORPASSWORDERROR(Exception):
    '''
    帐号或密码错误异常
    '''

    def __init__(self, msg=''):
        self._mgs = msg

    def __str__(self):
        return f"{self._mgs},帐号或密码错误"


class USEREXISTED(Exception):
    '''
    用户已经存在异常
    '''

    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return f"{self._msg},用户已经存在"


class NOTLOGIN(Exception):
    '''
    token错误
    '''

    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return f"{self._msg},身份异常,请重新登录"


class ERRORPermission(Exception):
    '''
        权限错误
    '''

    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return f"{self._msg},权限不足"
