# -*- conding: utf-8 -*-
# @Time:2020/1/27 11:58
# @Author:lyc
# @File: main.py
# @Software: PyCharm

import pytest

if __name__ == '__main__':
    pytest.main(["--reruns", "2", "--reruns-delay", "5",
                 #"--html=reports/result.html",
                 "--alluredir=allure-results",
                 ])
    #pytest.main(["-s"])
    #pytest.main(["-v", "-m", "demo", "--alluredir=allure_report"])
