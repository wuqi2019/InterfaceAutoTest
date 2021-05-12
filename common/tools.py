#coding:utf-8

import json
import logging
import requests
from config import *


def request_main(url, headers, method, data, has_token=False):
    """封装requests的通用请求方法"""
    res = None
    def request_by_method(method, headers):
        inner_res = None
        try:
            header_content_type = headers["Content-Type"]
        except KeyError:
            header_content_type = headers["mimeType"]

        try:
            if method.upper() == "GET":
                inner_res = requests.get(url=url, headers=headers, params=data)
            elif method.upper() == "POST":
                if header_content_type == "application/json":
                    inner_res = requests.post(url=url, headers=headers, data=json.dumps(data))
                elif header_content_type in ["application/x-www-form-urlencoded"]:
                    inner_res = requests.post(url=url, headers=headers, data=data)
            return inner_res
        except Exception as e:
            # logging.log(str(e))
            raise Exception

    # if headers == None or headers == {} or headers == "":
        # 如果传的headers为空，使用各自产品的通用headers
    headers = build_headers(headers, has_token)
    # print("打印headers",headers)
    try:
        res = request_by_method(method, headers)
    except requests.exceptions.ConnectionError as e:
        logging.log(str(e))
    except requests.exceptions.RequestException as e:
        logging.log(str(e))
    if res != None:
        return res.json()
    return res


def build_headers(headers, has_token):
    name = BaseConfig.current_name
    if has_token:
        return headers
    if name == BMCConfig.name:
        if headers == None or headers == "":
            headers = BMCConfig.headers
        headers['Pvt-Token'] = BMCConfig.bmc_pvt_token
        headers['Token'] = BMCConfig.bmc_token
    elif name == BmyConfig.name:
        if headers == None or headers == "":
            headers = BmyConfig.headers
        headers['Authorization'] = BmyConfig.bmy_token
    elif name == SSOConfig.name:
        if headers == None or headers == "":
            headers = SSOConfig.headers
        headers['token'] = SSOConfig.sso_token
    return headers


def get_case_dir(product_name):
    """根据传入的产品名来运行对应产品的测试用例目录"""
    test_case_dir = BaseConfig.test_case_dir
    if product_name == BMCConfig.name:
        test_case_dir = BMCConfig.test_case_dir
    if product_name == BmyConfig.name:
        test_case_dir = BmyConfig.test_case_dir
    if product_name == SSOConfig.name:
        test_case_dir = SSOConfig.test_case_dir
    return test_case_dir