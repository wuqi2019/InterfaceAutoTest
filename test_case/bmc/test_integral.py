__author__ = 'fanxun'
__data__ = "2021-05-14 18:04"

import pytest, allure, xlrd, os
import config
from common.utils.getExcelData import  get_excelData
from common.tools import request_main
from config import BMCConfig


# @allure.feature("积分商城")
# class TestCreditScore():
#     workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_testcase01_20210513.xlsx')
#
#     @allure.story("积分商城")
#     @allure.title("{inData[testPoint]}")
#     @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'Integral'))
#     def test_creditscore(self,inData):
#         url = f"{BMCConfig().host}{inData['url']}"
#         method  = inData['method']
#         req_data = inData['reqData']
#         expectData = inData['expectData']
#         headers = config.BMCConfig.headers
#         #res = requests.post(url = url,headers =headers,json =req_data )
#         res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
#         print(res)
#         assert res['code'] == expectData['code']

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_integral.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')





