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
from config import BMCConfig,BaseConfig


@allure.feature("账号信息基本功能")
class TestLogin():
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_login_20210513.xlsx')
    @allure.story("登录")
    @allure.severity("")
    @allure.title("{inData[testPoint]}")
    @allure.testcase("{inData[yapiAddress]}")
    @allure.description("url:/auth/login 。。。。")
    @pytest.mark.parametrize("inData", get_excelData(workBook,'登录', 'login'))
    def test_login(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method  = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.loginheader
        res = request_main(url= url,headers = headers,method =method,data = req_data,has_token=True)
        assert res['code'] == expectData['code']

    @allure.story("激活")
    @allure.link("")
    @allure.description("/user/credit/idAuth")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '登录', 'Active'))
    def test_active(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = config.BMCConfig.headers
        res = request_main(url=url, headers=headers, method=method, data=req_data)
        assert res['code'] == expectData['code']


class TestRegister():
    """注册"""
    workBook = xlrd.open_workbook(f'{BMCConfig.root_path}/test_case_data/bmc/bmc_base_info_2021513.xlsx')

    def setup_class(self):
    # def test_mysql_result(self):
        """数据库操作"""
        # self.ms = MYSQL('10.197.236.190', 3306, 'root', '123456', 'edl_public')
        self.ms = MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")

        # mysql = BaseConfig.test_mysql_215
        # self.ms  = MYSQL(*mysql)

    @allure.story("获取用户登录类型")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10745")
    @allure.description("/v1/user/login/type")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.flaky(reruns=2)
    @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'logintypeRegister'))
    def test_login_type_register(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        phone = req_data['phone']
        if not phone:
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            assert res['code'] == expectData['code']
        else:
            resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
            if resList:  # 已经注册过
                user_id = self.resList[0]['id']
                self.ms.ExecuNonQuery(
                    f'delete from edl_public.user where id={user_id};')
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']

    @allure.story("获取图形验证码")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/20446")
    @allure.description("/sys/captcha")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'captchaRegister'))
    def test_captcha_register(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_picture(self):
        """获取图形验证码"""
        url = f"{BMCConfig().host}/sys/captcha"
        method = 'get'
        req_data = {"bCityCode":"520100","bizType":"1"}
        headers = None
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
        return res
    #
    @allure.story("图形短信验证码")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10943")
    @allure.description("/v1/user/login/verifyCode/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'verifyCodedetailRegister'))
    def test_verify_code_detail_register(self, inData, test_picture):
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
        # elif casenum == 'verifyCodedetailRegister009' or casenum == 'verifyCodedetailRegister010':
            # time.sleep(61)
        #     pass
        if not phone:
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            # 发送次数过多
            if res['msg'] == '验证码发送次数过多，请24小时后再试' or '发送的间隔时间' in res['msg']:
                expectData['code'] = 1006
            assert res['code'] == expectData['code']
        else:
            resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
            if resList:
                user_id = resList[0]['id']
                self.ms.ExecuNonQuery(
                    f'delete from edl_public.user where id={user_id};')
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            # 发送次数过多
            if res['msg'] == '验证码发送次数过多，请24小时后再试' or '发送的间隔时间' in res['msg']:
                expectData['code'] = 1006
            assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_pre_message(self):
        """请求短信验证码"""
        # 获取图片验证码
        url1 = f"{BMCConfig().host}/sys/captcha"
        method1 = 'get'
        req_data1 = {"bCityCode":"520100","bizType":"1"}
        headers = None
        res_picture = request_main(url=url1, headers=headers, method=method1, data=req_data1, has_token=False)

        # 获取短信验证码
        url = f"{BMCConfig().host}/v1/user/login/verifyCode/detail"
        method = 'post'
        req_data = {"phone":"15999009999","bizType":1,"horPercent":None,"jtId":None,"bCityCode":"520100","bNetTag":"trf_mgt"}
        headers = None
        phone = req_data['phone']

        jtId = res_picture['data']['jtId']
        req_data['jtId'] = jtId
        horPercent = int(RedisString(0).get(f'bmc:captcha:{jtId}'))
        req_data['horPercent'] = horPercent
        resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
        if resList:
            user_id = resList[0]['id']
            self.ms.ExecuNonQuery(
                f'delete from edl_public.user where id={user_id};')
        res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)

    @allure.story("短信验证")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10787")
    @allure.description("/user/login/verifyCode")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'loginverifyCodeRegister'))
    def test_login_verify_code_register(self, inData, test_pre_message):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        casenum = inData['caseNum']
        phone = req_data['phone']
        pre = test_pre_message
        if not phone:
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            assert res['code'] == expectData['code']
        else:
            resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
            if resList:
                user_id = resList[0]['id']
                self.ms.ExecuNonQuery(
                    f'delete from edl_public.user where id={user_id};')
            if casenum == 'loginverifyCodeRegister004' or casenum == 'loginverifyCodeRegister005':
                try:
                    verifyCode = int(RedisString(0).get(f'edl:sms_value:{phone}:MOBILE_REGISTER'))
                except Exception:
                    expectData['code'] = 1006
                else:
                    req_data['verifyCode'] = verifyCode
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_pre_gesture_login(self):
        """请求令牌"""
        # 获取图片验证码
        picture_url = f"{BMCConfig().host}/sys/captcha"
        picture_method = 'get'
        picture_req_data = {"bCityCode": "520100", "bizType": "1"}
        picture_headers = None
        res_picture = request_main(url=picture_url, headers=picture_headers, method=picture_method, data=picture_req_data, has_token=False)
        # 获取短信验证码
        pic_msg_url = f"{BMCConfig().host}/v1/user/login/verifyCode/detail"
        pic_msg_method = 'post'
        pic_msg_req_data = {"phone": "15999099999", "bizType": 1, "horPercent": None, "jtId": None, "bCityCode": "520100",
                    "bNetTag": "trf_mgt"}
        pic_msg_headers = None
        phone = pic_msg_req_data['phone']
        jtId = res_picture['data']['jtId']
        pic_msg_req_data['jtId'] = jtId
        horPercent = int(RedisString(0).get(f'bmc:captcha:{jtId}'))
        pic_msg_req_data['horPercent'] = horPercent
        resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
        if resList:
            user_id = resList[0]['id']
            self.ms.ExecuNonQuery(
                f'delete from edl_public.user where id={user_id};')
        RedisString(0).delete_key(f"edl:sms_total:{phone}")
        RedisString(0).delete_key(f"edl:sms_one_total:{phone}")
        request_main(url=pic_msg_url, headers=pic_msg_headers, method=pic_msg_method, data=pic_msg_req_data, has_token=False)
        # 短信验证
        message_url = f"{BMCConfig().host}/user/login/verifyCode"
        message_method = 'post'
        message_req_data = {"phone":"15999099999","bizType":1,"bCityCode":"520100","bNetTag":"trf_mgt","verifyCode":""}
        message_headers = None
        try:
            verifyCode = int(RedisString(0).get(f'edl:sms_value:{phone}:MOBILE_REGISTER'))
        except Exception as e:
            raise TypeError('验证码发送次数过多，请24小时后再试')
        else:
            message_req_data['verifyCode'] = verifyCode
            res = request_main(url=message_url, headers=message_headers, method=message_method, data=message_req_data, has_token=False)
            return res  # {'success': True, 'code': 1000, 'msg': '操作成功', 'errorMsg': '操作成功', 'data': {'oneTimeToken': '357c8d80-e135-41a0-baae-009893f50a6e'}}

    @allure.story("设置手势-登录")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/10974")
    @allure.description("/v1/user/login/gesture/setAndLogin")
    @allure.title("{inData[testPoint]}")
    # @pytest.mark.flaky(reruns=1)
    @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'gesturesetAndLoginRegister'))
    def test_ges_ture_set_and_login_register(self, inData, test_pre_gesture_login):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        phone = req_data['phone']
        casenum = inData['caseNum']
        one_time_token = test_pre_gesture_login['data']['oneTimeToken']
        if not phone:
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            assert res['code'] == expectData['code']
        else:
            resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
            if resList:
                user_id = resList[0]['id']
                self.ms.ExecuNonQuery(
                    f'delete from edl_public.user where id={user_id};')
            if casenum >= 'gesturesetAndLoginRegister004':
                req_data['oneTimeToken'] = one_time_token
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']

    @pytest.fixture()
    def test_pre_pwd_login(self):
        """请求令牌"""
        # 获取图片验证码
        picture_url = f"{BMCConfig().host}/sys/captcha"
        picture_method = 'get'
        picture_req_data = {"bCityCode": "520100", "bizType": "1"}
        picture_headers = None
        res_picture = request_main(url=picture_url, headers=picture_headers, method=picture_method,
                                   data=picture_req_data, has_token=False)

        # 获取短信验证码
        pic_msg_url = f"{BMCConfig().host}/v1/user/login/verifyCode/detail"
        pic_msg_method = 'post'
        pic_msg_req_data = {"phone": "15999999999", "bizType": 1, "horPercent": None, "jtId": None,
                            "bCityCode": "520100",
                            "bNetTag": "trf_mgt"}
        pic_msg_headers = None
        phone = pic_msg_req_data['phone']
        jtId = res_picture['data']['jtId']
        pic_msg_req_data['jtId'] = jtId
        horPercent = int(RedisString(0).get(f'bmc:captcha:{jtId}'))
        pic_msg_req_data['horPercent'] = horPercent
        resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
        if resList:
            user_id = resList[0]['id']
            self.ms.ExecuNonQuery(
                f'delete from edl_public.user where id={user_id};')
        RedisString(0).delete_key(f"edl:sms_total:{phone}")
        RedisString(0).delete_key(f"edl:sms_one_total:{phone}")
        request_main(url=pic_msg_url, headers=pic_msg_headers, method=pic_msg_method, data=pic_msg_req_data,
                     has_token=False)

        # 短信验证
        message_url = f"{BMCConfig().host}/user/login/verifyCode"
        message_method = 'post'
        message_req_data = {"phone": "15999999999", "bizType": 1, "bCityCode": "520100", "bNetTag": "trf_mgt",
                            "verifyCode": ""}
        message_headers = None
        try:
            verifyCode = int(RedisString(0).get(f'edl:sms_value:{phone}:MOBILE_REGISTER'))
        except Exception as e:
            raise TypeError('验证码发送次数过多，请24小时后再试')
        else:
            message_req_data['verifyCode'] = verifyCode
            res = request_main(url=message_url, headers=message_headers, method=message_method, data=message_req_data,
                           has_token=False)
            return res  # {'success': True, 'code': 1000, 'msg': '操作成功', 'errorMsg': '操作成功', 'data': {'oneTimeToken': '357c8d80-e135-41a0-baae-009893f50a6e'}}

    @allure.story("字符密码-登录")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/11027")
    @allure.description("/v1/user/login/keyboardPwd/setAndLogin")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '账号信息基本功能', 'keyboardPwdsetAndLoginRegister'))
    def test_keyboard_pwd_set_and_login_register(self, inData, test_pre_pwd_login):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        phone = req_data['phone']
        casenum = inData['caseNum']
        one_time_token = test_pre_pwd_login['data']['oneTimeToken']
        if not phone:
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            assert res['code'] == expectData['code']
        else:
            resList = self.ms.ExecuQuery(f'SELECT * FROM edl_public.user where phone={phone};')
            if resList:
                user_id = resList[0]['id']
                self.ms.ExecuNonQuery(
                    f'delete from edl_public.user where id={user_id};')
            if casenum >= 'keyboardPwdsetAndLoginRegister004':
                req_data['oneTimeToken'] = one_time_token
            res = request_main(url=url, headers=headers, method=method, data=req_data, has_token=False)
            allure.attach("{0}".format(res), "用例结果")
            assert res['code'] == expectData['code']



if __name__ == '__main__':
    pytest.main(['-s', '-v', 'test_accountinfo.py',
                 r'--alluredir=D:\项目\接口自动化\InterfaceAutoTest\report', '--clean-alluredir'])
#
    os.system('allure serve D:\项目\接口自动化\InterfaceAutoTest\\report')

