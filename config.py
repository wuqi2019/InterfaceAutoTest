#coding:utf-8

class BaseConfig():
    """基础配置类"""
    # 请求头
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    # 当前运行的产品名
    name = "auto"
    test_case_dir = "test_case/"
    salt = 'hikcreate_xj'       # SSO 登录的东西
    secs=0.2


class BMCConfig(BaseConfig):
    """斑马信用app的配置类"""
    # 测试用例目录
    name = "bmc"
    test_case_dir = "test_case/bmc/"
    test_case_data_dir = "test_case_data/bmc/"
    webhook = ''


class BmyConfig(BaseConfig):
    """企业云的配置类"""
    name = "bmy"
    test_case_dir = "test_case/bmy/"
    test_case_data_dir = "test_case_data/bmy/"

