# -*- coding: utf-8 -*-
__author__ = 'jiaqiying'
__data__ = "2021-05-06 03:01"
from enum import Enum


# 用例优先级枚举
class CaseGrade(Enum):
    LOW = 0
    MIDDLE = 1
    HIGH = 2


# 产品名称枚举
class ProductName(Enum):
    # 斑马信用app
    BMC = "bmc"

    # 企业云平台
    BMY = "bmy"

    # sso平台
    SSO = "sso"