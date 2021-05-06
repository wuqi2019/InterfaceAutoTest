# 作者:  taoke
# 时间: 2021/5/6 21:10
# 编码: #coding:utf-8
# 版本:  python3.7

import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main

@allure.epic("营运车企业端")
@allure.feature("登录模块")
class TestLogin():
    workBook = xlrd.open_workbook('../../test_case_data/bmy/bmy_case.xlsx')

    @allure.story("登录")
    @allure.title("登录认证")
    @allure.testcase("http://yapi.hikcreate.com/")
    @allure.description("url:/auth/login 。。。。")
    @pytest.mark.parametrize("inData", get_excelData(workBook,'登录模块', 'Login'))
    def test_login(self,inData):
        url = inData['url']
        method  = inData['method']
        req_data = inData['reqData']
        expectData= inData['expectData']
        headers = inData['headers']

        """处理"""
        authorization = BMY().get_authorization()    #
        headers["Authorization"]=authorization
        # 密码加密
        password_Encrypted = BMY().pwd_encrypted(req_data['password'])
        req_data['password'] = password_Encrypted
        # 获取图片信息
        imageinfo = BMY().get_imageCode(req_data['username'], req_data['password'])
        req_data['imageId'] = imageinfo[0]
        req_data['imageCode'] = imageinfo[1]
        req_data['grant_type']= "passwordImageCode"

        """请求"""
        # res = request_main(f"http://testyun.banmago.com/api{url}", headers, method, req_data)
        res = requests.post(f"http://testyun.banmago.com/api{url}", data=req_data, headers=headers)
        # print(res.json())

        """断言"""
        assert res.json()['code'] == expectData['code']


if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_login.py', '-s', '--alluredir', '../../report/tmp'])
    # # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')