# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 12:06 
@mail: axingfly@gmail.com

Less is more.
"""

from flask import jsonify

from app.static import StatusCode


class R:
    """
    返回 json 数据类
    """

    def __init__(self):
        pass

    @classmethod
    def custom(cls, code=None, message=None, data=None):
        """
        传入自定义的状态码 code message data
        :param code:
        :param message:
        :param data:
        :return: dict
        """
        cls.code = code
        cls.message = message
        cls.data = data

        return jsonify(dict(
            code=cls.code,
            message=cls.message,
            data=cls.data
        ))

    @staticmethod
    def ok(data=None):
        """
        200 OK
        :param data:
        :return:
        """
        return jsonify(dict(
            code=StatusCode.OK.value.get('code'),
            message=StatusCode.OK.value.get('message'),
            data=data
        ))

    @staticmethod
    def bad_request():
        return jsonify(StatusCode.BadRequest.value)

    @staticmethod
    def not_found():
        """
        404 Not Found
        :return:
        """
        return jsonify(StatusCode.NotFound.value)
