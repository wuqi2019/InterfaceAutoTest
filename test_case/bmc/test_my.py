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


@allure.feature("我的")
class TestMy:
    workbook = xlrd.open_workbook(f'{config.BaseConfig.root_path}/test_case_data/bmc/bmc_my_2021513.xlsx')

    def setup_class(self):
        config.BMCConfig.headers["Pvt-Token"]=getattr(config.BMCConfig,"bmc_pvt_token")
        config.BMCConfig.headers["Token"]=getattr(config.BMCConfig,"bmc_token")
        self.headers=config.BMCConfig.headers


    @allure.story("个人信息获取")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfouserngs"))
    def test_myinfouserngs(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        data=indata["reqData"]
        expectdata=indata["expectData"]
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
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
        res = request_main(url, self.headers, method, data)
        try:
            assert res["code"] == expectdata["code"]
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
        mysql = MYSQL("10.197.236.190", 3306, "root", "123456", db="edl_public")
        addressId=mysql.ExecuQuery("SELECT id FROM user_address  WHERE address='接口自动化详细地址';")[-1]["id"]
        if indata["reqData"]["address"]=="存在":
            indata["reqData"]["addressId"]=addressId
            self.data=indata["reqData"]
        elif indata["reqData"]["address"]=="addressId为空":
            self.data = indata["reqData"]
        elif indata["reqData"]["address"] == "addressId不存在":
            indata["reqData"]["addressId"]=addressId+36598555
            self.data = indata["reqData"]
        expectdata=indata["expectData"]
        res=request_main(url,self.headers,method,self.data)
        try:
            assert res["code"]==expectdata["code"]
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
        mysql = MYSQL("10.197.236.190", 3306, "root", "123456", db="edl_public")
        addressId = mysql.ExecuQuery("SELECT id FROM user_address  WHERE address='接口自动化详细地址';")[-1]["id"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e



    @pytest.mark.skip(reason="接口yapi上存在，但是该接口在实际情况中没有使用到，斑马信用app没有收货地址详情页")
    @pytest.mark.usefixtures('test_addaddressId')
    @allure.story("用户收货地址")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfogetaddressdetail"))
    def test_myinfogetaddressdetail(self,indata):
        url=f'{config.BMCConfig.host}/{indata["url"]}'
        method=indata["method"]
        expectdata=indata["expectData"]
        mysql = MYSQL("10.197.236.190", 3306, "root", "123456", db="edl_public")
        addressId = mysql.ExecuQuery("SELECT id FROM user_address  WHERE address='接口自动化详细地址';")[-1]["id"]
        indata["reqData"]["addressId"]=addressId
        data = indata["reqData"]
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e


    @pytest.mark.usefixtures("test_addaddressId")
    @allure.story("用户收货地址新增")
    @allure.description("creator:李倩,autoCreator:huangchengcheng")
    @allure.title("{indata[testPoint]}")
    @pytest.mark.parametrize("indata",getExcelData.get_excelData(workbook,"我的","Myinfoaddressdelete"))
    def test_myinfoaddressdelete(self,indata):
        url = f'{config.BMCConfig.host}/{indata["url"]}'
        method = indata["method"]

        expectdata = indata["expectData"]
        mysql = MYSQL("10.197.236.190", 3306, "root", "123456", db="edl_public")
        addressId = mysql.ExecuQuery("SELECT id FROM user_address  WHERE address='接口自动化详细地址';")[-1]["id"]
        if len(indata["reqData"]["addressId"])==0:
            data = indata["reqData"]
        else:
            indata["reqData"]["addressId"]=addressId
            data = indata["reqData"]
        res = request_main(url, self.headers, method, data)
        try:
            assert res["code"] == expectdata["code"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
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
        res=request_main(url,self.headers,method,data)
        try:
            assert res["code"]==expectdata["code"]
        except Exception as e:
            raise e
if __name__ == '__main__':
    pytest.main(["-s","-v","test_my.py",'--alluredir', './bmc/report',"--clean-alluredir"])
    # pytest.main(['-v', '-s', "test_my.py::TestMy::test_myservicehotlist", '--alluredir', './bmc/report', "--clean-alluredir"])
    os.system('allure serve ./bmc/report')