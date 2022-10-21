import redis

r = redis.StrictRedis(host='localhost', port=6379, password='123456', decode_responses=True, db=0)
# print(r.get('name'))
# print(r.get('age'))

# 批量获取
# print(r.mget('name', 'age'))

# 批量设置
r.mset({'sex': 'male', 'hobby': 'basketball'})
print(r.mget("name", "age", "sex", 'hobby'))
