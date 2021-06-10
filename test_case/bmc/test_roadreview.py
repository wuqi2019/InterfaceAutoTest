#-*-coding：utf-8  -*-
__testauthor__ = "huangchengcheng"
__time__ = "2021/5/20 15:16"

import datetime
import os
import allure
import config
import pytest
import xlrd
from common.db import MYSQL
from common.tools import request_main
from common.utils import getExcelData
from service.login import BMC
from config import BaseConfig



@allure.feature("非交通占用道路审查")
class TestRoadreview:
    workbook=xlrd.open_workbook(f'{config.BaseConfig.root_path}/test_case_data/bmc/bmc_road_review_2021513.xlsx')

    def setup_class(self):
        indata = {"phone": "17822000000", "encodedGesture": "67e6d10010533eed4bbe9659863bf6ee"}
        res = BMC().bmc_login(indata)
        config.BMCConfig.headers["bmc_token"]=res[0]
        config.BMCConfig.headers["bmc_pvt_token"]=res[1]
        self.headers=config.BMCConfig.headers
        mysql=MYSQL(*BaseConfig.test_mysql)
        self.pvt_user_id=mysql.ExecuQuery("SELECT id FROM edl_private.user WHERE phone='17822000000';")[0]["id"]
        #不同账号登录，将sql中的user_id修改为获取到的用户专网id：self.pvt_user_id


    @allure.story("首页")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadlist"))
    def test_roadlist(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        data=indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("业务申请")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadgetBefore"))
    def test_roadgetBefore(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        data=indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("业务申请")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadmylist"))
    def test_roadmylist(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        data=indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("业务申请")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadaddBasicInfo"))
    def test_roadaddbasicinfo(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        data=indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @pytest.fixture(scope='function')
    def roadaddbasicinfo(self):
        url=f'{config.BMCConfig.host}/pvtapi/occupy/road/addBasicInfo'
        data={"isHasNotFinish": 0,"peoplePhone": "18800000044","companyName": "666","organizeCode": "168685858588855850","peopleName": "接口自动化","id":'null'}
        method='post'
        res=request_main(url,self.headers,method,data)
        mysql = MYSQL(*BaseConfig.test_mysql)
        basic_info_id = mysql.ExecuQuery("select id from db_gy_dmsmp.occupy_road_apply where user_id=393038 and people_phone='18800000044'order by id;")[-1]["id"]
        return basic_info_id


    @allure.story("业务申请")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadaddOccupyRoadInfo"))
    def test_roadaddoccupyroadinfo(self,indata,roadaddbasicinfo):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        today=datetime.datetime.now()
        offset=datetime.timedelta(days=1)
        beginDate=(today + offset).strftime('%Y-%m-%d')
        endDate=(today+offset+offset).strftime('%Y-%m-%d')
        expectdata=indata["expectData"]
        method=indata["method"]
        indata["reqData"]["beginDate"]=beginDate
        indata["reqData"]["endDate"]=endDate
        #处理开始结束时间不能小于当前日期问题
        indata["reqData"]["id"]=roadaddbasicinfo
        #处理关联任务的请求id
        data=indata["reqData"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @pytest.fixture(scope="function")
    def roadaddoccupyroadinfo(self,roadaddbasicinfo):
        url = f'{config.BMCConfig.host}//pvtapi/occupy/road/addOccupyRoadInfo'
        today = datetime.datetime.now()
        offset = datetime.timedelta(days=1)
        beginDate = (today + offset).strftime('%Y-%m-%d')
        endDate = (today + offset + offset).strftime('%Y-%m-%d')
        reqdata={ "operateType":1,"operateReason":2,"occupyType":2,"beginDate":"2021-05-10","endDate":"2021-07-10","roadRemark":"这是接口自动化数据","width":"2","length": "10","vehicle":[{ "plateType":"蓝牌","plateNum":"京A 54344"}],"time": [{"beginTime": "06:00","endTime": "18:00"}],"roadName": "四川省成都市双流区湖畔路北段","roadLng": 104.090169,"roadLat": 30.402453,"id": "404"}
        method = 'post'
        reqdata["beginDate"] = beginDate
        reqdata["endDate"] = endDate
        # 处理开始结束时间不能小于当前日期问题
        reqdata["id"] = roadaddbasicinfo
        # 处理关联任务的请求id
        data =reqdata
        res = request_main(url, self.headers, method, data)
        return roadaddbasicinfo



    @allure.story("业务申请")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata", getExcelData.get_excelData(workbook, "非交通占用道路审查", "roadaddpFile"))
    def test_roadaddfile(self, indata,roadaddoccupyroadinfo):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        expectdata = indata["expectData"]
        method = indata["method"]
        indata["reqData"]["id"]=roadaddoccupyroadinfo
        data = indata["reqData"]
        self.res = request_main(url, self.headers, method, data)
        try:
            assert self.res["code"] == expectdata["code"]
        except Exception as e:
            raise e



    @allure.story("申请详情")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roaddetail"))
    def test_roaddetail(self,indata,roadaddbasicinfo):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        indata["reqData"]["id"] = roadaddbasicinfo
        data = indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("重新提交")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadreSubmit"))
    def test_roadresubmit(self,indata,roadaddbasicinfo):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        indata["reqData"]["id"]=roadaddbasicinfo
        data = indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("查看意见书")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadnoticeDetail"))
    def test_roadnoticedetail(self,indata,roadaddbasicinfo):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        indata["reqData"]["id"]=roadaddbasicinfo
        data = indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("占道施工公示")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadtemOccupyRoad"))
    def test_roadtemoccupyroad(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        data=indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    def teardown_class(self):
        mysql = MYSQL(*BaseConfig.test_mysql)
        mysql.ExecuNonQuery("delete from db_gy_dmsmp.occupy_road_apply where user_id='393038' and people_phone='18800000044' ;")

    def teardown(self):
        allure.attach(f'{self.res}','响应结果',allure.attachment_type.TEXT)






# if __name__ == '__main__':

    # 生成报告数据
    # pytest.main(['-v', '-s', "test_roadreview.py", '--alluredir', './bmc/report',"--clean-alluredir"])
    # pytest.main(['-v', '-s', "test_roadreview.py::TestRoadreview::test_roadaddfile", '--alluredir', './bmc/report', "--clean-alluredir"])
    # 打开报告
    # os.system('allure serve ./bmc/report')