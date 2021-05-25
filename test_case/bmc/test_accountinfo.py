# 作者:  dengmaosheng
# 时间: 2021/5/13 15:10
# 编码: #coding:utf-8
# 版本:  python3.7
import time

import pytest,allure,xlrd,requests,os

import config
from common.db import MYSQL, RedisString
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BMCConfig


# @allure.feature("账号信息基本功能")
# class TestLogin():
#     workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_login_20210513.xlsx')
#     @allure.story("登录")
#     @allure.severity("")
#     @allure.title("{inData[testPoint]}")
#     @allure.testcase("{inData[yapiAddress]}")
#     @allure.description("url:/auth/login 。。。。")
#     @pytest.mark.parametrize("inData", get_excelData(workBook,'登录', 'login'))
#     def test_login(self,inData):
#         url = f"{BMCConfig().host}{inData['url']}"
#         method  = inData['method']
#         req_data = inData['reqData']
#         expectData = inData['expectData']
#         headers = config.BMCConfig.loginheader
#         res = request_main(url= url,headers = headers,method =method,data = req_data,has_token=True)
#         assert res['code'] == expectData['code']
#
#     @allure.story("激活")
#     @allure.link("")
#     @allure.description("/user/credit/idAuth")
#     @allure.title("{inData[testPoint]}")
#     @pytest.mark.parametrize("inData", get_excelData(workBook, '登录', 'Active'))
#     def test_active(self,inData):
#         url = f"{BMCConfig().host}{inData['url']}"
#         method = inData['method']
#         req_data = inData['reqData']
#         expectData = inData['expectData']
#         headers = config.BMCConfig.headers
#         res = request_main(url=url, headers=headers, method=method, data=req_data)
#         assert res['code'] == expectData['code']


class TestRegister():
    """注册"""
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_base_info_2021513.xlsx')

    def setup_class(self):
    # def test_mysql_result(self):
        """数据库操作"""
        self.ms = MYSQL('10.197.236.190', 3306, 'root', '123456', 'edl_public')
        # 获取账号信息，1577800000 这个账号为注册成功账号
        # self.resList = self.ms.ExecuQuery('SELECT * FROM edl_public.user where phone=1577800000;')
        # self.user_id = resList[0]['id']

    # @allure.story("获取用户登录类型")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10745")
    # @allure.description("/v1/user/login/type")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.flaky(reruns=2)
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'logintypeRegister'))
    # def test_login_type_register(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     phone = req_data['phone']
    #     if not phone:
    #         res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #         assert res['code'] == expectData['code']
    #     else:
    #         resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
    #         if not resList:  # 没有注册过
    #             res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #             assert res['code'] == expectData['code']
    #         else:
    #             user_id = self.resList[0]['id']
    #             self.ms.ExecuNonQuery(
    #                 f'delete from edl_public.user where id={user_id};')

    # @allure.story("获取图形验证码")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/20446")
    # @allure.description("/sys/captcha")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'captchaRegister'))
    # def test_login_type_register(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_picture(self):
        """获取图形验证码"""
        url = f"{BMCConfig().host}/sys/captcha"
        method = 'get'
        req_data = {"bCityCode":"520100","bizType":"1"}
        headers = None
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        return res

    # 有错误 提示图形验证码超时  -- 需要写个获取图形验证码的套件
    @allure.story("图形短信验证码")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10943")
    @allure.description("/v1/user/login/verifyCode/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'verifyCodedetailRegister'))
    def test_login_type_register(self, inData, test_picture):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        casenum = inData['caseNum']

        phone = req_data['phone']
        jtId = test_picture['data']['jtId']
        req_data['jtId'] = jtId
        horPercent = int(RedisString(0).get(f'bmc:captcha:{jtId}'))
        req_data['horPercent'] = horPercent
        if casenum == 'verifyCodedetailRegister006':
            req_data['horPercent'] = None
        elif casenum == 'verifyCodedetailRegister007':
            req_data['horPercent'] = 1
        elif casenum == 'verifyCodedetailRegister008':
            req_data['jtId'] = None
        elif casenum == 'verifyCodedetailRegister009' or casenum == 'verifyCodedetailRegister010':
            time.sleep(60)

        if not phone:
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            # 发送次数过多
            print(res)
            if res['msssage'] == '验证码发送次数过多，请24小时后再试':
                expectData['code'] = 1006
            assert res['code'] == expectData['code']
        else:
            resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
            if not resList:
                res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
                print(res)
                # 发送次数过多
                if res['msssage'] == '验证码发送次数过多，请24小时后再试':
                    expectData['code'] = 1006
                assert res['code'] == expectData['code']
            else:
                user_id = resList[0]['id']
                self.ms.ExecuNonQuery(
                        f'delete from edl_public.user where id={user_id};')

    # 有问题 -- 写个套件 获取短信验证码
    # @allure.story("短信验证")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10787")
    # @allure.description("/user/login/verifyCode")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'loginverifyCodeRegister'))
    # def test_login_type_register(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     phone = req_data['phone']
    #     if not phone:
    #         res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #         assert res['code'] == expectData['code']
    #     else:
    #         resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
    #         if not resList:
    #             res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #             assert res['code'] == expectData['code']
    #         else:
    #             user_id = resList[0]['id']
    #             self.ms.ExecuNonQuery(
    #                     f'delete from edl_public.user where id={user_id};')

    # @allure.story("设置手势-登录")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10974")
    # @allure.description("/v1/user/login/gesture/setAndLogin")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.flaky(reruns=2)
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'gesturesetAndLoginRegister'))
    # def test_login_type_register(self, inData):
    #     url = f"{BMCConfig().host}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     phone = req_data['phone']
    #     if not phone:
    #         res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #         assert res['code'] == expectData['code']
    #     else:
    #         resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
    #         if not resList:
    #             res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #             assert res['code'] == expectData['code']
    #         else:
    #             user_id = resList[0]['id']
    #             self.ms.ExecuNonQuery(
    #                 f'delete from edl_public.user where id={user_id};')


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_accountinfo.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    # os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')

