# 作者:  dengmaosheng
# 时间: 2021/5/13 15:10
# 编码: #coding:utf-8
# 版本:  python3.7

import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BMCConfig


@allure.epic("斑马信用")
@allure.feature("账号信息基本功能")
class TestLogin():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_testcase01_20210513.xlsx')

    @allure.story("账号信息基本功能")
    @allure.severity("")
    @allure.title("登录认证")
    @allure.testcase("http://yapi.hikcreate.com/")
    @allure.description("url:/auth/login 。。。。")
    @pytest.mark.parametrize("inData", get_excelData(workBook,'登录模块', 'Login'))
    def test_login(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method  = inData['method']