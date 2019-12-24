# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 10:33 
@mail: axingfly@gmail.com

Less is more.
"""

from flask import Flask

from app.utils.get_config import get_config
from app.utils.conn_redis import ConnRedis
from app.utils.return_jsonify import R
from app.static import Constant

snap_config = get_config()
redis_cli = ConnRedis(snap_config)


def create_app():
    """
    工厂函数 返回 Flask application 实例
    :return:
    """
    app = Flask(__name__, static_folder=Constant.STATIC_FOLDER.value, template_folder=Constant.TEMPLATE_FOLDER.value)
    register_blueprint(app)

    @app.errorhandler(404)
    def not_found(error):
        return R.not_found()

    return app


def register_blueprint(app):
    """
    注册蓝图
    :param app:
    :return:
    """
    from app.web import web
    app.register_blueprint(web)
