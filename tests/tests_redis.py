# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-01-27 11:10 
@mail: axingfly@gmail.com

Less is more.
"""

from app.utils.conn_redis import ConnRedis
from app.utils.get_config import get_config

import time

snap_config = get_config()

redis_cli = ConnRedis(snap_config=snap_config)

if __name__ == '__main__':
    print(redis_cli.set_value("jiaoyixia", "ronething"))
    time.sleep(1)
    print(redis_cli.get_value("jiaoyixia"))  # ronething
    time.sleep(1)
    print(redis_cli.get_value_and_del("jiaoyixia"))  # ronething
    time.sleep(1)
    print(redis_cli.get_value("jiaoyixia"))  # None
