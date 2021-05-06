#coding:utf-8

import json
import logging
import requests
from config import BaseConfig


def request_main(url, headers, method, data):
    """封装requests的通用请求方法"""
    res = None
    if headers == None or headers == {}:
        # 如果传的headers为空，使用通用headers
        headers = BaseConfig.headers
    header_content_type = headers["Content-Type"]

    try:
        if method.upper() == "GET":
            res = requests.get(url=url, headers=headers, params=data)
        elif method.upper() == "POST":
            if header_content_type in ["application/x-www-form-urlencoded"]:
                res = requests.post(url=url, headers=headers, data=data)
            elif header_content_type == "application/json":
                res = requests.post(url=url, headers=headers, data=json.dumps(data))
    except Exception as e:
        logging.log(str(e))
        raise Exception

    if res != None:
        return res.json()
    return res