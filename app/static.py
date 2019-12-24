# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 10:33 
@mail: axingfly@gmail.com

Less is more.
"""

import os

from enum import Enum, unique


@unique
class StatusCode(Enum):
    """
    snap 状态码
    """
    OK = dict(
        code=200,
        message="请求成功",
    )
    BadRequest = dict(
        code=400,
        message="客户端请求的语法错误"
    )
    NotFound = dict(
        code=404,
        message="未找到资源"
    )


@unique
class Constant(Enum):
    """
    snap 常量类
    """

    # snap 配置文件绝对路径
    SNAP_CONFIG_FILENAME = os.path.abspath(os.path.join(os.path.dirname(__file__), 'snap_config.conf'))

    # redis 默认增加/减少 数量值
    REDIS_AMOUNT = 1

    # redis key 默认过期时间 1 hour = 1 * 60 * 60 = 3600 sec
    REDIS_DEFAULT_EXPIRE_TIME = 3600

    # static 静态文件夹
    STATIC_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'dist/static'))

    # template 模版文件夹
    TEMPLATE_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'dist'))


if __name__ == '__main__':
    print(Constant.STATIC_FOLDER.value)
    print(Constant.TEMPLATE_FOLDER.value)
