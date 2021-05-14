#作者: taoke
#时间: 2021/5/13 18:59
#编码: -- coding: utf-8 --
#版本: !python3.7

#
import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BaseConfig,BMCConfig
from service.login import BMC



@allure.epic("电子证照")
@allure.feature("电子驾驶证")
class TestDrivingLicense():
    workBook = xlrd.open_workbook(f'{BaseConfig.root_path}/test_case_data/bmc/bmc_testcase01_20210513.xlsx')


    @allure.story("二维码详情")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/81596")
    @allure.description("/dlVeh/qr")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook,'电子证照', 'dlVehqr'))
    def test_dlVehQr(self,inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        """断言"""
        assert res['code'] == expectData['code']

    @allure.story("获取驾驶证图片状态")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/22758")
    @allure.description("/drivingLicense/image/status")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'LicimageStatus'))
    def test_LicimageStatus(self,inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        """断言"""
        assert res['code'] == expectData['code']

    @allure.story("照片审核状态")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/22759")
    @allure.description("/drivingLicense/image/audit/status")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'imaAuditStatus'))
    def test_imaAuditStatus(self,inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        """断言"""
        assert res['code'] == expectData['code']

    @allure.story("图像上传页文案")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/22762")
    @allure.description("/drivingLicense/image/text")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'LicenimageText'))
    def test_LicenimageText(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        """断言"""
        assert res['code'] == expectData['code']

    @allure.story("修改驾驶证头像")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/22750")
    @allure.description("/drivingLicense/avatar/update")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'LicenAvaUpdate'))
    def test_LicenAvaUpdate(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        """断言"""
        assert res['code'] == expectData['code']

    @pytest.mark.scoreDetail
    @allure.story("驾照扣分记录")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/5332")
    @allure.description("/drivingLicense/score/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'scoreDetail'))
    def test_scoreDetail(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        """断言"""
        assert res['code'] == expectData['code']

    def teardown_class(self):
        """清除"""



if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据  '-m','scoreDetail' ,
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_ ElectronicLicense.py', '-s','-m','scoreDetail' , '--alluredir','../../report/tmp'])
    # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')
