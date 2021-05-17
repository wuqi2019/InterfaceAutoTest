#coding:utf-8
import os
import pytest
import argparse
from config import BaseConfig
from common.tools import get_case_dir
from common.utils import dingTalk


def get_parser():
    parser = argparse.ArgumentParser(description="argparse")
    parser.add_argument('--product', type=str, default=BaseConfig.current_name)
    return parser


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    BaseConfig.current_name = args.product
    # 获取要执行的产品的用例目录
    test_case_dir = get_case_dir(args.product)
    print("********此次执行的产品测试用例是：%s********"%test_case_dir)

    #删除之前报告
    os.system('rm ./report/tmp/*.json')
    # 生成报告数据
    pytest.main(['-v', '-s', test_case_dir, '--alluredir', './report/tmp'])
    # 打开报告
    # os.system('allure serve ./report/tmp')
    # 发送钉钉
    dingTalk.dingTalk_markdown(secret="SEC465015385218e70a94f107a16f72dd33d8fc118c3b2a631e0433685302f2fbb3",
                 webhook="https://oapi.dingtalk.com/robot/send?access_token=229908a83825ed56abbf728d3382e446a4e8a90e9ad302c37a036bcbccbbf9ee",
                               message="")

