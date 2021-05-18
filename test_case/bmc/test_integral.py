__author__ = 'fanxun'
__data__ = "2021-05-14 18:04"

import pytest, allure, xlrd, os
import config
from common.utils.getExcelData import  get_excelData
from common.tools import request_main
from config import BMCConfig


@allure.feature("积分商城")
class TestCreditScore():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_integral_20210513.xlsx')

    @allure.story("查询我的积分")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55860")
    @allure.description("/integral/center/myIntegral")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'myIntegral'))
    def test_my_integral(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method  = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']


    @allure.story("查询我的签到情况")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55869")
    @allure.description("/integral/center/sign")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'getsignIntegral'))
    def test_get_sign_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']
        return res['data']['canSignInToday']

    @pytest.fixture()
    def test_pre_get_sign_integral(self):
        """签到前置用例"""
        url = f"{BMCConfig().host}/integral/center/sign"
        method = 'get'
        req_data = None
        headers = None
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        return res['data']['canSignInToday']

    @allure.story("签到")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55878")
    @allure.description("/integral/center/sign")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.usefixtures('test_pre_get_sign_integral')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'postSignIntegral'))
    def test_post_sign_integral(self, inData, test_pre_get_sign_integral):
        if not test_pre_get_sign_integral:
            pytest.skip(msg="今天已经进行签到过，此用例不执行")
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("查询待领取积分清单")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55887")
    @allure.description("/integral/center/recommendedTasks")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'taskIntegral'))
    def test_task_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        self.task_list = res['data']['list']
        assert res['code'] == expectData['code']

    @allure.story("查询积分商品")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/57138")
    @allure.description("/integral/center/integralGoods")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'goodsIntegral'))
    def test_goods_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("查询积分规则")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/64302")
    @allure.description("/integral/center/rule")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'ruleIntegral'))
    def test_rule_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("设置签到提醒开关")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56418")
    @allure.description("/integral/center/sign/warnSwitch")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'switchIntegral'))
    def test_switch_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("任务中心主页")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56427")
    @allure.description("/integral/task/info")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'infoIntegral'))
    def test_info_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("领取积分")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56436")
    @allure.description("/integral/task/receive")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'receiveIntegral'))
    def test_receive_integral(self, inData):
        case_num = inData['caseNum']
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        for task in self.task_list:
            if task['status'] == 2 and case_num == 'receiveIntegral001':  # 2表示可领取
                req_data['taskCode'] = task['taskCode']
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
                break
            elif task['status'] != 2 and case_num == 'receiveIntegral002':
                req_data['taskCode'] = task['taskCode']
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
                break
            else:
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
                break
        assert res['code'] == expectData['code']

    @allure.story("获取关注信息")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56841")
    @allure.description("/integral/task/getFollowInfo")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'FollowInfoIntegral'))
    def test_follow_info_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("商城中的商品")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/55896")
    @allure.description("/integral/mall/goods/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'listIntegral'))
    def test_list_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("商品的详情")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56076")
    @allure.description("/integral/mall/goods/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'detailIntegral'))
    def test_detail_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("兑换商品接口")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56085")
    @allure.description("/integral/mall/goods/exchange")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'exchangeIntegral'))
    def test_exchange_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("查询商品的适用门店列表")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56094")
    @allure.description("/integral/mall/goods/applicableStores")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'applicableStoresIntegral'))
    def test_applicable_stores_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("查询兑换记录")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56103")
    @allure.description("/integral/mall/exchangeRecord/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'exchangeRecordListIntegral'))
    def test_exchange_record_list_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("查询兑换记录详情")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/57354")
    @allure.description("/integral/mall/exchangeRecord/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'exchangeRecordDetailIntegral'))
    def test_exchange_record_detail_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @allure.story("关注成功回调")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/61233")
    @allure.description("/integral/task/focusSuccess")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'focusSuccessIntegral'))
    def test_focus_success_integral(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']
if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_integral.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')





