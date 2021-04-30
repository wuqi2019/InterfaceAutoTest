import requests
import json
from config import BaseConfig


def dingTalk(webhook, message):
    """发送消息到钉钉群"""
    data = {'msgtype': 'text', 'text': {"content": message},
            'at': {'isAtAll': True}}
    post_data = json.dumps(data)
    response = requests.post(webhook, headers=BaseConfig.headers, data=post_data)
    return response.text