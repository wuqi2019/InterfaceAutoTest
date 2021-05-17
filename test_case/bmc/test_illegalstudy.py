__author__ = 'fanxun'
__data__ = "2021-05-17 15:11"

import pytest, allure, xlrd, os
import config
from common.utils.getExcelData import  get_excelData
from common.tools import request_main
from config import BMCConfig


@allure.feature("三车违法学习")
class TestCreditScore():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_testcase01_20210513.xlsx')
    
    @allure.story("查询最近成绩")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/67503")
    @allure.description("/answer/recentGrade")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'recentGradeIllegalstudy'))
    def test_recentGradeIllegalstudy(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method  = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("获取典型案例视频")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/57606")
    @allure.description("/illegal/study/video/typicalCase")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'typicalCaseIllegalstudy'))
    def test_typicalCaseIllegalstudy(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @pytest.mark.run(order=1)
    @allure.story("获取试卷")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/69573")
    @allure.description("/paper/getPaper")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'getPaperIllegalstudy'))
    def test_getPaperIllegalstudy(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
        topic_lists = res['data']['topicList']
        self.browsequestion = {}
        self.choosequestion = {}
        for item in topic_lists:
            if item['topicType'] == 2:  # 浏览题
                self.browsequestion['topicId'] = item['topicId']
                self.browsequestion['topicType'] = item['topicType']
            elif item['topicType'] == 2:
                self.choosequestion['topicId'] = item['topicId']
                self.choosequestion['topicType'] = item['topicType']

        assert res['code'] == expectData['code']

    @allure.story("提交答案")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/67473")
    @allure.description("/paper/submitAnswer")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'submitAnswerIllegalstudy'))
    def test_submitAnswerIllegalstudy(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("查询成绩（只有错题）")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/67485")
    @allure.description("/answer/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'detailIllegalstudy'))
    def test_detailIllegalstudy(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("查询答题记录列表")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/67497")
    @allure.description("/answer/logList")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'logListIllegalstudy'))
    def test_logListIllegalstudy(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("答题记录查询")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/67491")
    @allure.description("/answer/log")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'logIllegalstudy'))
    def test_logIllegalstudy(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
        assert res['code'] == expectData['code']

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_illegalstudy.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')





