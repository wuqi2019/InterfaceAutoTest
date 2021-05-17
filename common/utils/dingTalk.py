import requests,time,hmac,hashlib,base64,urllib.parse,json
from config import BaseConfig
import datetime



def get_sign(secret):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return sign

def dingTalk(secret,webhook,message):
    """发送消息到钉钉群"""
    timestamp = str(round(time.time() * 1000))
    sign=get_sign(secret)
    webhook=webhook+f"&timestamp={timestamp}&sign={sign}"
    data = {'msgtype': 'text', 'text': {"content": message},
            'at': {'isAtAll': True}}
    post_data = json.dumps(data)
    response = requests.post(webhook, headers=BaseConfig.headers, data=post_data)
    return response.text

def dingTalk_link(secret,webhook,message):
    """发送消息到钉钉群"""
    timestamp = str(round(time.time() * 1000))
    sign=get_sign(secret)
    webhook=webhook+f"&timestamp={timestamp}&sign={sign}"
    data = {'msgtype': 'link',
            "link": {
            "text": "这个即将发布的新版本，创始人xx称它为红树林。而在此之前，每当面临重大升级，产品经理们都会取一个应景的代号，这一次，为什么是红树林",
            "title": "Dinding发送消息接口文档",
            "picUrl": "https://aqjg.gyszhjt.com:60028/img/group1/M00/00/03/Cgs5XWCf8QiAeR3KAAA1uImt-QE934.jpg",
            "messageUrl": "https://developers.dingtalk.com/document/app/custom-robot-access"
                     },
            'at': {'isAtAll': True}}
    post_data = json.dumps(data)
    response = requests.post(webhook, headers=BaseConfig.headers, data=post_data)
    return response.text


def dingTalk_markdown(secret,webhook,message):
    """发送消息到钉钉群"""
    timestamp = str(round(time.time() * 1000))
    sign=get_sign(secret)
    webhook=webhook+f"&timestamp={timestamp}&sign={sign}"
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    data = {'msgtype': 'markdown',
            "markdown": {
            "title":"接口执行报告",
            "text": f"#### 接口自动化测试报告  \n> 本消息由Jenkins构建后自动发送\n> \
            ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)\n> ###### {now_time}构建 [斑马信用](http://10.197.236.10:8080/job/bmc/allure/) \n"
                        },
            'at': {'isAtAll': False}}
    post_data = json.dumps(data)
    response = requests.post(webhook, headers=BaseConfig.headers, data=post_data)
    return response.text



if __name__ == '__main__':

    res=dingTalk_markdown(secret="SEC40a1be4bbd9214e16ba288208fd608b2b590e82e853fa9b24c1850a506c6185b",
                 webhook="https://oapi.dingtalk.com/robot/send?access_token=e830b05eeee88da31972099e403a74d05ec55719360707dc44e532c0d0b49cb6",
                 message="我就是我, @XXX 是不一样的烟火")
    print(res)



    # 自动化测试组 - 技术和思路分享 - ----小帅
    # SEC40a1be4bbd9214e16ba288208fd608b2b590e82e853fa9b24c1850a506c6185b
    # https: // oapi.dingtalk.com / robot / send?access_token = e830b05eeee88da31972099e403a74d05ec55719360707dc44e532c0d0b49cb6


