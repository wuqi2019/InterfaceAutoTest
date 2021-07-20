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

# def dingTalk_markdown(secret,webhook,message):
#     """发送消息到钉钉群"""
#     timestamp = str(round(time.time() * 1000))
#     sign=get_sign(secret)
#     webhook=webhook+f"&timestamp={timestamp}&sign={sign}"
#     now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
#     data = {'msgtype': 'markdown',
#             "markdown": {
#             "title":"接口执行报告",
#             "text": f"#### 接口自动化测试报告  \n> 本消息由Jenkins构建后自动发送\n> \
#             ![screenshot](https://aqjg.gyszhjt.com:60028/img/group1/M00/00/03/Cgs5X2CwRQ-AKCtYAAFAKzUlsWM407.png)\n> ###### 点击查看 >> [斑马信用](http://10.197.236.10:8080/job/bmc/allure/) \n"
#                         },
#             'at': {'isAtAll': False}}
#     post_data = json.dumps(data)
#     response = requests.post(webhook, headers=BaseConfig.headers, data=post_data)
#     return response.text

def dingTalk_markdown2(group):
    for i in group:
        """发送消息到钉钉群（斑马信用）"""
        timestamp = str(round(time.time() * 1000))
        sign=get_sign(i["secret"])
        webhook=i["webhook"]+f"&timestamp={timestamp}&sign={sign}"
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        data = {'msgtype': 'markdown',
                "markdown": {
                "title":"接口执行报告",
                "text": f"#### 接口自动化测试报告  \n> 本消息由Jenkins构建后自动发送\n> \
                ![screenshot](https://aqjg.gyszhjt.com:60028/img/group1/M00/00/03/Cgs5X2CwRQ-AKCtYAAFAKzUlsWM407.png)\n> ###### 点击查看 >> [斑马信用](http://10.197.236.10:8080/job/bmc/allure/) \n"
                            },
                'at': {'isAtAll': False}}
        post_data = json.dumps(data)
        requests.post(webhook, headers=BaseConfig.headers, data=post_data)

def dingTalk_markdown_bmy(group):
    for i in group:
        """发送消息到钉钉群（交委）"""
        timestamp = str(round(time.time() * 1000))
        sign=get_sign(i["secret"])
        webhook=i["webhook"]+f"&timestamp={timestamp}&sign={sign}"
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        data = {'msgtype': 'markdown',
                "markdown": {
                "title":"接口执行报告",
                "text": f"#### 接口自动化测试报告  \n> 本消息由Jenkins构建后自动发送\n> \
                ![screenshot](https://aqjg.gyszhjt.com:60028/img/group1/M00/00/04/Cgs5XWD2NrOACeeHAAhEU1jS9Xc475.png)\n> ###### 点击查看 >> [安全运输](http://10.197.236.10:8080/job/bmy/allure/) \n"
                            },
                'at': {'isAtAll': False}}
        post_data = json.dumps(data)
        requests.post(webhook, headers=BaseConfig.headers, data=post_data)





if __name__ == '__main__':
    test_group =[{"secret":"SEC40a1be4bbd9214e16ba288208fd608b2b590e82e853fa9b24c1850a506c6185b",
                "webhook":"https://oapi.dingtalk.com/robot/send?access_token=e830b05eeee88da31972099e403a74d05ec55719360707dc44e532c0d0b49cb6",
                "group":"自动化测试组 - 技术和思路分享"}
        # ,
        #         {"secret": "SEC1d08f46da74337cc0e1cd5bb9ad19622d825483343fdfa43ce396881e4745bdb",
        #         "webhook": "https://oapi.dingtalk.com/robot/send?access_token=f9e005c1a984b9607960345d38669337b1115d1141a0294e98666443b312115b",
        #         "group": "自动群"}
                 ]
    bmc_group= [{"secret":"SECd10e7eaf4ae5e4a9b15cb059951519c0d8537721fd588e38b861c411ce6442d3",
                "webhook":"https://oapi.dingtalk.com/robot/send?access_token=9755709d67e98f6adfa09c884b2b62480b5315ffb65acde5309094206374e3a1",
                "group":"斑马信用测试"},
                {"secret": "SEC465015385218e70a94f107a16f72dd33d8fc118c3b2a631e0433685302f2fbb3",
                "webhook": "https://oapi.dingtalk.com/robot/send?access_token=229908a83825ed56abbf728d3382e446a4e8a90e9ad302c37a036bcbccbbf9ee",
                "group": "自动化小组"}]
    dingTalk_markdown_bmy(test_group)