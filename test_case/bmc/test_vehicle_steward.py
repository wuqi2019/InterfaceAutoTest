__author__ = 'fanxun'
__data__ = "2021-05-18 14:41"

import allure, xlrd, pytest, os
from config import BMCConfig,BaseConfig
from common.utils.getExcelData import get_excelData
from common.tools import request_main
from common.db import MYSQL
from service.login import BMC
import requests


@allure.feature("出行服务")
class TestVehicleSteward():

    def setup_class(self):
    # def test_setup_class(self):
        """链接数据库"""
        # 出行服务
        self.ms = MYSQL('10.197.236.190', 3306, 'root', '123456', 'edl_public')
        # self.ms=MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")

        # 获取账号的userId  -- 目前已经在excel中写死为 17822000000 账号的userId
        resList = self.ms.ExecuQuery('SELECT * FROM edl_public.user where phone=17822000000;')
        self.user_id = resList[0]['id']

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

    @pytest.fixture()
    def test_pre_custody(self):
        """开启授权"""
        method = 'post'
        req_data = {"plateType": "02","plateNum": "贵ARR008"}
        headers = None
        url = f"{BMCConfig().host}/vehicle/steward/authorization/agree"
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)

    @allure.story("获取用户授权")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75421")
    @allure.description("/vehicle/steward/authorization/authorizationOfUse")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.run('first')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'authorizationOfUsevehiclesteward'))
    def test_authorization_of_use_vehicle_steward(self, inData, test_pre_info, test_pre_custody):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        try:
            is_auth = test_pre_info['data']['auth']
        except Exception as e:
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            setattr(TestVehicleSteward, 'gasLog', res['data']['gasLog'])
            setattr(TestVehicleSteward, 'trafficFine', res['data']['trafficFine'])
            assert res['code'] == expectData['code']
        else:
            # 开启授权
            test_pre_custody

    @allure.story("更改自动记账")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75191")
    @allure.description("/vehicle/steward/authorization/update")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'gasvehiclesteward'))
    def test_gas_vehicle_steward(self, inData, test_pre_info):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 查询账号对应的id
        resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.vehicle_steward_authorization where user_id={self.user_id};')
        id = resList[0]['id']
        req_data['id'] = id
        try:
            is_auth = test_pre_info['data']['auth']
        except Exception as e:
            if not self.gasLog :
                req_data['gasLog'] = True
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            elif self.gasLog:
                req_data['gasLog'] = False
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']
        else:
            pytest.skip(msg="未开启授权，跳过此用例")

    @allure.story("车辆列表")
    @allure.link("")
    @allure.description("/pvtapi/vehicle/manage/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'listvehiclesteward'))
    def test_list_vehicle_steward(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("更改自动记账")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75191")
    @allure.description("/vehicle/steward/authorization/update")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'trafficFinevehiclesteward'))
    def test_traffic_fine_vehicle_steward(self, inData, test_pre_info):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 查询账号对应的id
        resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.vehicle_steward_authorization where user_id={self.user_id};')
        id = resList[0]['id']
        req_data['id'] = id
        try:
            is_auth = test_pre_info['data']['auth']
        except Exception as e:
            if not self.gasLog :
                req_data['trafficFine'] = True
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            elif self.gasLog:
                req_data['trafficFine'] = False
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']
        else:
            pytest.skip(msg="未开启授权，跳过此用例")

    @allure.story("自动记账")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74446")
    @allure.description("/vehicle/steward/accounts/autoSyncAccounts")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'autoSyncAccountsvehiclesteward'))
    def test_auto_sync_count_vehicle_steward(self, inData, test_pre_info):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        try:
            is_auth = test_pre_info['data']['auth']
        except Exception as e:
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']
        else:
            pytest.skip(msg="未开启授权，跳过此用例")

    @allure.story("更新获取新费用")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75456")
    @allure.description("/vehicle/steward/index/updateLastTime")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'updateLastTimevehiclesteward'))
    def test_update_last_time_vehicle_steward(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("自动记账授权")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74441")
    @allure.description("")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.run('last')
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'agreedisagreevehiclesteward'))
    def test_custody_vehicle_steward(self, inData, test_pre_info):
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        try:
            is_auth = test_pre_info['data']['auth']
            automatic = test_pre_info['data']['automatic']
            if automatic:
                url = f"{BMCConfig().host}/vehicle/steward/authorization/disagree"
            else:
                url = f"{BMCConfig().host}/vehicle/steward/authorization/agree"
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']
        except Exception as e:
            # 清除记录 重新执行此用例
            self.ms.ExecuQuery(
                f'delete from edl_public.vehicle_steward_authorization where user_id={self.user_id};')

@allure.feature("出行服务")
class TestViolationWarn():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_vehicle_steward_40-58_20210513.xlsx')
    def setup_class(self):
        Headers={'City-Code': "520100", 'Device-Brand': "vivo",
                         'Device-Code': "000000001e167ed7000000001e167ed7", 'Device-Model': "vivo vivo X20",
                         'Device-Name': "vivo+X20", 'Device-Type': "Android", 'Mac': "38:6E:A2:A0:0E:AF",
                         'mimeType': "application/json", 'Net': "wifi", 'OS-Type': "Android", 'OS-Version': "27",
                         'Resolution': "2034x1080", 'Version': "2.2.6", 'Pvt-Token': "", 'Token': "", }
        self.headers1 = Headers
        indata = {"phone": "13688468803", "encodedGesture": "d4a68e08430ac8bd3bd497d95cbfa5de"}
        res = BMC().bmc_login(indata)
        self.headers1['Pvt-Token'] = res[1]
        self.headers1['Token'] = res[0]

        self.headers2 = Headers
        indata = {"phone": "15283936302", "encodedGesture": "67e6d10010533eed4bbe9659863bf6ee"} #public   user
        res = BMC().bmc_login(indata)
        self.headers2['Pvt-Token'] = res[1]
        self.headers2['Token'] = res[0]

        self.headers3 = Headers
        indata = {"phone": "19900000001", "encodedGesture": "67e6d10010533eed4bbe9659863bf6ee"}  # public   user
        res = BMC().bmc_login(indata)
        self.headers3['Pvt-Token'] = res[1]
        self.headers3['Token'] = res[0]

        self.headers4 = Headers
        indata = {"phone": "18311111111", "encodedGesture": "67e6d10010533eed4bbe9659863bf6ee"}  # public   user
        res = BMC().bmc_login(indata)
        self.headers4['Pvt-Token'] = res[1]
        self.headers4['Token'] = res[0]


    @allure.story("违法提醒首页")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/55122")
    @allure.description("/violationWarn/vioInfo/round")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'vioInfoRound'))
    def test_vioInfoRound(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']

        """请求"""
        res = request_main(url, self.headers1, method, req_data,has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("违法提醒首页")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/55122")
    @allure.description("/violationWarn/vioInfo/round")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'BvioInfoRound'))
    def test_BvioInfoRound(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']

        """请求"""
        res = request_main(url, self.headers2, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("违法提醒首页")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/55122")
    @allure.description("/violationWarn/vioInfo/round")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'CvioInfoRound'))
    def test_BvioInfoRound(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers3, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("违法类型")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/55104", name='点我看接口文档')
    @allure.description("/violationWarn/vioType/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'vioTypeList'))
    def test_vioTypeList(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']

        """请求"""
        res = request_main(url, self.headers1, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("违法点详情")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/55266", name='点我看接口文档')
    @allure.description("/violationWarn/vioPoint/vehicle/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'vioPointVehicleList'))
    def test_vioPointVehicleList(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']

        """请求"""
        res = request_main(url, self.headers1, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("违法通知")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/55338", name='点我看接口文档')
    @allure.description("/violationWarn/getSwitch")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'violationWarn'))
    def test_vioPointVehicleList(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']

        """请求"""
        res = request_main(url, self.headers1, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("违法提醒去添加车辆")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/55122")
    @allure.description("/violationWarn/vioInfo/round")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'eventData'))
    def test_BvioInfoRound(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers3, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("车管家_首页信息")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74426")
    @allure.description("/vehicle/steward/index/info")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'stewardIndexInfo'))
    def test_stewardIndexInfo(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers3, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("车管家_费用类型")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74431")
    @allure.description("/vehicle/steward/index/expenseType")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'stewardIndexExpenseType'))
    def test_stewardIndexExpenseType(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers3, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("车管家_广告")
    @allure.link("http://yapi.hikcreate.com")
    @allure.description("/banner/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'bannerList'))
    def test_bannerList(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers3, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("车管家_车辆信息")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75256")
    @allure.description("/vehicle/steward/vehicle/vehicleOfUser")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'vehicleOfUser'))
    def test_vehicleOfUser(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers3, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("车管家_完善车辆信息")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74471")
    @allure.description("/vehicle/steward/vehicle/add")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'stewardvehicleAdd'))
    def test_stewardvehicleAdd(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers4, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("车管家_手动记账")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74451")
    @allure.description("/vehicle/steward/accounts/manualBookkeeping,autoCreator:taoke,creator:林静文")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'manualBookkeeping'))
    def test_manualBookkeeping(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers4, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("车管家_记账明细")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/75086")
    @allure.description("/vehicle/steward/vehicle/accountingStatistics")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'accountingStatistics'))
    def test_accountingStatistics(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers4, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("车管家_删除记账明细")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74571")
    @allure.description("/vehicle/steward/accounts/delete")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'accountsDelete'))
    def test_accountsDelete(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """处理"""
        req_data["id"]=int(req_data["id"])
        """请求"""
        res =requests.post(url,data=req_data,headers=self.headers4)
        # res = request_main(url, self.headers4, method, req_data, has_token=True)    # 此接口的content—type实际要用表单才行，所以不用这个
        allure.attach("{0}".format(res.json()), "用例结果")
        assert res.json()['code'] == expectData['code']


    @allure.story("车管家_更新记账明细")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/74461")
    @allure.description("/vehicle/steward/accounts/update")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'accountsUpdate'))
    def test_accountsUpdate(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers4, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("油耗记录概况")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78636")
    @allure.description("/vehicle/steward/petrol/consumption/summarise")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'consumptionSummarise'))
    def test_consumptionSummarise(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers4, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("油耗记录列表")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78646")
    @allure.description("/vehicle/steward/petrol/consumption/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'consumptionList'))
    def test_consumptionList(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers4, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("油耗记录详情")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78640")
    @allure.description("/vehicle/steward/petrol/consumption/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'consumptionDetail'))
    def test_consumptionDetail(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers4, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("删除油耗记录")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78642")
    @allure.description("/vehicle/steward/petrol/consumption/delete")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '出行服务', 'consumptionDelete'))
    def test_consumptionDelete(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        """请求"""
        res = request_main(url, self.headers4, method, req_data, has_token=True)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_vehicle_steward.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report' , '--clean-alluredir'])
    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')

