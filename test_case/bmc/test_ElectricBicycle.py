#作者: taoke
#时间: 2021/5/31 16:34
#编码: -- coding: utf-8 --
#版本: !python3.7

import pytest,allure,xlrd,requests,os,datetime,random
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



@pytest.fixture(scope='function')
def applySubmit_del() : # 号牌换领初始化_
    mysql = MYSQL(*BaseConfig.test_mysql)
    mysql.ExecuNonQuery(
        "DELETE FROM db_gy_dmsmp.elec_bicy_change_apply WHERE old_plate_num='贵州A20065';")  # 删除驾驶员
    RedisString(0).delete_key("bmc:c1:dl_img:uid")
    yield

@pytest.fixture(scope='function')
def electricBicycle_apply():     # 撤销用例的初始
    # headers = BMCConfig.headers   # 单独跑用例，在这儿使用
    # headers['Pvt-Token'] = BMCConfig.bmc_pvt_token
    # headers['Token'] = BMCConfig.bmc_token
    req_data = {"idCardFront": "/group1/M00/00/12/CsXswmCWYmSAR-MyAAETz8z_wnU267.jpg",
                "idCardBack": "/group1/M00/00/12/CsXswmCWX7KAUhnwAAJNBLcB7t8390.jpg",
                "idCardHolding": "/group1/M00/00/12/CsXsyWCWX7WAVlilAAIH4RXNjCU152.jpg",
                "frameNumberPicture": "/group1/M00/00/12/CsXsyWCWX7mATu4tAAJRfeuJLMk818.jpg",
                "chinaProductCertification": "",
                "qualificationPictureFront": "/group1/M00/00/12/CsXswmCWX8CAap1KAAI478TVrkk602.jpg",
                "qualificationPictureBack": "/group1/M00/00/12/CsXswmCWX8OAcUDXAAJbjNcuYDA752.jpg",
                "vehiclePurchaseInvoice": "", "vehiclePurchaseHolding": "",
                "vehicleRearLeft": "/group1/M00/00/12/CsXsyWCWX8qAb28IAAouW5i3RRs249.jpg",
                "vehicleLeft": "/group1/M00/00/12/CsXswmCWX8-AEpM2AAlcdGC3lu4658.jpg",
                "vehicleRight": "/group1/M00/00/12/CsXswmCWX9SADyOGAAncK1T4SXo181.jpg",
                "vehicleInvoicePicture": "/group1/M00/00/12/CsXsyWCWX8WAXVpIAAJALFqsbA0243.jpg",
                "certificateType": "居民身份证", "certificateNumber": "520102199306117822", "residenceAddress": "小号地址",
                "ownerName": "pytest自动化", "cellphoneNumber": "19180580229", "currentHomeAddressProvince": "贵州省",
                "currentHomeAddressCity": "",
                "currentHomeAddressArea": "贵阳市南明区新华社区服务中心纪念塔居委会解放路88号-贵阳红星拖拉机厂宿舍1栋4单元1层102",
                "currentHomeAddressStreet": "", "currentHomeAddress": "", "notResidenceCertificate": "",
                "vehiclePurchaseTime": "2018-10-10", "frameNumber": "579757890668997", "vehicleBrands": "小宝",
                "vehicleColor": "灰,白,白", "vehicleSizeLong": "120", "vehicleSizeWidth": "50", "vehicleSizeHigh": "30",
                "vehicleModel": "5569885598", "vehicleManufacturer": "小黑", "vehicleProductionDate": "2005-10-10",
                "showDetailAddress": False, "id": "", "dmvId": 565, "dmvName": "自动化", "appointDate": "2021-05-28",
                "appointTime": 1, "applyCountReachedLimit": False, "appointDates": ""}
    today = datetime.date.today()
    if today.isoweekday() in [5, 6, 7]:
        today += datetime.timedelta(days=8 - today.isoweekday())  # 需要是工作日
        appointDate = str(today)
    else:
        today += datetime.timedelta(days=1)  # 放管服设置需提前预约一天
        appointDate = str(today)
        print(appointDate)
    # 随机一位修改车架号
    frameNumber = f"{random.randint(100, 999)}757890668{random.randint(100, 999)}"
    req_data['appointDate'] = appointDate
    req_data['frameNumber'] = frameNumber
    res = requests.post(f"{BMCConfig().host}/pvtapi/electricBicycle/apply/newGB/submit", json=req_data, headers=headers)
    return res.json()['data']['id']


# @allure.epic("斑马信用")
@allure.feature("电动车预约")
class TestDrivingLicense( ) :
    workBook = xlrd.open_workbook(f'{BaseConfig.root_path}/test_case_data/bmc/bmc_ElectricBicycle_20210531.xlsx')
    def setup_class(self):
        pass

    @allure.story("“通行证类型”状态")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/19711")
    @allure.description("/pvtapi/deliveryVehicle/passcardTypeState")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'passcardTypeState'))
    def test_passcardTypeState(self,inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("电动车banner接口")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/61377")
    @allure.description("接口：/electric/electricBannerOrPop，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'electricBannerOrPop'))
    def test_electricBannerOrPop(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("电动车banner接口")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/61377")
    @allure.description("接口：/electric/electricBannerOrPop，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'electricBannerOrPop'))
    def test_electricBannerOrPop(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("检测是否领取")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45684")
    @allure.description("接口：/pvtapi/electricBicycle/isBind，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'electricBicycleIsBind'))
    def test_electricBicycleIsBind(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("电动自行车行驶证二维码")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/46554")
    @allure.description("接口：/electricBicycle/qr，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'ElectricBicycleQr'))
    def test_ElectricBicycleQr(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("获取须知信息")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/7704")
    @allure.description("接口：/pvtapi/sys/notice/detail，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'noticeDetail'))
    def test_noticeDetail(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("文件上传")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/5452")
    @allure.description("接口：/pvtapi/file/upload，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'fileUpload'))
    def test_fileUpload(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        expectData = inData['expectData']
        """特殊处理"""
        headers = {'City-Code': "520100", 'Device-Brand': "vivo", 'Device-Code': "000000001e167ed7000000001e167ed7",
                   'Device-Model': "vivo vivo X20", 'Device-Name': "vivo+X20", 'Device-Type': "Android",
                   'Mac': "38:6E:A2:A0:0E:AF", 'mimeType': "application/json", 'Net': "wifi", 'OS-Type': "Android",
                   'OS-Version': "27", 'Pvt-Token': f"{BMCConfig.bmc_pvt_token}", 'Resolution': "2034x1080",
                   'Token': f"{BMCConfig.bmc_token}", 'Version': "2.2.6"}
        user_file = {'file': ("321.gif", open(f"{BaseConfig.root_path}/test_case_data/bmc/321.gif", 'rb'), 'image/png/jpg')}
        res = requests.post(url, files=user_file, headers=headers)
        allure.attach(f"{res.json()}", "响应结果", allure.attachment_type.TEXT)
        assert res.json()['code'] == expectData['code']


    @allure.story("获取系统字典")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/5077")
    @allure.description("接口：/pvtapi/sys/dict/list，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'sysDictlist'))
    def test_sysDictlist(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("地址选择")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45572")
    @allure.description("接口：//electricBicycle/apply/address/addressSelector，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'addressSelector'))
    def test_addressSelector(self, inData):
        url = f"{BMCConfig().pvthost}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("车架号是否存在")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45032")
    @allure.description("接口：/pvtapi/electricBicycle/getBikeCccInfo，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'getBikeCccInfo'))
    def test_getBikeCccInfo(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("检查车架号和身份证号")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45540")
    @allure.description("接口：/pvtapi/electricBicycle/checkStatus，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'checkStatus'))
    def test_checkStatus(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("车管所列表")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45216")
    @allure.description("接口：/pvtapi/electricBicycle/dmv/list，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'dmvList'))
    def test_dmvList(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("获取可预约日期的列表")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45508")
    @allure.description("接口：/pvtapi/electricBicycle/exchangeLicensePlate/getDataList，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'getDataList'))
    def test_getDataList(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']
#12339225 12339157


    @allure.story("提交新国标备案申请") # 时间需要加8小时
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/44776")
    @allure.description("接口：/pvtapi/electricBicycle/apply/newGB/submit，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'newGBsubmit'))
    def test_newGBsubmit(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 返回一个可用的预约日期
        today = datetime.date.today()
        if today.isoweekday() in [5, 6, 7]:
            today += datetime.timedelta(days=8 - today.isoweekday())    # 需要是工作日
            appointDate=str(today)
        else:
            today += datetime.timedelta(days=1)      # 放管服设置需提前预约一天
            appointDate=str(today)
            print(appointDate)
        # 随机一位修改车架号
        frameNumber = f"{random.randint(100, 999)}757890668{random.randint(100, 999)}"
        req_data['appointDate']=appointDate
        req_data['frameNumber']=frameNumber
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("预约状态查询")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45356")
    @allure.description("接口：/pvtapi/electricBicycle/apply/records/applyStatus，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'applyStatus'))
    def test_applyStatus(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("电动车banner接口")
    @allure.link("http://yapi.hikcreate.com/project/31/interface/api/61377")
    @allure.description("接口：/electric/electricBannerOrPop，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'electricBanner'))
    def test_electricBanner(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("登记信息详情")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45360")
    @allure.description("接口：/pvtapi/electricBicycle/apply/records/applyDetail，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'recordsApplyDetail'))
    def test_recordsApplyDetail(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("登记记录列表查询")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45352")
    @allure.description("接口：/pvtapi/electricBicycle/apply/records/list，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'applyRecords'))
    def test_applyRecords(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """请求"""
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("取消申请")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45324")
    @allure.description("接口：/pvtapi/electricBicycle/applyCancel，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'applyCancel'))
    def test_applyCancel(self, inData,electricBicycle_apply):   # 初始化新增一个申请获取id
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        """处理"""
        req_data['id']=electricBicycle_apply
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("获取电动车手机号列表")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45652")
    @allure.description("接口：/pvtapi/electricBicycle/getPhones，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'getPhones'))
    def test_getPhones(self, inData, ):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 请求 #需要electric_bicycle_apply ，已归档的数据
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    # @pytest.mark.scoreDetail
    @allure.story("发送短信")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/45640")
    @allure.description("接口：/pvtapi/electricBicycle/smsSend，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'smsSend'))
    def test_smsSend(self, inData, ):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 请求
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    # @pytest.mark.scoreDetail
    @allure.story("换领须知文案")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/78482")
    @allure.description("接口：/pvtapi/elecBicyChange/apply/elecBicyChangeNotice，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'elecBicyChangeNotice'))
    def test_elecBicyChangeNotice(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 请求
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


    @allure.story("获取行驶证列表")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/78486")
    @allure.description("接口：/pvtapi/elecBicyChange/apply/elecBicyLicenseList，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'elecBicyLicenseList'))
    def test_elecBicyLicenseList(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 请求
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @allure.story("预约记录查询")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/78666")
    @allure.description("接口：/pvtapi/elecBicyChange/apply/elecBicyApplyPage，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'elecBicyApplyPage'))
    def test_elecBicyApplyPage(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 请求
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @pytest.mark.scoreDetail
    @pytest.mark.usefixtures("applySubmit_del")
    @allure.story("提交申请")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/78476")
    @allure.description("接口：/pvtapi/elecBicyChange/apply/submit，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'applySubmit'))
    def test_applySubmit(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 请求
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']

    @pytest.mark.scoreDetail
    @allure.story("撤回申请")
    @allure.link("http://yapi.hikcreate.com/project/32/interface/api/78478")
    @allure.description("接口：/pvtapi/elecBicyChange/apply/recall，creator：胥键雪，autoCreator：taoke")
    @allure.title("{inData[testPoint]}")
    @pytest.mark.parametrize("inData", get_excelData(workBook, '电动车', 'applyRecall'))
    def test_applyRecall(self, inData):
        url = f"{BMCConfig().host}{inData['url']}"
        method = inData['method']
        req_data = inData['reqData']
        expectData = inData['expectData']
        headers = inData['headers']
        # 请求
        res = request_main(url, headers, method, req_data)
        allure.attach(f"{res}", "响应结果", allure.attachment_type.TEXT)
        assert res['code'] == expectData['code']


if __name__ == '__main__':
    for one in os.listdir('../../report/tmp'):  #  '-m','scoreDetail' ,
        if 'json' in one:
            os.remove(f'../../report/tmp/{one}')
    pytest.main(['test_ElectricBicycle.py', '-s',  '-m','scoreDetail' , '--alluredir','../../report/tmp'])
    os.system('allure serve ../../report/tmp')
