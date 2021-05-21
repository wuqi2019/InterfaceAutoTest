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
        otherExpectData= inData['otherExpectData']

        if inData['frontInterface'] == "未激活":
            res = request_main(url, self.noActiveheaders, method, req_data,has_token=True)
            allure.attach("{0}".format(res), "未激活用例结果1")
            assert res['data']['creditInfo']['creditLevelName'] ==otherExpectData['data']['creditInfo']['creditLevelName']
            assert res['code'] == expectData['code']

        else:
            """请求"""
            res = request_main(url, headers, method, req_data)
            allure.attach("{0}".format(res), "用例结果2")
            assert res['code'] == expectData['code']

    @allure.story("信用权益主页")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/45856")
    @allure.description("/creditRight/home")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'creditRightHome'))
    def test_creditRightHome(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        if inData['frontInterface'] == "未激活":
            """请求"""
            res = request_main(url, self.noActiveheaders, method, req_data, has_token=True)
            allure.attach("{0}".format(res), "用例结果1")
            assert res['code'] == expectData['code']
        else:
            """请求"""
            res = request_main(url, headers, method, req_data)
            allure.attach("{0}".format(res), "用例结果2")
            assert res['code'] == expectData['code']


    @allure.story("保持和提升信用分")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/45860")
    @allure.description("/creditRight/howToUpgrade")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'howToUpgrade'))
    def test_howToUpgrade(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        if inData['frontInterface'] == "未激活":
            """请求"""
            res = request_main(url, self.noActiveheaders, method, req_data, has_token=True)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']
        else:
            """请求"""
            res = request_main(url, headers, method, req_data)
            """断言"""
            assert res['code'] == expectData['code']

    @allure.story("文章详情")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/8110")
    @allure.description("/article/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'articleDetail'))
    def test_articleDetail(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        if inData['frontInterface'] == "未激活":
            """请求"""
            res = request_main(url, self.noActiveheaders, method, req_data, has_token=True)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']
        else:
            """请求"""
            res = request_main(url, headers, method, req_data)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']

    @allure.story("所有信用权益")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74916")
    @allure.description("/creditRight/v2/all")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'creditRightAll'))
    def test_creditRightAll(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("预约通行")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/44512")
    @allure.description("/plantrip/getUpdateTimeInfo")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'plantripInfo'))
    def test_plantripInfo(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("预约通行")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/20971")
    @allure.description("/plantrip/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'plantripList'))
    def test_plantripList(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("预约通行")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/20992")
    @allure.description("/plantrip/plantripList")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'plantripListRecord'))
    def test_plantripListRecord(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("预约通行")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/21510")
    @allure.description("/plantrip/myPlantrip")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'myPlantrip'))
    def test_myPlantrip(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("信用优享日")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/23278")
    @allure.description("/activity/creditMan/introduce")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'creditMan'))
    def test_creditMan(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("拜尔口腔")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78246")
    @allure.description("/creditRight/baiEr/creditRightDescription")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'baiErRightDescription'))
    def test_baiErRightDescription(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("拜尔口腔")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78344")
    @allure.description("/creditRight/baiEr/isReceiveRight")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'isReceiveRight'))
    def test_isReceiveRight(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("拜尔口腔")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78236")
    @allure.description("/creditRight/baiEr/receiveRight")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'receiveRight'))
    def test_receiveRight(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("车辆评估")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78668")
    @allure.description("/creditRight/carValuation/creditRightDescription")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用权益', 'carValuation'))
    def test_carValuation(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']




if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据  '-m','scoreDetail' ,
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_creditRight.py', '-s',  '--alluredir','../../report/tmp'])
    os.system('allure serve ../../report/tmp')
