#-*-coding：utf-8  -*-
__testauthor__ = "huangchengcheng"
__time__ = "2021/5/20 9:47"

import os
import allure
import config
import pytest
import xlrd
from common.tools import request_main
from common.utils import getExcelData


headers=config.BMCConfig.headers
@allure.feature("首页基础功能")
class TestHomebasic:
    workbook=xlrd.open_workbook(f'{config.BaseConfig.root_path}/test_case_data/bmc/bmc_home_basic_functions_2021513.xlsx')

    @allure.story("获取开通城市列表")
    @allure.link("")
    @allure.description("creator：liaohui,autoCreator：huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"首页基础功能","SwitchList"))
    def test_switchList(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        res=request_main(url,headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
            assert res["success"]==expectdata["success"]
        except Exception as e:
            raise e


    @allure.story("城市切换保存")
    @allure.description("creator：liaohui,autoCreator：huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"首页基础功能","Switchchange"))
    def test_switchchang(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        res=request_main(url=url,data=data,method=method,headers=headers)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获取资讯分类")
    @allure.description("creator：liaohui,autoCreator：huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"首页基础功能","Newsclassify"))
    def test_Newsclassify(self,indata):
        print(indata)
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        res=request_main(url=url,data=data,method=method,headers=headers)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e

    @allure.story("文章banner列表")
    @allure.description("creator：liaohui,autoCreator：huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"首页基础功能","Newsgetbanner"))
    def test_newsgetbanner(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        expectdata=indata["expectData"]
        data=indata["reqData"]
        res=request_main(url=url,method=method,data=data,headers=headers)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获取资讯列表")
    @allure.description("creator：liaohui,autoCreator：huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"首页基础功能","Newsgetlist"))
    def test_newsgetlist(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        expectdata=indata["expectData"]
        data=indata["reqData"]
        res=request_main(url=url,method=method,data=data,headers=headers)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获得文章详情")
    @allure.description("creator：liaohui,autoCreator：huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"首页基础功能","Newsdetail"))
    def test_newsdetail(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        expectdata=indata["expectData"]
        data=indata["reqData"]
        res=request_main(url=url,method=method,data=data,headers=headers)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e

    @allure.story("资讯列表搜索")
    @allure.description("creator：liaohui,autoCreator：huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"首页基础功能","Newssearch"))
    def test_newssearch(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        expectdata=indata["expectData"]
        data=indata["reqData"]
        res=request_main(url=url,method=method,data=data,headers=headers)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e


# if __name__ == '__main__':
#
#     # 生成报告数据
#     pytest.main(['-v', '-s', "test_homebasic.py", '--alluredir', './bmc/report',"--clean-alluredir"])
#     # pytest.main(['-v', '-s', "test_homebasic.py::TestHomebasic::test_newsgetbanner", '--alluredir', './bmc/report', "--clean-alluredir"])
#     # 打开报告
#     os.system('allure serve ./bmc/report')
