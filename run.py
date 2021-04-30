#coding:utf-8
import os
import pytest

if __name__ == "__main__":
    for one in os.listdir('../report/tmp'):
        if 'json' in one:
            os.remove(f'../report/tmp/{one}')
    # 生成报告数据
    pytest.main([ '-s', '--alluredir', '../report/tmp'])

    # 打开报告
    os.system('allure serve ../report/tmp')