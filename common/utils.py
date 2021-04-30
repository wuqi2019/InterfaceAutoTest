import redis,hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import encodebytes

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

# 加密类
class Encryption:
    def get_md5(self,pwd):
        """md5加密成32位小写"""
        md5 = hashlib.md5()
        if pwd:
            md5.update(pwd.encode('utf-8'))
            return md5.hexdigest().lower()
        else:
            return ''

    def aes_cipher(self,key, aes_str):
        """AES采用ECB模式，使用PKCS7补偿"""
        aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
        pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')  # 选择pkcs7补全
        encrypt_aes = aes.encrypt(pad_pkcs7)
        # 加密结果
        encrypted_text = str(encodebytes(encrypt_aes), encoding='utf-8')  # 解码
        encrypted_text_str = encrypted_text.replace("\n", "")
        # 此处我的输出结果老有换行符，所以用了临时方法将它剔除
        return encrypted_text_str


if __name__ == '__main__':
    # r= RedisString(6).get('bmc:captcha:bf46c0c0-11b4-4b7d-99d7-530f77f8ab88')
    # r = RedisString(0).get('edl:sms_value:17822000010:MOBILE_REGISTER')
    # print(r)
    # print(str(r)[-7:-1])

    pass