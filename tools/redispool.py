# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 9:49
# @Author  : #
# @File    : redispool.py
# @Software: PyCharm
import os
import aioredis
from config import DB_Config

REDIS_DICT = dict(
    IS_CACHE=True,
    REDIS_ENDPOINT=DB_Config['Redis']['host'],
    REDIS_PORT=6379,
    REDIS_PASSWORD=DB_Config['Redis']['password'],
    DB=0,
    POOLSIZE=10,
)

url = f'redis://:{DB_Config["Redis"]["password"]}@r-bp1a4a9e8158ad84pd.redis.rds.aliyuncs.com/'

url_api = f'redis://:{DB_Config["Redis"]["password"]}@r-bp1a4a9e8158ad84pd.redis.rds.aliyuncs.com/1'


class RedisSession:
    """
    建立redis连接池
    """
    _pool = None
    _pool_api = None

    async def get_redis_pool(self):
        if not self._pool:
            self._pool = await aioredis.create_redis_pool(url)

        return self._pool

    async def get_redis_pool_api(self):
        if not self._pool_api:
            self._pool_api = await aioredis.create_redis_pool(url_api)

        return self._pool_api


redis_session = RedisSession()
redis_pool = redis_session.get_redis_pool
redis_pool_api = redis_session.get_redis_pool_api

