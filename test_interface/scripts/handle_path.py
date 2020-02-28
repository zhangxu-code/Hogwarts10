# -*- conding: utf-8 -*-
# @Time:2019/11/17 16:56
# @Author:lyc
# @File: handle_path.py
# @Software: PyCharm

import os

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 获取配置文件所在的路径
CONFIGS_DIR = os.path.join(BASE_DIR, "configs")
# 配置文件的路径
CONFIG_FILE_PATH = os.path.join(CONFIGS_DIR, "config.yaml")

# 日志文件所在的路径
LOGS_DIR = os.path.join(BASE_DIR, "logs")

# 报告文件所在的路径
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

# 获取excel文件所在的路径
DATAS_DIR = os.path.join(BASE_DIR, "datas")

USER_ACCOUNTS_FILE_PATH = os.path.join(CONFIGS_DIR, 'user_account.yaml')

# 获取测试用例文件夹的路径
CASES_DIR = os.path.join(BASE_DIR, "cases")

