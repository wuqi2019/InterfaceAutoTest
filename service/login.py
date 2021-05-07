import pytest,time
import requests

from config import BaseConfig
from common.utils.encryption import Encryption
# from common.utils.getExcelData import get_excelData
from common.tools import request_main
from common.db import RedisString


@pytest.fixture(scope='session')
def sso_login(url, headers, method, data):
    """SSO登录"""
    req_data = {"loginName":"fanxun","password":"fx123456"}
    password = req_data['password']
    md5_password = Encryption().get_md5(password, salt=BaseConfig.salt)
    req_data['password'] = md5_password
    res = request_main(url, headers, method, req_data)
    print(res)


class BMY():
    """斑马云登录相关"""
    # 获取当前时间的Authorization
    def get_authorization(self,defaultToken="Basic aHpjcF93ZWI6MTIzNDU2"):
        key = "Jv+h&c0A"  # 原始密钥
        m5dkey = Encryption().get_md5(key)  # AES密钥
        t = time.time()
        num = str(round(t * 1000))
        return Encryption().aes_cipher(m5dkey, defaultToken + num)

    """
    ①AES加密  -注 AES 秘钥进行MD5(原始密钥)
    ②MD5
    ③逆序
    """
    def pwd_encrypted(self,pwd):
        key = "Jv+h&c0A"  # 原始密钥
        m5dkey = Encryption().get_md5(key)
        encrypted_text_str = Encryption().aes_cipher(m5dkey, pwd)  # ①
        newpwd = Encryption().get_md5(encrypted_text_str)  # ②
        return newpwd[::-1]  # ③

    # 从redis获取获取图形验证码x轴百分比
    def get_imageCode(self,username, pwd):
        payload = {"username": username, "password": pwd}
        try:
            rep = requests.get("http://testyun.banmago.com/api/website/common/graph/login-captcha", params=payload)
            imageId = rep.json()['data']['jtId']
            result = RedisString(6).get(f'bmc:captcha:{imageId}')
            imageCode = str(result)[-3:-1]
            return imageId, imageCode
        except:
            return ("imageId", "imageCode")  # 返回错误的验证码


    def bmy_login(self,indata, getToken=True):
        """企业云登录"""
        # token加密
        authorization = BMY().get_authorization()
        header = {"Authorization": authorization}
        payload = {"username": "","password": "", "imageId": "", "grant_type": "passwordImageCode", "imageCode": ""}
        # 账号
        payload['username'] = indata['username']

        # 密码加密
        password_Encrypted = BMY().pwd_encrypted(indata['password'])
        payload['password'] = password_Encrypted

        # 获取图片信息
        imageinfo = BMY().get_imageCode(payload['username'], payload['password'])
        payload['imageId'] = imageinfo[0]
        payload['imageCode'] = imageinfo[1]
        # print(payload)

        resp = requests.post("http://testyun.banmago.com/api/auth/login", data=payload, headers=header)
        if getToken:
            token = resp.json()['data']['token']  # 数据权限会藏在token中
            return BMY().get_authorization(defaultToken=token)
        else:
            return resp.json()


    def get_token(self, indata):
        """斑马信用登录获取token"""
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
    # login = request_main(url=r'http://testtbdzj.hikcreate.com/web/auth/users/login',
    #                      method='post',
    #                 data={"loginName":"fanxun","password":"d67fac1d71943576b6c397d0cca166cb"},
    #                 headers=getattr(BaseConfig, 'headers'))
    # sso_login(r'http://testtbdzj.hikcreate.com/web/auth/users/login',
    #           headers=getattr(BaseConfig, 'headers'),
    #           method='post',
    #           data=None)
    indata= {"username":"15150000000","password":"A123456"}
    token= BMY().bmy_login(indata,getToken=False)
    print(token)
