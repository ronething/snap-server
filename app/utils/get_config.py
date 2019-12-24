# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 10:41 
@mail: axingfly@gmail.com

Less is more.
"""

import configparser

from app.static import Constant


def get_config():
    """
    获取 snap_config.conf 配置
    :return: 返回 config -> ConfigParser
    """
    config = configparser.ConfigParser()
    config.read(Constant.SNAP_CONFIG_FILENAME.value)

    return config
