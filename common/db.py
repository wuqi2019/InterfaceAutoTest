import redis,pymysql

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


# mysql类
class MYSQL:
    """
    对pymysql的简单封装
    """
    def __init__(self, host, port,user, pwd, db):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        """
        得到连接信息
        返回: conn.cursor()
        """
        self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                    password=self.pwd, database=self.db, charset="utf8")
        cur = self.conn.cursor()
        return cur

    def ExecuQuery(self,sql):
        """
        执行查询语句
        返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段

        调用示例：
                ms = MYSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()        #查询所有,得到列表 [(1,2,3),(1,2,3),(1,2,3)]
        # resList = cur.fetchone()      # 查询一个，得到1个(不用这个)

        #查询完毕后必须关闭连接
        self.conn.close()
        return resList

    def ExecuNonQuery(self,sql):
        """
        执行非查询语句

        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        cur = self.__GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()




if __name__ == '__main__':
    # r= RedisString(6).get('bmc:captcha:bf46c0c0-11b4-4b7d-99d7-530f77f8ab88')
    # r = RedisString(0).get('edl:sms_value:17822000010:MOBILE_REGISTER')
    # print(r)
    # print(str(r)[-7:-1])

    pass