__author__ = 'fanxun'
__data__ = "2021-05-18 14:41"

import allure, xlrd, pytest
from config import BMCConfig
from common.utils.getExcelData import get_excelData
from common.tools import request_main


@allure.feature("出行服务")
class TestCreditScore():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_vehicle_steward_29_39_20210513.xlsx')

    @allure.story("获取用户授权")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75421")
    @allure.description("/vehicle/steward/authorization/authorizationOfUse")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'authorizationOfUsevehicle_steward'))
    def test_my_integral(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method  = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']