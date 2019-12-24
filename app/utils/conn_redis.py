# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 10:49 
@mail: axingfly@gmail.com

Less is more.
"""

import redis

from app.static import Constant

import json
from json import JSONDecodeError


class ConnRedis:

    def __init__(self, snap_config=None):
        self.__pool = redis.ConnectionPool(host=snap_config.get('redis', 'host'),
                                           port=snap_config.getint('redis', 'port'),
                                           db=snap_config.getint('redis', 'db')
                                           )
        self.redis_cli = redis.StrictRedis(connection_pool=self.__pool)

    def set_value(self, key: str, value: str, expire: int = Constant.REDIS_DEFAULT_EXPIRE_TIME.value) -> bool:
        """
        SET KEY VALUE 参数传入都是字符串
        EXPIRE KEY 超时时间
        :param expire: (单位: 秒/s) 默认过期时间 1h
        :return: bool
        """
        if key is not None and key != '':

            self.redis_cli.set(key, value, ex=expire)

            return True
        else:
            return False

    def get_value(self, key: str) -> str:
        """
        GET KEY 获取 key 的值 result.decode()
        decode() 可以将 byte 转化为 str
        这样中文就不会乱码
        :return: str
        """
        result = self.redis_cli.get(key)
        if result is not None:
            return result.decode()
        else:
            return None

    def get_value_and_del(self, key: str) -> str:
        """
        获取值后顺便删除 达到阅后即焚的效果
        :return: str
        """
        result = self.get_value(key)
        if result is not None:
            # 如果不为空删除这个键
            self.key_del(key)
            return result
        else:
            return None

    def set_dict(self, key: str, value: dict, expire: int = Constant.REDIS_DEFAULT_EXPIRE_TIME.value) -> bool:
        """
        set 字典
        :param expire: 过期时间
        :return: bool
        """
        value = json.dumps(value, ensure_ascii=False)
        return self.set_value(key, value, expire)

    def get_dict(self, key: str) -> dict:
        """
        get 字典
        :param key:
        :return: dict
        """
        try:
            result = self.get_value(key)
            if result is not None:
                result = json.loads(result)
            return result
        except TypeError:
            return None
        except JSONDecodeError:
            return None

    def key_expire(self, name: str, time: int) -> bool:
        """给一个 Key 设置超时时间"""
        return self.redis_cli.expire(name, time)

    def key_del(self, *names) -> int:
        """
        删除一个或多个 KEY
        :return: 返回的 int 类型 表示删除了几个 key
        """
        return self.redis_cli.delete(*names)
