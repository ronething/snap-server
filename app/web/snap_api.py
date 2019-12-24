# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 13:41 
@mail: axingfly@gmail.com

Less is more.
"""

from flask.views import MethodView

from flask import request

from app.utils.utils import Utils
from app.utils.return_jsonify import R
from app import redis_cli


class SnapAPI(MethodView):
    def get(self, uuid=None):
        """
        get 方法返回链接的内容 阅后即焚
        :param uuid: 注意这里进来的类型是 UUID 所以在 传入 get_value_and_del 的时候需要 str(uuid)
        :return:
        """
        if uuid is not None:
            result = redis_cli.get_value_and_del(str(uuid))
            # print(result)
            if result is not None:
                return R.ok(data=dict(
                    text=result
                ))
            else:
                return R.not_found()
        return R.not_found()

    def post(self):
        """
        post 生成一条 uuid 记录然后将 text 插入 redis
        :return:
        """
        # ⚠️ 从 vue axios 过来的要用 request.json 获取到
        # print(request.json)
        text = request.json.get('text')
        if text is not None:
            uuid = Utils.get_uuid()
            redis_cli.set_value(uuid, text)
            return R.ok(data=dict(
                uuid=uuid
            ))
        else:
            return R.bad_request()
