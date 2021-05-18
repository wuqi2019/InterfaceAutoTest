__author__ = 'fanxun'
__data__ = "2021-05-17 15:11"

import pytest, allure, xlrd, os, random
import config
from common.utils.getExcelData import  get_excelData
from common.tools import request_main
from config import BMCConfig


@allure.feature("三车违法学习")
class TestCreditScore():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_testcase01_20210513.xlsx')
    
    # @allure.story("查询最近成绩")
    # @allure.link("http://yapi.hikcreate.com/project/32/interface/api/67503")
    # @allure.description("/answer/recentGrade")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'recentGradeIllegalstudy'))
    # def test_recentGradeIllegalstudy(self,inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method  = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
    #     assert res['code'] == expectData['code']
    # #
    # @allure.story("获取典型案例视频")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/57606")
    # @allure.description("/illegal/study/video/typicalCase")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'typicalCaseIllegalstudy'))
    # def test_typicalCaseIllegalstudy(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
    #     assert res['code'] == expectData['code']

    @allure.story("获取试卷")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/69573")
    @allure.description("/paper/getPaper")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'getPaperIllegalstudy'))
    def test_get_paper_illegal_study(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_pre_get_paper_illegal_study(self):
        """获取试卷套件"""
        url = f"{BMCConfig().host}/paper/getPaper"
        method = 'get'
        req_data = None
        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=False)
        topic_lists = res['data']['topicList']

        browsequestion = {}
        choosequestion = {}
        browsequestion['answerId'] = res['data']['answerId']
        choosequestion['answerId'] = res['data']['answerId']

        for item in topic_lists:
            if item['topicType'] == 2 and len(browsequestion) == 1:  # 浏览题
                browsequestion['topicId'] = item['topicId']
                browsequestion['topicType'] = item['topicType']
            elif item['topicType'] == 1 and len(choosequestion) == 1:
                choosequestion['topicId'] = item['topicId']
                choosequestion['topicType'] = item['topicType']
        return browsequestion, choosequestion

    @allure.story("提交答案")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/67473")
    @allure.description("/paper/submitAnswer")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.usefixtures('test_pre_get_paper_illegal_study')
    @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'submitAnswerIllegalstudy'))
    def test_submitAnswerIllegalstudy(self, inData, test_pre_get_paper_illegal_study):
        browsequestion, choosequestion = test_pre_get_paper_illegal_study
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        req_data['answerId'] = browsequestion['answerId']
        req_data['topicId'] = browsequestion['topicId']
        req_data['topicType'] = browsequestion['topicType']
        expectData = inData['expectData']
        case_num = inData['caseNum']
        if case_num == 'submitAnswerIllegalstudy001':
            req_data['answerId'] = browsequestion['answerId']
            req_data['topicId'] = browsequestion['topicId']
        elif case_num == 'submitAnswerIllegalstudy002':
            req_data['answerId'] = browsequestion['answerId']
            while True:
                topic_id = random.randint(1, 100)
                if topic_id != browsequestion['topicId']:
                    req_data['topicId'] = topic_id
                    break
        elif case_num == 'submitAnswerIllegalstudy003':
            req_data['topicId'] = browsequestion['topicId']
            while True:
                answer_id = random.randint(1, 100)
                if answer_id != browsequestion['answerId']:
                    req_data['answerId'] = answer_id
                    break
        elif case_num == 'submitAnswerIllegalstudy004':
            req_data['answerId'] = browsequestion['answerId']
            req_data['topicId'] = browsequestion['topicId']
            req_data['topicType'] = 1
        elif case_num == 'submitAnswerIllegalstudy005':
            req_data['answerId'] = choosequestion['answerId']
            req_data['topicId'] = choosequestion['topicId']

        res = request_main(url=url, headers=None, method=method, data=req_data, has_token=False)
        assert res['code'] == expectData['code']

    # @allure.story("查询成绩（只有错题）")
    # @allure.link("http://yapi.hikcreate.com/project/32/interface/api/67485")
    # @allure.description("/answer/detail")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'detailIllegalstudy'))
    # def test_detailIllegalstudy(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("查询答题记录列表")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/67497")
    # @allure.description("/answer/logList")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'logListIllegalstudy'))
    # def test_logListIllegalstudy(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("答题记录查询")
    # @allure.link("http://yapi.hikcreate.com/project/32/interface/api/67491")
    # @allure.description("/answer/log")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '三车违法学习', 'logIllegalstudy'))
    # def test_logIllegalstudy(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     res = request_main(url=url, headers=None, method=method, data=req_data, has_token=True)
    #     assert res['code'] == expectData['code']

if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_illegalstudy.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')





