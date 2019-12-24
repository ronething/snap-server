# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 11:25 
@mail: axingfly@gmail.com

Less is more.
"""

# Flask 入口文件

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
