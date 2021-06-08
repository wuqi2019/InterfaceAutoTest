__author__ = 'fanxun'
__data__ = "2021-05-31 16:19"

import xlrd, pytest, allure, os
from config import BMCConfig
from common.utils.getExcelData import get_excelData
from common.tools import request_main


@allure.feature('账号与安全')
class TestAccountAndSecurity():
    """账号与安全"""
    pass
    # workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_account_and_security.xlsx')
    #
    # @allure.story("绘制势密码")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10769")
    # @allure.description("/user/verifyGesture")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'verifyGestureAccountSecurity'))
    # def test_verify_gesture(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("获取图形验证码")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/20446")
    # @allure.description("/sys/captcha")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'captchaAccountSecurity'))
    # def test_captcha(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("拼图校验情况")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10944")
    # @allure.description("/v1/user/login/verifyCode/detail")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'verifyCodedetailAccountSecurity'))
    # def test_verify_code_detail(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("验证码输入")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10943")
    # @allure.description("/user/login/verifyCode")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'loginverifyCodeAccountSecurity'))
    # def test_login_verify_code(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("手势密码修改")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10764")
    # @allure.description("/user/gesture")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'gestureAccountSecurity'))
    # def test_gesture(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("字符密码修改")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/4726")
    # @allure.description("/user/password")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'passwordAccountSecurity'))
    # def test_password(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("旧手机号验证码")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/1492")
    # @allure.description("/user/phone/old/verifyCode")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'oldverifyCodeAccountSecurity'))
    # def test_old_verify_code(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("新手机号验证码")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/4957")
    # @allure.description("/user/phone/new/verifyCode")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'newverifyCodeAccountSecurity'))
    # def test_new_verify_code(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("更换手机号")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/1496")
    # @allure.description("/user/phone")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'phoneAccountSecurity'))
    # def test_phone(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("账号数据找回")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78204")
    # @allure.description("/user/change/binding/verifyCode")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'bindingverifyCodeAccountSecurity'))
    # def test_binding_verify_code(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("原账号信息")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78206")
    # @allure.description("/user/change/binding/verify")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'bindingverifyAccountSecurity'))
    # def test_binding_verify(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("实名信息认证")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78208")
    # @allure.description("/user/change/binding/idAuth")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'idAuthAccountSecurity'))
    # def test_id_auth(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']
    #
    # @allure.story("账号换绑")
    # @allure.link("http://yapi.hikcreate.com/project/31/interface/api/78210")
    # @allure.description("/user/change/binding")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '账号与安全', 'changebindingAccountSecurity'))
    # def test_change_binding(self, inData):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #     res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
    #     allure.attach("{0}".format(res), "用例结果")
    #     assert res['code'] == expectData['code']


if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_account_and_security.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])

    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')







