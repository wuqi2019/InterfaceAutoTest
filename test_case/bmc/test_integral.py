__author__ = 'fanxun'
__data__ = "2021-05-14 18:04"

import pytest, allure, xlrd, os
import config
from common.utils.getExcelData import  get_excelData
from common.tools import request_main
from config import BMCConfig


@allure.feature("积分商城")
class TestCreditScore():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_testcase01_20210513.xlsx')

    @allure.story("查询我的积分")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55860")
    @allure.description("/integral/center/myIntegral")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'myIntegral'))
    def test_myintegral(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method  = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("签到")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55878")
    @allure.description("/integral/center/sign")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'postSignIntegral'))
    def test_postsignintegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("查询我的签到情况")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55869")
    @allure.description("/integral/center/sign")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'getsignIntegral'))
    def test_getsignIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("查询待领取积分清单")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55887")
    @allure.description("/integral/center/recommendedTasks")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'taskIntegral'))
    def test_taskIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("查询积分商品")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/57138")
    @allure.description("/integral/center/integralGoods")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'goodsIntegral'))
    def test_goodsIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("查询积分规则")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/64302")
    @allure.description("/integral/center/rule")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'ruleIntegral'))
    def test_ruleIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("设置签到提醒开关")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56418")
    @allure.description("/integral/center/sign/warnSwitch")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'switchIntegral'))
    def test_switchIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("任务中心主页")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56427")
    @allure.description("/integral/task/info")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'infoIntegral'))
    def test_infoIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("领取积分")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56436")
    @allure.description("/integral/task/receive")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'receiveIntegral'))
    def test_receiveIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("获取关注信息")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56841")
    @allure.description("/integral/task/getFollowInfo")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'FollowInfoIntegral'))
    def test_FollowInfoIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']


    @allure.story("商城中的商品")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55896")
    @allure.description("/integral/mall/goods/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'listIntegral'))
    def test_listIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("商品的详情")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56076")
    @allure.description("/integral/mall/goods/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'detailIntegral'))
    def test_detailIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("兑换商品接口")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56085")
    @allure.description("/integral/mall/goods/exchange")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'exchangeIntegral'))
    def test_exchangeIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("查询商品的适用门店列表")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56094")
    @allure.description("/integral/mall/goods/applicableStores")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'applicableStoresIntegral'))
    def test_applicableStoresIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("查询兑换记录")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56103")
    @allure.description("/integral/mall/exchangeRecord/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'exchangeRecordListIntegral'))
    def test_exchangeRecordListIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("查询兑换记录详情")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/57354")
    @allure.description("/integral/mall/exchangeRecord/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'exchangeRecordDetailIntegral'))
    def test_exchangeRecordDetailIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("关注成功回调")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/61233")
    @allure.description("/integral/task/focusSuccess")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'focusSuccessIntegral'))
    def test_focusSuccessIntegral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']
if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_integral.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')





