from service.login import BMC

__author__ = 'fanxun'
__data__ = "2021-05-14 14:13"

import pytest, allure, xlrd, os, requests
import config
from common.utils.getExcelData import  get_excelData
from common.tools import request_main
from config import BMCConfig


@allure.feature("信用分")
class TestCreditScore():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_credit_score_20210513.xlsx')

    @allure.story("信用分详情")
    @allure.link("")
    @allure.description("/credit/myCredit/V2")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'Vcreditscore'))
    def test_v_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("分享信用分")
    @allure.link("")
    @allure.description("/credit/pkCredit/sharePic")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'sharePiccreditscore'))
    def test_share_pic_credit_score(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("历史信用分")
    @allure.link("")
    @allure.description("/credit/record/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'recordlistcreditscore'))
    def test_record_list_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("完善基础信息")
    @allure.link("")
    @allure.description("/credit/base/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'baselistcreditscore'))
    def test_base_list_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("获取履约任务")
    @allure.link("")
    @allure.description("/credit/explore/performance/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'performancelistcreditscore'))
    def test_performance_list_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("身份证信息")
    @allure.link("")
    @allure.description("/credit/detail/idCard")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'idCardcreditscore'))
    def test_idCard_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("驾驶证信息")
    @allure.link("")
    @allure.description("/drivingLicense/image/status")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'imagestatuscreditscore'))
    def test_image_status_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("身份证信息正反面")
    @allure.link("")
    @allure.description("/drivingLicense/image")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'imagecreditscore'))
    def test_image_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("车辆列表")
    @allure.link("")
    @allure.description("/vehicle/manage/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'managelistcreditscore'))
    def test_manage_list_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("我的学历信息")
    @allure.link("")
    @allure.description("/credit/education/getEducationList")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'getEducationListcreditscore'))
    def test_get_education_list_credit_score(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("我的单位信息")
    @allure.link("")
    @allure.description("/credit/work/getWorkList")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'getWorkListcreditscore'))
    def test_get_work_list_credit_score(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("我的车辆信息")
    @allure.link("")
    @allure.description("/vehicle/selection/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'selectionlistcreditscore'))
    def test_selection_list_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("学历认证地区选择")
    @allure.link("")
    @allure.description("/credit/education/provinces")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'provincescreditscore'))
    def test_provinces_credit_score(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("学历单位选择")
    @allure.link("")
    @allure.description("/sys/dict/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'dictlistcreditscore'))
    def test_dict_list_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_get_education(self):
        """获取学历信息"""
        url = f"{BMCConfig().host}/credit/education/getEducationList"
        method = 'get'
        req_data = None
        headers = None
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        return res

    @allure.story("学历认证")
    @allure.link("")
    @allure.description("/credit/education/addEducation")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.usefixtures('test_get_education')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'addEducationcreditscore'))
    def test_add_education_credit_score(self, inData, test_get_education):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        education_list = test_get_education['data']['list']
        for item in education_list:
            if item['school'] == req_data['school']:  # 根据学校来判断是否相同学历
                expectData['code'] = 1006
            else:
                expectData['code'] = 1000
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("删除学历")
    @allure.link("")
    @allure.description("/credit/education/deleteEducation")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.usefixtures('test_get_education')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'deleteEducationcreditscore'))
    def test_delete_education_credit_score(self, inData, test_get_education):
        education_list = test_get_education['data']['list']
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        req_data['id'] = education_list[0]['id']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("新增单位")
    @allure.link("")
    @allure.description("/credit/work/addCompany")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.usefixtures('test_pre_work_info')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'addCompanycreditscore'))
    def test_add_company_credit_score(self, inData, test_pre_work_info):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        company_name = req_data['companyName']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        work_list = test_pre_work_info['data']['list']
        for work in work_list:
            if company_name == work['companyName']:
                expectData['code'] = 1006
            else:
                expectData['code'] = 1000
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_pre_work_info(self):
        """获取单位信息套件"""
        url = f"{BMCConfig().host}/credit/work/getWorkList"
        method = 'get'
        req_data = None
        headers = None
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        return res

    @allure.story("删除单位信息")
    @allure.link("")
    @allure.description("/credit/work/deleteWork")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.usefixtures('test_pre_work_info')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'deleteWorkcreditscore'))
    def test_delete_work_credit_score(self, inData, test_pre_work_info):
        work_id = test_pre_work_info['data']['list'][0]['id']
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        req_data['id'] = work_id
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("驾驶证年审")
    @allure.link("")
    @allure.description("/credit/explore/performance/wait/dl/examine")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'examinecreditscore'))
    def test_examine_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("更换驾驶证本人照片")
    @allure.link("")
    @allure.description("/drivingLicense/image/text")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'imagetextcreditscore'))
    def test_image_text_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("期满换证信息")
    @allure.link("")
    @allure.description("/credit/explore/performance/wait/dl/expire")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'expirecreditscore'))
    def test_expire_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("车辆年检信息")
    @allure.link("")
    @allure.description("/vehicle/selection/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'vehiclelistcreditscore'))
    def test_vehicle_list_credit_score(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @allure.story("添加车辆失败")
    @allure.link("")
    @allure.description("/vehicle/vCode/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '信用分', 'detailcreditscore'))
    def test_detail_credit_score(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_credit_score.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])

    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')

