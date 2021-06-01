#作者: taoke
#时间: 2021/5/31 16:34
#编码: -- coding: utf-8 --
#版本: !python3.7

import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BaseConfig,BMCConfig
from service.login import BMC
from common.db import RedisString,MYSQL

# @allure.epic("斑马信用")
@allure.feature("电动车预约")
class TestDrivingLicense():
    workBook = xlrd.open_workbook(f'{BaseConfig.root_path}/test_case_data/bmc/bmc_ElectricBicycle_20210531.xlsx')
    def setup_class(self):
        pass

    @allure.story("“通行证类型”状态")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/19711")
    @allure.description("/pvtapi/deliveryVehicle/passcardTypeState")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'passcardTypeState'))
    def test_passcardTypeState(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("电动车banner接口")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/61377")
    @allure.description("接口：/electric/electricBannerOrPop，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'electricBannerOrPop'))
    def test_electricBannerOrPop(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("电动车banner接口")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/61377")
    @allure.description("接口：/electric/electricBannerOrPop，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'electricBannerOrPop'))
    def test_electricBannerOrPop(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("检测是否领取")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45684")
    @allure.description("接口：/pvtapi/electricBicycle/isBind，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'electricBicycleIsBind'))
    def test_electricBicycleIsBind(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("电动自行车行驶证二维码")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/46554")
    @allure.description("接口：/electricBicycle/qr，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'ElectricBicycleQr'))
    def test_ElectricBicycleQr(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    # @pytest.mark.scoreDetail
    @allure.story("获取须知信息")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/7704")
    @allure.description("接口：/pvtapi/sys/notice/detail，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'noticeDetail'))
    def test_noticeDetail(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  #  '-m','scoreDetail' ,
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_ElectricBicycle.py', '-s', '-m','scoreDetail' , '--alluredir','../../report/tmp'])
    os.system('allure serve ../../report/tmp')
