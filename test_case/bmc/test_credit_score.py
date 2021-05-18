from service.login import BMC

__author__ = 'fanxun'
__data__ = "2021-05-14 14:13"

import pytest, allure, xlrd, os, requests
import config
from common.utils.getExcelData import  get_excelData
from common.tools import request_main
from config import BMCConfig


# @allure.feature("信用分")
class TestCreditScore():
    # workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_credit_score_20210513.xlsx')
    # inData = get_excelData(workBook, '信用分', 'creditscore')[0]

    def bmc_login_fixture(self):
        """bmc登录获取token"""

        indata = {"phone": "17822000000",
                  "encodedGesture": "67e6d10010533eed4bbe9659863bf6ee"}
        res = BMC().bmc_login(indata)
        setattr(BMCConfig, 'bmc_token', res[0])
        setattr(BMCConfig, 'bmc_pvt_token', res[1])
        # BMCConfig.headers['Pvt-Token'] = res[1]
        # BMCConfig.headers['Token'] = res[0]
    #
    #     # print('Pvt-Token==========================', res[1])
    #     # print('Token==========================', res[0])

    # @allure.story("信用分")
    # @allure.title("{inData[testPoint]}")
    # @allure.testcase("{inData[yapiAddress]}")
    # @allure.description("url:/auth/login 。。。。")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'creditscore'))
    def test_creditscore(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method  = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        # headers = config.BMCConfig.headers
        # print(expectData)
        #res = requests.post(url = url,headers =headers,json =req_data )
        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=False)
        print(res)
        # assert res['code'] == expectData['code']



if __name__ == '__main__':
    # pytest.main(['-s', '-v', 'test_credit_score.py',
    #              r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    # os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_vehicle_steward_29_39_20210513.xlsx')
    inData = get_excelData(workBook, '出行服务', 'agreevehiclesteward')
    print(inData)
    # TestCreditScore().bmc_login_fixture()
    # TestCreditScore().test_creditscore(inData)

    # res = requests.get('http://testbmcapp.hikcreate.com/credit/myCredit/V2', params={"bCityCode":"520100","bNetTag":"trf_mgt"},
    #                    headers= {
    #     'City-Code': "520100",
    #     'Device-Brand': "vivo",
    #     'Device-Code': "000000001e167ed7000000001e167ed7",
    #     'Device-Model': "vivo vivo X20",
    #     'Device-Name': "vivo+X20",
    #     'Device-Type': "Android",
    #     'Mac': "38:6E:A2:A0:0E:AF",
    #     'mimeType': "application/json",
    #     'Net': "wifi",
    #     'OS-Type': "Android",
    #     'OS-Version': "27",
    #     'Pvt-Token': "eyJhbGciOiJIUzI1NiIsInppcCI6IkRFRiJ9.eNpcjEEKgDAMBP-Ss0hS2kT7CP9Qa8CiVbB6Ev9uD56c0w4sc0MqBTzMaYmHhlPbuGdoIIUTPLEhQ2xZGijXWG_OICFRL4h1sRXnLTrHnccPUmLRSf5em8e-6hCy1k6YctrgeQEAAP__.GcCYQ7-NG3rSDLFUvgRVDS94QpYDBtisEuYSY4V_wAw",
    #     'Resolution': "2034x1080",
    #     'Token': "eTir/N9Z7ddMjuvo8M5MJWRLAWrlJ7pUlUe2+eYszHJumBknucBL6nuzBdYWFTWIpFiiDNjxV7Ehw32usHdd6VMFs0k7Rm70FcoDPkTEvyUkwhnN2GHlnk8nhxKvk3AJFDAj6JLl1Mr9OVj9I6TcjpQTzzyjzZjteIreMsUDwJW0Se+CW/teW+1DE70HDMY+0lrm01ftft627SGVsnr6AqxLF3KF/y+GyxKNrwKO29n8T33RFdWgcHs+fji46E/rBdSxxxJHjyClxnJOIoiU3DxZ/SoyNPn5X3CMGUio6MumAfJSQNh6Onk337G2tMum",
    #     'Version': "2.2.6"
    # })
    # print(res.json())


