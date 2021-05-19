#作者: taoke
#时间: 2021/5/19 10:52
#编码: -- coding: utf-8 --
#版本: !python3.7
import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BaseConfig,BMCConfig
from service.login import BMC
from common.db import RedisString,MYSQL

"""环境初始化和清除"""
# 1.headers获取
headers = BMCConfig.headers
headers['Pvt-Token'] = BMCConfig.bmc_pvt_token
headers['Token'] = BMCConfig.bmc_token

@allure.epic("信用权益")
class TestCreditRight():
    workBook = xlrd.open_workbook(f'{BaseConfig.root_path}/test_case_data/bmc/bmc_credit_right_2021513.xlsx')

    @allure.story("未激活用户信用权益获取")
    @allure.link('http://yapi.hikcreate.com/project/31/interface/api/74396', name='点我看接口文档')
    @allure.description("/creditRight/v2/index")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'creditRightIndex'))
    def test_creditRightIndex(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     """请求"""
    #     res = request_main(url, headers, method, req_data)
    #     """断言"""
    #     assert res['code'] == expectData['code']
        pass

