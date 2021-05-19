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
    def setup_class(self):
        self.noActiveheaders = {
            'City-Code': "520100",'Device-Brand': "vivo",'Device-Code': "000000001e167ed7000000001e167ed7",'Device-Model': "vivo vivo X20",'Device-Name': "vivo+X20",'Device-Type': "Android",'Mac': "38:6E:A2:A0:0E:AF",'mimeType': "application/json",'Net': "wifi",'OS-Type': "Android",'OS-Version': "27",'Resolution': "2034x1080",'Version': "2.2.6",
            'Pvt-Token': "", 'Token': "",
        }
        indata = {"phone": f"{BMCConfig.NoactivePhone}",
                  "encodedGesture": "67e6d10010533eed4bbe9659863bf6ee"}
        res = BMC().bmc_login(indata)
        self.noActiveheaders['Pvt-Token'] = res[1]
        self.noActiveheaders['Token'] = res[0]


    @allure.story("信用权益获取")
    @allure.link('http://yapi.hikcreate.com/project/31/interface/api/74396', name='点我看接口文档')
    @allure.description("/creditRight/v2/index")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'creditRightIndex'))
    def test_creditRightIndex(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']

        if inData['frontInterface'] == "未激活":
            res = request_main(url, self.noActiveheaders, method, req_data,has_token=True)
            print("未激活",res)
            assert res['code'] == expectData['code']
        else:
            """请求"""
            res = request_main(url, headers, method, req_data)
            print("---------------------",res)
            """断言"""
            assert res['code'] == expectData['code']


if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据  '-m','scoreDetail' ,
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_creditRight.py', '-s',  '--alluredir','../../report/tmp'])
    # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')
