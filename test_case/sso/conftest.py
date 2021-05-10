__author__ = 'fanxun'
__data__ = "2021-05-08 10:26"
import pytest
from config import SSOConfig
from service.login import SSOLogin


@pytest.fixture(scope='module', autouse=True)
def sso_login():
    """SSO登录获取token"""
    sso_token = SSOLogin().sso_login(url=SSOConfig.sso_url)
    setattr(SSOConfig, 'sso_token', sso_token)