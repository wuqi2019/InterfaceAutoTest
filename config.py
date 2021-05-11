#coding:utf-8
import os

class BaseConfig():
    """基础配置类"""
    # 请求头
    headers = {'Content-Type': 'application/json'}
    # 当前运行的产品名
    current_name = "auto"
    test_case_dir = "test_case/"

    secs=0.1                    # 测试用例间隔运行时间
    test_redis = {"host": "10.197.236.197", "port": 6379, "password": "123456"}
    root_path = os.path.abspath(os.path.dirname(__file__))          # 项目根目录

    # 钉钉相关
    webhook = ''

    # 日志相关
    log_path = r''  # 日志路径


class BMCConfig(BaseConfig):
    """斑马信用app的配置类"""
    # 测试用例目录
    name = "bmc"
    test_case_dir = "test_case/bmc/"
    test_case_data_dir = "test_case_data/bmc/"
    bmc_login_url = "http://testbmcapp.hikcreate.com/v1/user/login/gesture"
    bmc_token = ""  #公网加密token
    bmc_pvt_token = ""  #专网token
    host = "http://testbmcapp.hikcreate.com"  #bmc业务所有URL的host
    #bmc除登录外所有的header
    header = {
        'City-Code': "520100",
        'Device-Brand': "vivo",
        'Device-Code': "000000001e167ed7000000001e167ed7",
        'Device-Model': "vivo vivo X20",
        'Device-Name': "vivo+X20",
        'Device-Type': "Android",
        'Mac': "38:6E:A2:A0:0E:AF",
        'mimeType': "application/json",
        'Net': "wifi",
        'OS-Type': "Android",
        'OS-Version': "27",
        'Pvt-Token': bmc_pvt_token,
        'Resolution': "2034x1080",
        'Token': bmc_token,
        'Version': "2.2.5",
    }
    #注册和注销专用账号


class BmyConfig(BaseConfig):
    """企业云的配置类"""
    name = "bmy"
    test_case_dir = "test_case/bmy/"
    test_case_data_dir = "test_case_data/bmy/"
    # 获取token和密码加密原始密钥
    key = "Jv+h&c0A"
    # 获取token 原始token
    defaultToken = "Basic aHpjcF93ZWI6MTIzNDU2"
    # 测试环境host
    test_host = "http://testyun.banmago.com/api"
    # 登录账号
    test_name_password = {"username": "15151500000", "password": "bmy123456"}
    # 企业云接口的Authorization
    bmy_token = ''
    header = {"Content-Type":"application/json"}


class SSOConfig(BaseConfig):
    """SSO配置类"""
    name = "sso"
    sso_username = 'robot_fanxun'  # SSO登录名
    sso_password = 'fx123456'  # sso密码
    sso_url = r'http://testtbdzj.hikcreate.com/web/auth/users/login'  # sso登录地址
    sso_salt = 'hikcreate_xj'  # SSO盐值
    sso_token = ''
    headers = {'Content-Type': 'application/json'}
