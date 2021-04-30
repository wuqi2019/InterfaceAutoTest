import requests,hashlib
import json
from config import BaseConfig
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from base64 import encodebytes

def dingTalk(webhook, message):
    """发送消息到钉钉群"""
    data = {'msgtype': 'text', 'text': {"content": message},
            'at': {'isAtAll': True}}
    post_data = json.dumps(data)
    response = requests.post(webhook, headers=BaseConfig.headers, data=post_data)
    return response.text


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
