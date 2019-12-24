# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 10:33 
@mail: axingfly@gmail.com

Less is more.
"""

from flask import Blueprint

web = Blueprint("web", __name__)

import app.web.views
