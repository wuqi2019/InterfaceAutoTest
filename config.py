class BaseConfig():
    """基础配置类"""
    # 请求头
    headers = {'Content-Type': 'application/json; charset=utf-8'}


class DingTalk(BaseConfig):
    """钉钉机器人"""
    webhook = ''


class SSOLoginConfig(BaseConfig):
    """登录配置"""
    salt = 'hikcreate_xj'