import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import encodebytes
import time
import json
import requests




# 加密类
class Encryption:
    def get_md5(self, pwd, salt=None):
        """md5加密成32位小写"""
        md5 = hashlib.md5()
        if salt:
            pwd = pwd + salt
        else:
            pwd = pwd
        if pwd:
            md5.update(pwd.encode('utf-8'))
            # print(md5.hexdigest().lower())
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

    def aes_token(self,token):
        key = "HIKEDL@#"
        m5dkey = Encryption().get_md5(key)
        token_plus_timestamp = token + str(int(round(time.time() * 1000)))
        encrypted_token = Encryption().aes_cipher(m5dkey, token_plus_timestamp)
        return encrypted_token

    def get_token(self, indata):
        url = "http://testbmcapp.hikcreate.com/v1/user/login/gesture"
        header = {"Content-Type": "application/json; charset=utf-8",
                  "device-type": "Android",
                  "device-name": "vivo+X20",
                  "device-model": "vivo vivo X20",
                  "city-code": "520100",
                  "Version": "2.2.0",
                  "Device-Code": "000000001e167ed7000000001e167ed7"}

        res = requests.post(url, json=indata, headers=header)
        print(res.json())
        encrypted_token = Encryption().aes_token(res.json()["data"]["token"])
        print(encrypted_token)
        # 获取专网token
        header1 = header.copy()
        header1["Token"] = encrypted_token
        resp = requests.get("http://testbmcapp.hikcreate.com/token", headers=header1)
        print(resp.json())
        pvt_token = resp.json()["data"]["token"]
        print(pvt_token)
        return encrypted_token,pvt_token



if __name__ == '__main__':
    Encryption().get_md5('fx123456', 'hikcreate_xj')
