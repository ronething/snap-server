# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 13:11 
@mail: axingfly@gmail.com

Less is more.
"""

from uuid import uuid4


class Utils:
    """
    字符工具类🔧
    """

    def __init__(self):
        pass

    @staticmethod
    def get_uuid():
        """
        获取 uuid 格式如 'f5754404-6b75-46c6-a396-7b1ae57db100'
        :return:
        """
        return str(uuid4())
