#作者: taoke
#时间: 2021/5/8 11:43
#编码: -- coding: utf-8 --
#版本: !python3.7
from service.login import BMY
from config import BmyConfig
import pytest

@pytest.fixture(scope='module', autouse=True)
def bmy_login():
    """BMY登录获取token"""
    res = BMY().bmy_login(BmyConfig.test_name_password)
    header = {"Authorization": res,"Content-Type":"application/json"}
    setattr(BmyConfig,'header', header)
