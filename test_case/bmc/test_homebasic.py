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



@allure.feature("首页基础功能")
class TestHomebasic:
    workbook=xlrd.open_workbook(f'{config.BaseConfig.root_path}/test_case_data/bmc/bmc_home_basic_functions_2021513.xlsx')

    def setup_class(self):
        config.BMCConfig.headers["Pvt-Token"] = getattr(config.BMCConfig, "bmc_pvt_token")
        config.BMCConfig.headers["Token"] = getattr(config.BMCConfig, "bmc_token")
        self.headers = config.BMCConfig.headers


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
        self.res=request_main(url,self.headers,method,data)
        try:
            assert self.res["code"]==expectdata["code"]
            assert self.res["success"]==expectdata["success"]
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
        self.res=request_main(url=url,data=data,method=method,headers=self.headers)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @allure.story("获取资讯分类")
    @allure.description("creator：liaohui,autoCreator：huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"首页基础功能","Newsclassify"))
    def test_Newsclassify(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        self.res=request_main(url=url,data=data,method=method,headers=self.headers)
        try:
            assert self.res["code"]==expectdata["code"]
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
        self.res=request_main(url=url,method=method,data=data,headers=self.headers)
        try:
            assert self.res["code"]==expectdata["code"]
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
        self.res=request_main(url=url,method=method,data=data,headers=self.headers)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e

    @pytest.fixture(scope='function')
    def newsgetlist(self):
        url = f'{config.BMCConfig.host}/news/categoryItems'
        method = "get"
        data = {"categoryId":"1","page":"1","size":"20"}
        res=request_main(url,self.headers,method,data,)
        return res



    @allure.story("获得文章详情")
    @allure.description("creator：liaohui,autoCreator：huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"首页基础功能","Newsdetail"))
    def test_newsdetail(self,indata,newsgetlist):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        expectdata=indata["expectData"]
        try:
            newlist=newsgetlist["data"]["list"]
            if newlist==[]:
                pytest.skip("没有文章，无法获取文章详情")
            else:
                if len(indata["reqData"]["id"])==0:
                    data = indata["reqData"]
                else:
                    indata["reqData"]["id"]=newlist[0]["id"]
                    data=indata["reqData"]
        except Exception as e:
            raise e
        self.res=request_main(url=url,method=method,data=data,headers=self.headers)
        try:
            assert self.res["code"]==expectdata["code"]
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
        self.res=request_main(url=url,method=method,data=data,headers=self.headers)
        try:
            assert self.res["code"]==expectdata["code"]
        except Exception as e:
            raise e

    def teardown(self):
        allure.attach(f'{self.res}','相应结果',allure.attachment_type.TEXT)


# if __name__ == '__main__':
#
#     # 生成报告数据
#     pytest.main(['-v', '-s', "test_homebasic.py", '--alluredir', './bmc/report',"--clean-alluredir"])
#     # pytest.main(['-v', '-s', "test_homebasic.py::TestHomebasic::test_newsdetail", '--alluredir', './bmc/report', "--clean-alluredir"])
#     # 打开报告
#     os.system('allure serve ./bmc/report')
