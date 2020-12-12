"""
1、键操作

"""

import redis
import time

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
redis = redis.Redis(connection_pool=pool)

# print(r['name'])

# redis.set('visit_count', 0)
#
# print(redis['visit_count'])
#
# redis.incr('visit_count')
# print(redis['visit_count'])

def demo_append():
    redis.append('name', ' 111')


# demo_append()

def hash_hset():
    redis.hset('hash1', 'k1', 'v1')
    redis.hset('hash1', 'k2', 'v2')

    print(redis.hkeys('hash1'))

hash_hset()