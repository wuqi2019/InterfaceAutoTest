#作者: taoke
#时间: 2021/5/13 18:59
#编码: -- coding: utf-8 --
#版本: !python3.7

#
import pytest,allure,xlrd,requests,os
from common.utils.getExcelData import  get_excelData
from service.login import BMY
from common.tools import request_main
from config import BaseConfig,BMCConfig
from service.login import BMC
from common.db import RedisString,MYSQL

"""环境初始化和清除"""
# 1.headers获取
headers = BMCConfig.headers
headers['Pvt-Token'] = BMCConfig.bmc_pvt_token
headers['Token'] = BMCConfig.bmc_token

@pytest.fixture(scope='function') # 绑定车辆 初始化
def get_code() :    # 绑定车辆时获取验证码(手机号是绑定车辆固定参数的手机号)
    payload = {"plateType": "02", "plateNum": "贵APS001", "vehicleIdentifyNum": "000001", "ownerName": "配送车"}
    requests.get(f"{BMCConfig().host}/vehicle/vCode/detail", params=payload, headers=headers)
    num = RedisString(0).get(f"edl:sms_value:18581438351:BIND_VEHICLE")
    num = str(num)[-7:-1]
    return num

@pytest.fixture(scope='function') # 解绑车辆初始化
def get_vehickleId_Tounbind():
    res= requests.get(f"{BMCConfig().pvthost}/vehicle/license/list", headers=headers)
    for dic in res.json()['data']['list']:
        if dic['plateNumName'] == '贵A·PS001':  # 为绑定车辆的车牌
            vehicleId = dic['vehicleId']
            return vehicleId

@pytest.fixture(scope='function')
def avatarUpdate_del() : #修改头像清除
    mysql=BaseConfig.test_mysql_215
    mysql = MYSQL(*mysql)

    # mysql = MYSQL(host="10.197.236.190", port=3306, user="root", pwd="123456", db="edl_private")
    # mysql = MYSQL("10.197.236.215", 3306, "root", "DataCenter@!hik", "edl_public")
    mysql.ExecuNonQuery(
        "DELETE FROM edl_private.driving_license_image_audit WHERE name='自动化';")  # 删除驾驶员
    RedisString(0).delete_key("bmc:c1:dl_img:uid")
    yield

@pytest.fixture(scope='function')
def imaAuditStatus():  # 查看照片审核状态
    payload = {"bNetTag": "trf_mgt", "avatarUrl": "\/group1\/M00\/00\/11\/CsXswmCTvF-AOPy1AABzUjaImN072.JPEG",
               "bCityCode": "520100"}
    res = requests.post(f"{BMCConfig().host}/drivingLicense/avatar/update", json=payload, headers=headers)



@allure.epic("电子证照")
# @allure.feature("电子驾驶证")
class TestDrivingLicense():
    workBook = xlrd.open_workbook(f'{BaseConfig.root_path}/test_case_data/bmc/bmc_ele_License_2021513.xlsx')
    def setup_class(self):
        RedisString(0).delete_key("edl:sms_total:18581438351")      # 删除发送验证码次数缓存,手机号为绑定车辆用例的车辆的手机号
        RedisString(0).delete_key("edl:sms_one_total:18581438351")
    @allure.story("二维码详情")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/81596")
    @allure.description("/dlVeh/qr")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'dlVehqr'))
    def test_dlVehQr(self,inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("获取驾驶证图片状态")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/22758")
    @allure.description("/drivingLicense/image/status")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'LicimageStatus'))
    def test_LicimageStatus(self,inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @pytest.mark.usefixtures("imaAuditStatus")
    @allure.story("照片审核状态")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/22759")
    @allure.description("/drivingLicense/image/audit/status")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'imaAuditStatus'))
    def test_imaAuditStatus(self,inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("图像上传页文案")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/22762")
    @allure.description("/drivingLicense/image/text")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'LicenimageText'))
    def test_LicenimageText(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @pytest.mark.usefixtures("avatarUpdate_del")
    @allure.story("修改驾驶证头像")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/22750")
    @allure.description("/drivingLicense/avatar/update")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'LicenAvaUpdate'))
    def test_LicenAvaUpdate(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("驾照扣分记录")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/5332")
    @allure.description("/drivingLicense/score/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'scoreDetail'))
    def test_scoreDetail(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("驾驶证图片接口")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/10859")
    @allure.description("/drivingLicense/image")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'LicenseImage'))
    def test_LicenseImage(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        # method = inData['method']
        req_data = inData['reqData']
        # expectData = inData['expectData']
        # headers = inData['headers']
        """请求"""
        res = requests.get(url,params=req_data,headers=headers)
        """断言,此接口响应和其他不通，暂未做断言"""
        allure.attach("{0}".format(res), "用例结果")
        # assert res['code'] == expectData['code']


    @allure.story("我的行驶证列表")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/46536")
    @allure.description("/vehicle/license/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'vehicleLicenseList'))
    def test_vehicleLicenseList(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']



    @pytest.mark.run(order=664)     # 建议放在 绑定用例之后
    @allure.story("行驶证二维码")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/81596")
    @allure.description("/dlVeh/qr(电子行驶证二维码)")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'vehicledlVehqr'))
    def test_vehicledlVehqr(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']

        """处理"""
        # 1.使用行驶证列表接口获取一个车的vehicleId
        resp = requests.get(f"{BMCConfig().pvthost}/vehicle/license/list", headers=headers)
        vehicleId = resp.json()['data']['list'][0]['vehicleId']

        # 2.修改参数
        req_data['vehicleId'] = vehicleId

        """请求"""
        res = request_main(url, headers, method, req_data,has_token=True)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    """把其他某个用例做为初始化，这种方式还需讨论，暂时不行"""
    # # @pytest.mark.scoreDetail
    # @allure.story("行驶证二维码2")
    # @allure.link("http://yapi.hikcreate.com/project/32/interface/api/81596")
    # @allure.description("/dlVeh/qr(电子行驶证二维码)")
    # @allure.title("{inData[testPoint]}")
    # @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'vehicledlVehqr'))
    # def test_vehicledlVehqr2(self, inData,test_vehicleLicenseList):
    #     url = f"{BMCConfig().pvthost}{inData['url']}"
    #     method = inData['method']
    #     req_data = inData['reqData']
    #     expectData = inData['expectData']
    #     headers = inData['headers']
    #
    #     """处理"""
    #     # 2.修改参数
    #     print("我打印一下", req_data)
    #     req_data['vehicleId'] = test_vehicleLicenseList
    #     print("我打印一下",req_data)
    #
    #     """请求"""
    #     res = request_main(url, headers, method, req_data)
    #     """断言"""
    #     assert res['code'] == expectData['code']


    @allure.story("车辆管理列表")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/10913")
    @allure.description("/vehicle/manage/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'vehiclelist'))
    def test_vehiclelist(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']

    @pytest.mark.run(order=662)
    @allure.story("绑定机动车-发送验证码")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/8261")
    @allure.description("/vehicle/vCode/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'bindVcode'))
    def test_bindVcode(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']

    @pytest.mark.run(order=663)
    @allure.story("绑定机动车-提交")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/8268")
    @allure.description("/vehicle/bind")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'vehicleBind'))
    def test_vehicleBind(self, inData,get_code):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']

        """处理"""
        # 若参数读出为验证码88888，则修改为正确的
        if req_data["verifyCode"]=="888888":
            req_data["verifyCode"]= get_code
        else:
            pass
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']

    @pytest.mark.run(order=665)         # 需要在绑定用例之后
    @allure.story("解绑机动车备案")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/1888")
    @allure.description("/vehicle/unbind")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'vehicleUnbind'))
    def test_vehicleUnbind(self, inData, get_vehickleId_Tounbind):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']

        """处理"""
        req_data["vehicleId"] = get_vehickleId_Tounbind
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']




    @allure.story("机动车详情")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/1880")
    @allure.description("/vehicle/bind/detail")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'binddetail'))
    def test_binddetail(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']


    @allure.story("获取检验合格标志信息")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/51369")
    @allure.description("/vehicle/getInspectionSign")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'getInspectionSign'))
    def test_getInspectionSign(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']


    @allure.story("违法列表")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/5254")
    @allure.description("/violation/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'violationList'))
    def test_violationList(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach("{0}".format(res), "用例结果")
        assert res['code'] == expectData['code']


    @allure.story("查询强制保险")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/11048")
    @allure.description("/vehicle/insurance/getCompulsoryIns")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'getCompulsoryIns'))
    def test_getCompulsoryIns(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']


    @allure.story("查询商业险")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/11042")
    @allure.description("/vehicle/insurance/getCommercialIns")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'getCommercialIns'))
    def test_getCommercialIns(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']


    @allure.story("添加强制保险")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/11051")
    @allure.description("/vehicle/insurance/setCompulsoryIns")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'setCompulsoryIns'))
    def test_setCompulsoryIns(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']

    @allure.story("添加商业保险")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/11045")
    @allure.description("/vehicle/insurance/setCommercialIns")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'setCommercialIns'))
    def test_setCommercialIns(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']

    @allure.story("关联查询强制险信息")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/65877")
    @allure.description("/vehicle/insurance/setCommercialIns")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'getRelatedCompulsoryIns'))
    def test_getRelatedCompulsoryIns(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']

    @allure.story("获取商业险枚举")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/11066")
    @allure.description("/vehicle/insurance/getDicts")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'insuranceGetDicts'))
    def test_insuranceGetDicts(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']


    @allure.story("车辆选择列表")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/11066")
    @allure.description("/vehicle/selection/list")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电子证照', 'vehicleList'))
    def test_vehicleList(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach( "{0}".format(res),"用例结果")
        assert res['code'] == expectData['code']




    def teardown_class(self):
        """清除"""

if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  # 列出对应文件夹的数据  '-m','scoreDetail' ,
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_ ElectronicLicense.py', '-s',  '--alluredir','../../report/tmp'])
    # 启动默认浏览器打开报告
    os.system('allure serve ../../report/tmp')
