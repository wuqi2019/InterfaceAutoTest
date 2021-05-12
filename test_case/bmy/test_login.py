# 作者:  taoke
# 时间: 2021/5/6 21:10
# 编码: #coding:utf-8
# 版本:  python3.7

import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BmyConfig


@allure.epic("营运车企业端")
@allure.feature("登录模块")
class TestLogin():
    workBook = xlrd.open_workbook(f'{BmyConfig.root_path}/test_case_data/bmy/bmy_case.xlsx')

    @allure.story("登录")
    @allure.title("登录认证")
    @allure.testcase("http://yapi.hikcreate.com/")
    @allure.description("url:/auth/login 。。。。")
    @pytest.mark.parametrize("inData", get_excelData(workBook,'登录模块', 'Login'))
    def test_login(self,inData):
        url = f"{BmyConfig().test_host}{inData['url']}"
        method  = inData['method']
        req_data = inData['reqData']
        expectData= inData['expectData']
        headers = inData['headers']

        """处理"""
        req_data['grant_type'] = "passwordImageCode"                         # 请求体中的固定值
        authorization = BMY().get_authorization()                            # 获取当前时间戳的Authorization
        headers["Authorization"] = authorization
        password_Encrypted = BMY().pwd_encrypted(req_data['password'])       # 密码加密
        req_data['password'] = password_Encrypted
        imageinfo = BMY().get_imageCode(req_data['username'], req_data['password'])     # 获取图片信息
        req_data['imageId'] = imageinfo[0]
        req_data['imageCode'] = imageinfo[1]

        # """请求"""
        # res = request_main(url, headers, method, req_data)
        # # print(res)
        # """断言"""
        # assert res['code'] == expectData['code']


        """ 请求和断言若不使用通用方法"""
        res = requests.post(f"http://testyun.banmago.com/api{url}", data=req_data, headers=headers)
        print("我是headers",headers)
        print("我是data",req_data)
        print(res.json())
        assert res.json()['code'] == expectData['code']

    def teardown_class(self):
        """清除"""

if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_login.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')
