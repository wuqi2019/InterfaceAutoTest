#-*-coding：utf-8  -*-
__testauthor__ = "huangchengcheng"
__time__ = "2021/6/15 10:19"

import os

import allure
import pytest
import xlrd
from common.db import MYSQL
from common.tools import request_main
from common.utils.getExcelData import get_excelData
from config import BaseConfig, BMCConfig


class TestElebicycle:
    workbook=xlrd.open_workbook(f'{BaseConfig.root_path}/test_case_data/bmc/bmc_prize20210531.xlsx')

    def setup_class(self):
        mysql=MYSQL(*BaseConfig.test_mysql)
        mysql.ExecuNonQuery("INSERT INTO edl_public.user_prize (user_id,`type`,source,prize_name,prize_img,name,phone,address_region,address_detail,coupon_id,tips,tips_mini,receive_flag,redeem_way,coupon_type,coupon_redeem_url,use_status,external_coupon,gmt_expiry_start,gmt_expiry_end,is_show_receive,gmt_create,gmt_modified,receive_point_id) VALUES (598137,1,'自动化奖品','100元加油卡',NULL,NULL,NULL,NULL,NULL,NULL,'<p>领奖地址：贵阳市南明区遵义路15号贵阳广播电视大楼一楼FM102.7贵阳交通广播广告接待中心——交通1027发奖办公室</p><p>领奖时间：周一至周五10:00-12:00,14:00-16:00（节假日除外）</p>',NULL,0,2,NULL,NULL,NULL,NULL,NULL,NULL,0,'2020-06-11 10:59:59.000','2020-08-07 14:56:47.000',NULL);")
        mysql.ExecuNonQuery("INSERT INTO edl_public.article (display_type,source,title,part_content,imgs,content_url,content,status,verify_status,views,likes,collects,dislikes,feedback_flag,create_by,gmt_create,modified_by,gmt_modified,gmt_release,is_time,is_share,is_recommed,gmt_recommend,city_id) VALUES (2,'自动化','测试的内容','为贯彻落实“9.20”全国公安机关70周年大庆安保维稳战前动员视频会议精神，推动华北片区区域联合整治','/group1/M00/00/6F/CsXsq12dWsaAeXHGAABg40-RswI41.jpeg',NULL,'自动化',1,5,144,1,2,0,0,NULL,'2019-10-09 11:58:03.000',NULL,'2020-07-18 13:31:21.000','2019-10-10 11:48:22.000',0,0,2,NULL,',520100,');")
        mysql.ExecuNonQuery("INSERT INTO edl_public.user_login_device (user_id,device_code,device_name,device_model,gmt_login,status) VALUES (598137,'ffffffffa6dedb72ffffffffa6dedb73','ART-AL00x','HUAWEI nava','2021-03-30 15:58:43.000',1);")


    @allure.story("获取奖品记录")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata',get_excelData(workbook,"电动车","PrizeLoglist"))
    def test_prizeLoglist(self,indata):
        url=f'{BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        headers=indata["headers"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url=url,headers=headers,method=method,data=data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获取实物奖品信息")
    @allure.title("indata[testPoint]")
    @pytest.mark.parametrize("indata",get_excelData(workbook,"电动车","PrizeLoginfo"))
    def test_prizeLoginfo(self,indata):
        url=f"{BMCConfig.host}/{indata['url']}"
        method=indata["method"]
        mysql = MYSQL(*BaseConfig.test_mysql)
        id=mysql.ExecuQuery("select id from edl_public.user_prize where user_id='598137';")[-1]["id"]
        indata["reqData"]["id"]=id
        data=indata["reqData"]
        expectdata=indata["expectData"]
        headers=indata["headers"]
        if indata["testPoint"] == "获取实物奖品信息":
            self.res=request_main(url,headers,method,data)
        else:
            mysql=MYSQL(*BaseConfig.test_mysql)
            mysql.ExecuNonQuery("update edl_public.user_prize set receive_flag=1 where user_id='598137'and source='自动化奖品';")
            self.res = request_main(url, headers, method, data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("用户收获地址列表")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata',get_excelData(workbook,"电动车","PrizeLogaddress"))
    def test_prizeLogaddress(self,indata):
        url=f'{BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        headers=indata["headers"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url=url,headers=headers,method=method,data=data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e

    @allure.story("获取默认地址")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata',get_excelData(workbook,"电动车","PrizeLogdefault"))
    def test_prizeLogdefault(self,indata):
        url=f'{BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        headers=indata["headers"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url=url,headers=headers,method=method,data=data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("【线上领奖】领取奖品")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata',get_excelData(workbook,"电动车","PrizeLogonline"))
    def test_prizeLogonline(self,indata):
        url=f'{BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        headers=indata["headers"]
        mysql = MYSQL(*BaseConfig.test_mysql)
        mysql.ExecuNonQuery("update edl_public.user_prize set receive_flag=0 where user_id='598137'and source='自动化奖品';")
        id = mysql.ExecuQuery("select id from edl_public.user_prize where user_id='598137';")[-1]["id"]
        indata["reqData"]["prizeId"]=id
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url=url,headers=headers,method=method,data=data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("我的礼券")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "Coupon"))
    def test_coupon001(self, indata):
        url = f'{BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("收藏文章")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "Article"))
    def test_article(self, indata):
        url = f'{BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        mysql = MYSQL(*BaseConfig.test_mysql)
        id = mysql.ExecuQuery("select id from edl_public.article where display_type='2' and source='自动化' and title='测试的内容';")[-1]["id"]
        indata["reqData"]["id"]=id
        data=indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("文章详情")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "Articledetail"))
    def test_articledetail(self, indata):
        url = f'{BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        mysql = MYSQL(*BaseConfig.test_mysql)
        id = mysql.ExecuQuery("select id from edl_public.article where display_type='2' and source='自动化' and title='测试的内容';")[-1]["id"]
        indata["reqData"]["id"] = id
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("点赞文章")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "Articlelike"))
    def test_articlelike(self, indata):
        url = f'{BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        mysql = MYSQL(*BaseConfig.test_mysql)
        id = mysql.ExecuQuery("select id from edl_public.article where display_type='2' and source='自动化' and title='测试的内容';")[-1]["id"]
        indata["reqData"]["id"] = id
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获取版本列表")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "Syslist"))
    def test_syslist(self, indata):
        url = f'{BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("版本更新")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "Sysupdate"))
    def test_sysupdate(self, indata):
        url = f'{BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("服务协议")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "Sysh"))
    def test_sysh5(self, indata):
        url = f'{BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("常用登陆设备")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "SysloginDevices"))
    def test_sysloginDevices(self, indata):
        url = f'{BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("常用登陆设备")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "Sysremove"))
    def test_sysremove(self, indata):
        url = f'{BMCConfig.host}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        mysql=MYSQL(*BaseConfig.test_mysql)
        id=mysql.ExecuQuery("select id from edl_public.user_login_device where user_id=598137;")[-1]["id"]
        indata["reqData"]["deviceId"]=id
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e



    @allure.story("检查驾驶证补领状态")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "ReplacementDrvcheck"))
    def test_replacementDrvcheck(self, indata):
        url = f'{BMCConfig.pvthost}{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("提交驾驶证补领信息")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize('indata', get_excelData(workbook, "电动车", "ReplacementDrvapply"))
    def test_replacementDrvapply(self, indata):
        url = f'{BMCConfig.pvthost}/{indata["url"]}'
        method = indata["method"]
        headers = indata["headers"]
        data = indata["reqData"]
        expectdata = indata["expectData"]
        self.res = request_main(url=url, headers=headers, method=method, data=data)
        print(self.res)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e






    def teardown(self):
        allure.attach(f'{self.res}',"响应结果",allure.attachment_type.TEXT)


    def teardown_class(self):
        mysql=MYSQL(*BaseConfig.test_mysql)
        mysql.ExecuNonQuery("delete from edl_public.user_prize where user_id='598137' and source='自动化奖品';")
        mysql.ExecuNonQuery("delete from edl_public.article  where display_type='2' and source='自动化' and title='测试的内容';")
        mysql.ExecuNonQuery("delete from edl_public.user_login_device where user_id=598137 and device_model='HUAWEI nava';")


if __name__ == '__main__':
    # pytest.main(["-s","-v","test_elebicycle.py",'--alluredir', './bmc/report',"--clean-alluredir"])
    pytest.main(['-v', '-s', "test_elebicycle.py::TestElebicycle::test_replacementDrvapply", '--alluredir', './bmc/report', "--clean-alluredir"])
    # os.system('allure serve ./bmc/report')


