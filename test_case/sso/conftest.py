__author__ = 'fanxun'
__data__ = "2021-05-08 10:26"
import pytest
from config import SSOConfig
from common.utils.encryption import Encryption
from common.tools import request_main


@pytest.fixture(scope='module', autouse=True)
def sso_login():
    """SSO登录获取token"""
    encrypted_password = Encryption().get_md5(SSOConfig.sso_password, salt=SSOConfig.sso_salt)
    req_data = {"loginName": SSOConfig.sso_username, "password": encrypted_password}
    res = request_main(SSOConfig.sso_url, headers=None, method='post', data=req_data)
    setattr(SSOConfig, 'sso_token', res['data']['token'])
