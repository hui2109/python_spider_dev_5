import random

import redis

from settings import *


class HSaveIp:
    def __init__(self):
        self.r = redis.StrictRedis(host=HOST, port=PORT, password=PASSWORD, decode_responses=True)

    def __del__(self):
        self.r.close()

    def zset_zadd(self, ip):
        self.r.zadd(ZSET, {ip: MAX_SCORE})

    def zet_zscore(self, ip):
        return self.r.zscore(ZSET, ip)

    def zset_getip(self):
        ip = self.r.zrangebyscore(ZSET, MAX_SCORE, MAX_SCORE, 0, -1)
        if ip:
            return random.choice(ip)
        else:
            ip = self.r.zrangebyscore(ZSET, MID_SCORE, MAX_SCORE, 0, -1)
            if ip:
                return random.choice(ip)
            else:
                print('实在没有高质量ip了')
                return None

    def zet_zincrby(self, ip):
        score = self.zet_zscore(ip)
        if score > MIN_SCORE:
            self.r.zincrby(ZSET, -1, ip)
        else:
            print('ip:', ip, '低于最低权重，删除')
            self.zet_zrem(ip)

    def zet_zrange(self):
        return self.r.zrange(ZSET, 0, -1)

    def zet_zrem(self, ip):
        self.r.zrem(ZSET, ip)

    def set_randmember(self):
        return self.r.srandmember('User-Agent')
