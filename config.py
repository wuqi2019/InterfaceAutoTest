#coding:utf-8

class BaseConfig():
    """基础配置类"""
    # 请求头
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    # 当前运行的产品名
    current_product = "bmc"
    default_test_case_dir = "test_case/bmc/"
    salt = 'hikcreate_xj'                       # SSO的登录用的

class BMCConfig(BaseConfig):
    """斑马信用app的配置类"""
    # 测试用例目录
    name = "bmc"
    test_case_dir = "test_case/bmc/"
    test_case_data_dir = "test_case_data/bmc/"
    webhook = ''


