__author__ = 'dengmaosheng'
__data__ = "2021-05-08 10:26"
import pytest

import config
from config import BMCConfig
from common.utils.encryption import Encryption
import requests

@pytest.fixture(scope='module', autouse=True)
def bmc_login(indata):
    """bmc登录获取token"""
    url = config.BMCConfig.host+"/v1/user/login/gesture"
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
    url = config.BMCConfig.host+"/token"
    resp = requests.get(url=url, headers=header1)
    print(resp.json())
    pvt_token = resp.json()["data"]["token"]
    print(pvt_token)
    setattr(BMCConfig, 'bmc_token', encrypted_token)
    setattr(BMCConfig, 'bmc_pvt_token', pvt_token)
