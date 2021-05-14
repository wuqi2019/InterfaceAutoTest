__author__ = 'dengmaosheng'
__data__ = "2021-05-08 10:26"
import pytest
from service.login import BMC
import config
from config import BMCConfig
from common.utils.encryption import Encryption
import requests
# requests
@pytest.fixture(scope='module', autouse=True)
def bmc_login_fixture():
    """bmc登录获取token"""

    indata = {"phone":"17822000000",
            "encodedGesture": "67e6d10010533eed4bbe9659863bf6ee"}
    res = BMC().bmc_login(indata)
    setattr(BMCConfig, 'bmc_token', res[0])
    setattr(BMCConfig, 'bmc_pvt_token', res[1])

