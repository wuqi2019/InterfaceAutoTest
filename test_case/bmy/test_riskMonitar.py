#作者: taoke
#时间: 2021/5/8 10:39
#编码: -- coding: utf-8 --
#版本: !python3.7

import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BmyConfig
from service.login import BMY
@allure.epic("营运车企业端")
@allure.feature("风控台")
class TestMonitor():
    workBook = xlrd.open_workbook(f'{BmyConfig.root_path}/test_case_data/bmy/bmy_case.xlsx')
    # def setup_class(self):  # 每一个类下面所有的方法调用只运行一次
    #     self.token = BMY().bmy_login(BmyConfig.test_name_password)
    @allure.story("风险列表")
    @allure.severity("critical")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("http://yapi.hikcreate.com/")
    @allure.description("url:/auth/login 。。。。")
    @pytest.mark.parametrize("inData", get_excelData(workBook,'风控台', 'riskMonitorList'))
    def test_login(self,inData):
        url = f"{BmyConfig().test_host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # print(inData['testPoint'])

        """请求"""
        res = request_main(url, headers, method, req_data)

        """断言"""
        assert res['code'] == expectData['code']

    def teardown_class(self):
        """清除"""


if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_riskMonitar.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')
