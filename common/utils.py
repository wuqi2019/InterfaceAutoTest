import requests
import json
from config import BaseConfig

class RedisBase:
    pass

def dingTalk(webhook, message):
    """发送消息到钉钉群"""
    data = {'msgtype': 'text', 'text': {"content": message},
            'at': {'isAtAll': True}}
    post_data = json.dumps(data)
    response = requests.post(webhook, headers=BaseConfig.headers, data=post_data)
    return response.text







aaaaaa
aaaaaa
21323213
12321321
1233213
123321
135123