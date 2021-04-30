import redis

# redis类
class RedisBase:
    def __init__(self, inum):
        """每一个数据库实例管理一个连接池"""
        self.num = inum
        pool = redis.ConnectionPool(host='10.197.236.197', port=6379, db=0, password='123456')
        self.r = redis.Redis(connection_pool=pool)

class RedisString(RedisBase):
    def __init__(self, inum):
        RedisBase.__init__(self, inum=inum)
    def get(self, xx):
        """获取值"""
        result = self.r.get(xx)
        return result


if __name__ == '__main__':
    # r= RedisString(6).get('bmc:captcha:bf46c0c0-11b4-4b7d-99d7-530f77f8ab88')
    # r = RedisString(0).get('edl:sms_value:17822000010:MOBILE_REGISTER')
    # print(r)
    # print(str(r)[-7:-1])
    pass