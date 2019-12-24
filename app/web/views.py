# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 10:35 
@mail: axingfly@gmail.com

Less is more.
"""

from app.web import web
from app import redis_cli

from flask import render_template, request
from flask.views import MethodView

from app.utils.return_jsonify import R
from app.utils.utils import Utils

from app.web.snap_api import SnapAPI


@web.route("/")
def Home():
    return render_template("index.html")


snap_view = SnapAPI.as_view('snap')

web.add_url_rule('/web/<uuid:uuid>', view_func=snap_view, methods=["GET", ])
web.add_url_rule('/web/generate', view_func=snap_view, methods=['POST', ])
