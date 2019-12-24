# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 11:11 
@mail: axingfly@gmail.com

Less is more.
"""

from app.utils.get_config import get_config

snap_config = get_config()

if __name__ == '__main__':
    print(snap_config.get('redis', 'host'))
