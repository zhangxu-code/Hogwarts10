# -*- conding: utf-8 -*-
# @Time:2019/11/17 16:25
# @Author:lyc
# @File: run.py
# @Software: PyCharm

import unittest
from datetime import datetime
import os



# suite = unittest.TestSuite()
from test_interface.libs.HTMLTestRunnerNew import HTMLTestRunner
from test_interface.scripts.handle_path import USER_ACCOUNTS_FILE_PATH, CASES_DIR, REPORTS_DIR
from test_interface.scripts.handle_user import write_user_info
from test_interface.scripts.handle_yaml import do_yaml

if not os.path.exists(USER_ACCOUNTS_FILE_PATH):
    write_user_info()
suite = unittest.defaultTestLoader.discover(CASES_DIR)

# loader = unittest.TestLoader()
# if not os.path.isfile(os.path.join(CONFIGS_DIR,"rules_user.yaml")):
#     RegisterUser.test_register_three_users()
# suite.addTest(loader.loadTestsFromModule(test_login_api))

result_full_path = do_yaml.read("report", "name") + "_" + \
                   datetime.strftime(datetime.now(), "%Y%m%d%H%M%S") + ".html"
result_full_path = os.path.join(REPORTS_DIR, result_full_path)

with open(result_full_path, "wb") as fb:
    runner = HTMLTestRunner(stream=fb,
                            title=do_yaml.read('report', 'title'),
                            description=do_yaml.read('report', 'description'),
                            tester=do_yaml.read('report', 'tester'))
    runner.run(suite)