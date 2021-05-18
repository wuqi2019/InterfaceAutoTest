__author__ = 'fanxun'
__data__ = "2021-05-18 14:41"

import allure, xlrd, pytest, os
from config import BMCConfig
from common.utils.getExcelData import get_excelData
from common.tools import request_main
from common.db import MYSQL


@allure.feature("出行服务")
class TestVehicleSteward():

    # def setUp_class(self):
    #     """链接数据库"""
    #     # 出行服务
    #     ms = MYSQL('10.197.236.190', 3306, 'root', '123456', 'edl_public')
    #     # 获取账号的userId  -- 目前已经在excel中写死为 17822000000 账号的userId
    #     self.resList = ms.ExecuQuery('SELECT * FROM edl_public.user where phone=17822000000;')

    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_vehicle_steward_29_39_20210513.xlsx')

    # 更改自动记账状态
    gasLog = ''
    trafficFine = ''

    @pytest.fixture()
    def test_pre_info(self):
        """首页套件"""
        url = f"{BMCConfig().host}/vehicle/steward/index/info"
        method = 'get'
        req_data = None
        headers = None
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        return res

    @allure.story("获取用户授权")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75421")
    @allure.description("/vehicle/steward/authorization/authorizationOfUse")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.usefixtures('test_pre_info')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'authorizationOfUsevehiclesteward'))
    def test_authorization_of_use_vehicle_steward(self, inData, test_pre_info):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        try:
            is_auth = test_pre_info['data']['auth']
        except Exception as e:
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            print(res)
            setattr(TestVehicleSteward, 'gasLog', res['data']['gasLog'])
            setattr(TestVehicleSteward, 'trafficFine', res['data']['trafficFine'])
            assert res['code'] == expectData['code']
        else:
            pytest.skip(msg="未开启授权，跳过此用例")

    @allure.story("更改自动记账")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75191")
    @allure.description("/vehicle/steward/authorization/update")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.usefixtures('test_pre_info')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'gasvehiclesteward'))
    def test_my_integral(self, inData, test_pre_info):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # case_num = inData['caseNum']
        try:
            is_auth = test_pre_info['data']['auth']
        except Exception as e:
            if not self.gasLog :
                req_data['gasLog'] = True
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
                print(res)
            elif self.gasLog:
                req_data['gasLog'] = False
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            assert res['code'] == expectData['code']
        else:
            pytest.skip(msg="未开启授权，跳过此用例")


    #
    # @allure.story("车辆列表")
    # @allure.link("")
    # @allure.description("/pvtapi/vehicle/manage/list")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'listvehiclesteward'))
    # def test_my_integral(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("更改自动记账")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75191")
    # @allure.description("/vehicle/steward/authorization/update")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'postvehiclesteward'))
    # def test_my_integral(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("自动记账")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74446")
    # @allure.description("/vehicle/steward/accounts/autoSyncAccounts")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'autoSyncAccountsvehiclesteward'))
    # def test_my_integral(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("更新获取新费用")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75456")
    # @allure.description("/vehicle/steward/index/updateLastTime")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'updateLastTimevehiclesteward'))
    # def test_my_integral(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("不同意开启自动记账")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74441")
    # @allure.description("/vehicle/steward/authorization/disagree")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'disagreevehiclesteward'))
    # def test_my_integral(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("同意开启自动记账")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74436")
    # @allure.description("/vehicle/steward/authorization/agree")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'agreevehiclesteward'))
    # def test_my_integral(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     assert res['code'] == expectData['code']

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_vehicle_steward.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    # os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')