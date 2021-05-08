#coding:utf-8
import os

class BaseConfig():
    """基础配置类"""
    # 请求头
    headers = {'Content-Type': 'application/json'}
    # 当前运行的产品名
    name = "auto"
    test_case_dir = "test_case/"

    secs=0.1                    # 测试用例间隔运行时间
    test_redis = {"host": "10.197.236.197", "port": 6379, "password": "123456"}
    root_path = os.path.abspath(os.path.dirname(__file__))          # 项目根目录

    # 钉钉相关
    webhook = ''

    # SSO相关
    username = 'fanxun'  # SSO登录名
    password = 'fx123456'  # sso密码
    sso_url = r'http://testtbdzj.hikcreate.com/web/auth/users/login'  # sso登录地址
    salt = 'hikcreate_xj'  # SSO盐值


class BMCConfig(BaseConfig):
    """斑马信用app的配置类"""
    # 测试用例目录
    name = "bmc"
    test_case_dir = "test_case/bmc/"
    test_case_data_dir = "test_case_data/bmc/"


class BmyConfig(BaseConfig):
    """企业云的配置类"""
    name = "bmy"
    test_case_dir = "test_case/bmy/"
    test_case_data_dir = "test_case_data/bmy/"
    key = "Jv+h&c0A"                                      # 获取token和密码加密原始密钥
    defaultToken = "Basic aHpjcF93ZWI6MTIzNDU2"           # 获取token 原始token
    # 测试环境
    test_host = "http://testyun.banmago.com/api"
    test_name_password = {"username": "15151500000", "password": "bmy123456"}
    Authorization = ''


