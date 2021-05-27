__author__ = 'fanxun'
__data__ = "2021-05-14 18:04"

import pytest, allure, xlrd, os
import config
from common.utils.getExcelData import  get_excelData
from common.tools import request_main
from config import BMCConfig


@allure.feature("积分商城")
class TestIntegral():
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

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
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        other_expected_data = inData['otherExpectData']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        if not test_pre_get_sign_integral:  # 已经签到过
            assert res['code'] == other_expected_data['code']
        else:
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_pre_task_integral(self):
        """查询待领取积分清单"""
        url = f"{BMCConfig().host}/integral/center/recommendedTasks"
        method = 'get'
        req_data = None
        headers = None
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        return res['data']['list']

    @allure.story("领取积分")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56436")
    @allure.description("/integral/task/receive")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.usefixtures('test_pre_task_integral')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'receiveIntegral'))
    def test_receive_integral(self, inData, test_pre_task_integral):
        case_num = inData['caseNum']
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        for task in test_pre_task_integral:
            if task['status'] == 2 and case_num == 'receiveIntegral001':  # 2表示可领取
                req_data['taskCode'] = task['taskCode']
                break
            elif task['status'] != 2 and case_num == 'receiveIntegral001':
                expectData['code'] = 1006
                break
            elif task['status'] != 2 and case_num == 'receiveIntegral002':
                req_data['taskCode'] = task['taskCode']
                break
            else:
                break
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_pre_list_integral(self):
        """获取商品；列表"""
        url = f"{BMCConfig().host}/integral/mall/goods/list"
        method = 'get'
        req_data = {"pageSize":"20","pageIndex":"1","sortType":"0"}
        headers = None
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        return res['data']

    @allure.story("兑换商品接口")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/56085")
    @allure.description("/integral/mall/goods/exchange")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '积分商城', 'exchangeIntegral'))
    def test_exchange_integral(self, inData, test_pre_list_integral):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        case_num = inData['caseNum']
        count = 0

        for good in test_pre_list_integral['list']:
            if case_num != 'exchangeIntegral002' and case_num != 'exchangeIntegral003':
                if good['status'] == 1:
                    req_data['id'] = good['id']
                    count += 1
                    break
        if count == 0:
            if case_num == 'exchangeIntegral002':  # 说明没有可兑换的商品
                expectData['code'] = 1005
            else:
                expectData['code'] = 1006
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
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
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_integral.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')





