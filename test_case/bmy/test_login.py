# 作者:  taoke
# 时间: 2021/5/6 21:10
# 编码: #coding:utf-8
# 版本:  python3.7

import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BmyConfig
from service.login import BMY


@allure.epic("登录模块")
@allure.feature("登录模块")
class TestLogin():
    workBook = xlrd.open_workbook(f'{BmyConfig.root_path}/test_case_data/bmy/bmy_case.xlsx')

    @allure.story("登录")
    @allure.title("登录认证")
    @allure.testcase("http://yapi.hikcreate.com/")
    @allure.description("url:/auth/login 。。。。")
    @pytest.mark.parametrize("inData", get_excelData(workBook,'登录模块', 'Login'))

    def test_login(self, inData):
        res = BMY().bmy_login(inData['reqData'], getToken=False)
        # print(res)
        assert  res['code'] == inData['expectData']['code']


if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_login.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')
