#coding:utf-8
import os
import pytest
import argparse
from config import BaseConfig
from common.tools import get_case_dir


def get_parser():
    parser = argparse.ArgumentParser(description="argparse")
    parser.add_argument('--product', type=str, default=BaseConfig.current_product)
    return parser


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    BaseConfig.current_product = args.product
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
    os.system('allure serve ./report/tmp')