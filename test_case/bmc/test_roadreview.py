#-*-coding：utf-8  -*-
__testauthor__ = "huangchengcheng"
__time__ = "2021/5/20 15:16"

import datetime
import os
import allure
import config
import pytest
import xlrd
from common.tools import request_main
from common.utils import getExcelData
from service.login import BMC



@allure.feature("非交通占用道路审查")
class TestRoadreview:
    workbook=xlrd.open_workbook(f'{config.BaseConfig.root_path}/test_case_data/bmc/bmc_road_review_2021513.xlsx')

    def setup_class(self):
        indata = {"phone": "17822000000", "encodedGesture": "67e6d10010533eed4bbe9659863bf6ee"}
        res = BMC().bmc_login(indata)
        config.BMCConfig.headers["bmc_token"]=res[0]
        config.BMCConfig.headers["bmc_pvt_token"]=res[1]
        self.headers=config.BMCConfig.headers

    @allure.story("首页")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadlist"))
    def test_roadlist(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        data=indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("业务申请")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadaddBasicInfo"))
    def test_roadaddBasicInfo(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        data=indata["reqData"]
        expectdata=indata["expectData"]
        method=indata["method"]
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("业务申请")
    @allure.description("creator:林静文,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"非交通占用道路审查","roadaddOccupyRoadInfo"))
    def test_roadaddOccupyRoadInfo(self,indata):
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
        data=indata["reqData"]
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e

if __name__ == '__main__':

    # 生成报告数据
    # pytest.main(['-v', '-s', "test_roadreview.py", '--alluredir', './bmc/report',"--clean-alluredir"])
    pytest.main(['-v', '-s', "test_roadreview.py::TestRoadreview::test_roadaddOccupyRoadInfo", '--alluredir', './bmc/report', "--clean-alluredir"])
    # 打开报告
    os.system('allure serve ./bmc/report')