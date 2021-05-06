#coding:utf-8

class BaseConfig():
    """基础配置类"""
    # 请求头
    headers = {'Content-Type': 'application/json'}
    # 当前运行的产品名
    current_product = ""
    webhook = ''
    salt = 'hikcreate_xj'


class BMCConfig(BaseConfig):
    """斑马信用app的配置类1111"""
    pass

