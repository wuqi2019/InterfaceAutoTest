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


    @allure.story("文件上传")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/5452")
    @allure.description("接口：/pvtapi/file/upload，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'fileUpload'))
    def test_fileUpload(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        expectData = inData['expectData']
        """特殊处理"""
        headers = {'City-Code': "520100", 'Device-Brand': "vivo", 'Device-Code': "000000001e167ed7000000001e167ed7",
                   'Device-Model': "vivo vivo X20", 'Device-Name': "vivo+X20", 'Device-Type': "Android",
                   'Mac': "38:6E:A2:A0:0E:AF", 'mimeType': "application/json", 'Net': "wifi", 'OS-Type': "Android",
                   'OS-Version': "27", 'Pvt-Token': f"{BMCConfig.bmc_pvt_token}", 'Resolution': "2034x1080",
                   'Token': f"{BMCConfig.bmc_token}", 'Version': "2.2.6"}
        user_file = {'file': ("321.gif", open(f"{BaseConfig.root_path}/test_case_data/bmc/321.gif", 'rb'), 'image/png/jpg')}
        res = requests.post(url, files=user_file, headers=headers)
        allure.attach(f"{res.json()}", "响应结果", allure.attachment_type.TEXT)
        assert res.json()['code'] == expectData['code']


    @allure.story("获取系统字典")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/5077")
    @allure.description("接口：/pvtapi/sys/dict/list，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'sysDictlist'))
    def test_sysDictlist(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @pytest.mark.scoreDetail
    @allure.story("地址选择")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45572")
    @allure.description("接口：/pvtapi/sys/dict/list，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'addressSelector'))
    def test_addressSelector(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
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
