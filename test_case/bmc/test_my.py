#-*-coding：utf-8  -*-
__testauthor__ = "huangchengcheng"
__time__ = "2021/5/21 16:47"

import json
import os

import allure
import config
import pytest
import xlrd
from common.db import MYSQL
from common.tools import request_main
from common.utils import getExcelData
from config import BaseConfig
#111111

@allure.feature("我的")
class TestMy:
    workbook = xlrd.open_workbook(f'{config.BaseConfig.root_path}/test_case_data/bmc/bmc_my_2021513.xlsx')

    def setup_class(self):
        config.BMCConfig.headers["Pvt-Token"]=getattr(config.BMCConfig,"bmc_pvt_token")
        config.BMCConfig.headers["Token"]=getattr(config.BMCConfig,"bmc_token")
        self.headers=config.BMCConfig.headers
        mysql = MYSQL(*BaseConfig.test_mysql)
        mysql.ExecuNonQuery( "insert into edl_public.feedback_type values ('10008611','自动化类型','0','1','0','2021-05-01 16:51:12','2021-05-01 16:51:12','520100,330100,500100');")
        mysql.ExecuNonQuery( "INSERT INTO edl_public.trade (user_id,phone,brand_id,shop_id,trade_type,trade_amount,privilege_amount,pay_amount,uuid,trade_no,trade_source,memo,gmt_finished,status,gmt_create,gmt_modified,shop_name,brand_name,trade_status,remark_status,verification_status,settlement_status,refund_status,close_status,gmt_closed,close_memo,expired_status,gmt_expired,bill_status) VALUES (598137,'17822000000',48,112,2,2.55,0.00,2.55,'7ac6253d-8586-475d-8474-be848fe5c4b6','hik202105081390911897531973632',1,NULL ,NULL ,1,'2021-05-08 14:10:13.000','2021-05-24 17:25:30.000','回归测试门店1','回归（个人）1',3,'N/A','N/A','N/A','N/A','N/A',NULL,NULL,'N/A','2021-06-07 14:10:13.000','N/A');")


    @allure.story("个人信息获取")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfouserngs"))
    def test_myinfouserngs(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e

    @allure.story("个人信息修改")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfonickname"))
    def test_myinfonickname(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("个人信息修改")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfoavatar"))
    def test_myinfoavatar(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("用户收货地址")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfoaddresslist"))
    def test_myinfoaddresslist(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("用户收货地址")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfoarea"))
    def test_myinfoarea(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("用户收货地址新增")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfoaddressadd"))
    def test_myinfoaddressadd(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        indata["reqData"]["address"]="接口自动化详细地址"
        indata["reqData"]["recipientName"] = "自动化"
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @pytest.fixture(scope="function")
    def test_addaddressId(self):
        url = f'{config.BMCConfig.host}/user/address/add'
        method='post'
        data={"address":"详细地址","city":"北京市","cityCode":"110100","county":"东城区","countyCode":"110101","defaultAddressFlag":'false',"province":"北京市","provinceCode":"110000","recipientName":"李倩2","recipientPhone":"15283936399"}
        data["recipientName"] = "自动化"
        data["address"] = "接口自动化详细地址"
        expectdata={ "success": 'true',"code": 1000, "msg": "操作成功"}
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @pytest.mark.usefixtures('test_addaddressId')
    @allure.story("用户收货地址")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfoaddressupdate"))
    def test_myinfoaddressupdate(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        mysql = MYSQL(*BaseConfig.test_mysql)
        addressId=mysql.ExecuQuery("SELECT id FROM edl_public.user_address  WHERE address='接口自动化详细地址';")[-1]["id"]
        if indata["reqData"]["address"]=="存在":
            indata["reqData"]["addressId"]=addressId
            self.data=indata["reqData"]
        elif indata["reqData"]["address"]=="addressId为空":
            self.data = indata["reqData"]
        elif indata["reqData"]["address"] == "addressId不存在":
            indata["reqData"]["addressId"]=addressId+36598555
            self.data = indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,self.data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e



    @pytest.mark.usefixtures('test_addaddressId')
    @allure.story("用户收货地址")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfoaddressdefault"))
    def test_myinfoaddressdefault(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        mysql = MYSQL(*BaseConfig.test_mysql)
        addressId = mysql.ExecuQuery("SELECT id FROM edl_public.user_address  WHERE address='接口自动化详细地址';")[-1]["id"]
        if len(indata["reqData"]["addressId"])==0:
            data = indata["reqData"]
        else:
            if indata["reqData"]["addressId"]=='8888':
                indata["reqData"]["addressId"]=addressId+8888
                data = indata["reqData"]
            else:
                indata["reqData"]["addressId"]=addressId
                data = indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e



    @pytest.mark.usefixtures("test_addaddressId")
    @allure.story("用户收货地址")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfoaddressdelete"))
    def test_myinfoaddressdelete(self,indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        expectdata = indata["expectData"]
        mysql = MYSQL(*BaseConfig.test_mysql)
        addressId = mysql.ExecuQuery("SELECT id FROM edl_public.user_address  WHERE address='接口自动化详细地址';")[-1]["id"]
        if len(indata["reqData"]["addressId"])==0:
            data = indata["reqData"]
        else:
            indata["reqData"]["addressId"]=addressId
            data = indata["reqData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e



    @allure.story("获取列表信息")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myserviceguesses"))
    def test_myserviceguesses(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获取列表信息")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myservicehotlist"))
    def test_myservicehotlist(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("智能问答")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myservicechat"))
    def test_myservicechat(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("消息分类列表")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Messagecentergroups"))
    def test_messagecentergroups(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("未读消息数")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","MessagecenterunRead"))
    def test_messagecenterunread(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e



    @allure.story("消息列表")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Messagecenterlist"))
    def test_messagecenterlist(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @pytest.fixture(scope="function")
    def messagecenterlist(self):
        url = f'{config.BMCConfig.host}/msg/list'
        method ='get'
        data={"timestamp":0,"size":20,"bizType":"msg","groupId":1}
        res = request_main(url, self.headers, method, data)
        return res["data"]["list"]



    @allure.story("读消息")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Messagecenterread"))
    def test_messagecenterread(self, indata,messagecenterlist):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        if messagecenterlist==[]:
            pytest.skip("无消息可读取")
        else:
            indata["reqData"]['msgId']=messagecenterlist[0]["msgId"]
            data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("全部已读")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Messagecenterall"))
    def test_messagecenterall(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获取公网H5页面地址")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Basich"))
    def test_basich5(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获取奖品记录")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Basiclist"))
    def test_basiclist(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("【订单】 - 列表")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Basictradelist"))
    def test_basictradelist(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("【订单】 - 我的订单状态列表")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Basicstatuslist"))
    def test_basicstatuslist(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("【订单】 - 查看券码")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "BasiccouponCode"))
    def test_basiccouponCode(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        expectdata = indata["expectData"]
        if indata["reqData"]["tradeId"]=="不存在id":
            indata["reqData"]["tradeId"]=1234567890
            data = indata["reqData"]
        else:
            mysql = MYSQL(*BaseConfig.test_mysql)
            tradeId = mysql.ExecuQuery("select id from edl_public.trade where status=1 and trade_status=2 limit 1;")[0]["id"]
            indata["reqData"]["tradeId"]=tradeId
            data=indata["reqData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("【订单】 - 取消")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Basiccancel"))
    def test_basiccancel(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        expectdata = indata["expectData"]
        if isinstance(indata["reqData"]["tradeId"],str):
            if indata["reqData"]["tradeId"] == "不存在id":
                indata["reqData"]["tradeId"] = 1234567890
                data = indata["reqData"]
            else:
                mysql = MYSQL(*BaseConfig.test_mysql)
                mysql.ExecuNonQuery("update edl_public.trade set trade_status='2'where user_id='598137';")
                tradeId=mysql.ExecuQuery("select id from edl_public.trade where trade_status=2 and user_id='598137';")[-1]["id"]
                indata["reqData"]["tradeId"] = tradeId
                data = indata["reqData"]
        else:
            mysql = MYSQL(*BaseConfig.test_mysql)
            mysql.ExecuNonQuery("update edl_public.trade set trade_status='1'where user_id='598137';")
            tradeId = mysql.ExecuQuery("select id from edl_public.trade where status=1 and user_id='598137';")[-1]["id"]
            indata["reqData"]["tradeId"] = tradeId
            data = indata["reqData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获取意见反馈类型")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "FeedbackfeedbackType"))
    def test_feedbackfeedbackType(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("新增意见反馈")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Feedbackadd"))
    def test_feedbackadd(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        if indata["reqData"]['content']=="不传类型id自动化测试":
            data=indata["reqData"]
        else:
            indata["reqData"]["feedbackTypeId"]=10008611
            data=indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e



    @pytest.fixture(scope="function")
    def feedbackadd(self):
        url=f'{config.BMCConfig.host}/v1/feedback/add'
        feedbackTypeId=10008611
        print(feedbackTypeId)
        data = {"content":"自动化新用户意见数据","feedbackTypeId":feedbackTypeId}
        method = "post"
        res=request_main(url,self.headers,method,data)
        mysql = MYSQL(*BaseConfig.test_mysql)
        feedbackId=mysql.ExecuQuery("select feedback_id from edl_public.feedback_chat_record where user_id='598137' and content='自动化新用户意见数据';")[-1]["feedback_id"]
        return feedbackId


    @pytest.mark.usefixtures("feedbackadd")
    @allure.story("意见反馈列表")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Feedbacklist"))
    def test_feedbacklist(self, indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e



    @allure.story("意见反馈详情")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "Feedbackdetails"))
    def test_feedbackdetails(self, indata,feedbackadd):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        indata["reqData"]["feedbackId"]=feedbackadd
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("检查未读信息")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "我的", "FeedbackcheckFeedbackSee"))
    def test_feedbackcheckFeedbackSee(self, indata,feedbackadd):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        otherexpectData=indata["otherExpectData"]
        if indata['testPoint']=="有未读信息":
            mysql = MYSQL(*BaseConfig.test_mysql)
            mysql.ExecuNonQuery("update edl_public.feedback_main set read_flag='0'where user_id='598137'and feedback_type_id='10008611';")
            mysql.ExecuNonQuery("update edl_public.feedback_main set status='1'where user_id='598137'and feedback_type_id='10008611';")
        else:
            mysql = MYSQL(*BaseConfig.test_mysql)
            mysql.ExecuNonQuery( "update edl_public.feedback_main set read_flag='1'where user_id='598137'and feedback_type_id='10008611';")
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
            assert self.res["data"]["flag"]==otherexpectData["data"]["flag"]
        except Exception as e:
            raise e


    @allure.story("问题已解决")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Feedbacksolve"))
    def test_feedbacksolve(self,indata,feedbackadd):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        indata["reqData"]["feedbackId"] = feedbackadd
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    def teardown(self):
        mysql = MYSQL(*BaseConfig.test_mysql)
        mysql.ExecuNonQuery("delete from edl_public.feedback_type where id='10008611';")
        mysql.ExecuNonQuery("delete from edl_public.feedback_chat_record where user_id='598137'")
        mysql.ExecuNonQuery("delete from edl_public.feedback_main where user_id='598137'")

        allure.attach(f"{self.res}",'响应结果',allure.attachment_type.TEXT)


    def teardown_class(self):
        mysql = MYSQL(*BaseConfig.test_mysql)
        mysql.ExecuNonQuery("update edl_public.user set nickname='自动化' where id='598137';")
        mysql.ExecuNonQuery( "delete from edl_public.user_address where user_id='598137'and address in ('接口自动化详细地址','存在');")
        mysql.ExecuNonQuery("delete from edl_public.trade where user_id='598137'and trade_no='hik202105081390911897531973632';")

# if __name__ == '__main__':
#     pytest.main(["-s","-v","test_my.py",'--alluredir', './bmc/report',"--clean-alluredir"])
    # pytest.main(['-v', '-s', "test_my.py::TestMy::test_basiccouponCode", '--alluredir', './bmc/report', "--clean-alluredir"])
    # os.system('allure serve ./bmc/report')



