# 作者:  dengmaosheng
# 时间: 2021/5/13 15:10
# 编码: #coding:utf-8
# 版本:  python3.7

import pytest,allure,xlrd,requests,os

import config
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BMCConfig


@allure.epic("账号信息基本功能")
# @allure.feature("账号信息基本功能")
class TestLogin():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_base_info_2021513.xlsx')
    @allure.story("账号信息基本功能")
    @allure.severity("")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("{inData[yapiAddress]}")
    @allure.description("url:/auth/login 。。。。")
    @pytest.mark.parametrize("inData", get_excelData(workBook,'账号信息基本功能', 'login'))


    def test_login(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method  = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.loginheader
        #res = requests.post(url = url,headers =headers,json =req_data )
        res = request_main(url= url,headers = headers,method =method,data = req_data,has_token=True)
        # print(res)
        assert res['code'] == expectData['code']
if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_accountinfo.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')