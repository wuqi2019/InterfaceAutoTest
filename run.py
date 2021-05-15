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
    for one in os.listdir('./report/tmp'):
        if 'json' in one:
            os.remove(f'./report/tmp/{one}')
    # 生成报告数据
    pytest.main(['-v', '-s', test_case_dir, '--alluredir', './report/tmp'])
    # 打开报告
    # os.system('allure serve ./report/tmp')
    dingTalk.dingTalk_markdown(secret="SEC1d08f46da74337cc0e1cd5bb9ad19622d825483343fdfa43ce396881e4745bdb",
                 webhook="https://oapi.dingtalk.com/robot/send?access_token=f9e005c1a984b9607960345d38669337b1115d1141a0294e98666443b312115b",
                               message="")

