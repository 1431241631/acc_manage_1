# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 14:12
# @Author  : #
# @File    : __init__.py.py
# @Software: PyCharm
import yaml
import os

'''
    设置当前工作路径
    如果屏蔽这段代码会导致找不到*.yaml文件
    这取决于导入该包的文件路径
'''
config_file_path = os.path.dirname(__file__)

with open(os.path.join(config_file_path, 'db.yaml')) as f:
    DB_Config = yaml.load(f.read(), Loader=yaml.FullLoader)
