import pytest
import requests

from config import BaseConfig
from common.utils.encryption import Encryption
# from common.utils.getExcelData import get_excelData
from common.tools import request_main

@pytest.fixture(scope='session')
def sso_login(url, headers, method, data):
    """SSO登录"""
    req_data = {"loginName":"fanxun","password":"fx123456"}
    password = req_data['password']
    md5_password = Encryption().get_md5(password, salt=BaseConfig.salt)
    req_data['password'] = md5_password
    res = request_main(url, headers, method, req_data)
    print(res)



def bmy_login():
    """企业云登录"""
    """kkkk"""
    pass


if __name__ == '__main__':
    # login = request_main(url=r'http://testtbdzj.hikcreate.com/web/auth/users/login',
    #                      method='post',
    #                 data={"loginName":"fanxun","password":"d67fac1d71943576b6c397d0cca166cb"},
    #                 headers=getattr(BaseConfig, 'headers'))
    sso_login(r'http://testtbdzj.hikcreate.com/web/auth/users/login',
              headers=getattr(BaseConfig, 'headers'),
              method='post',
              data=None)
