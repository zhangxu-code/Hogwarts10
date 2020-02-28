import allure
import pytest
from test_interface.scripts.handle_excel import HandleExcel
from test_interface.scripts.handle_log import do_log
from test_interface.scripts.handle_parameterize import HandleParam
from test_interface.scripts.handle_requests import HandleRequests
from test_interface.scripts.handle_yaml import do_yaml


class TestRegister:
    excel = HandleExcel("register_cases")  # 创建HandleExcel对象
    cases = excel.read_data()  # 读取excel中register_cases【列表里面包含的是对象】
    do_log.debug("读取excel用例成功")  # 记录读取用例日志

    def setup_class(self):
        self.do_request = HandleRequests()  # 在所有用例执行之前，创建HandlerRequest对象
        self.do_request.add_headers(do_yaml.read("api", "version"))  # 添加公共请求头，接口版本号

    def teardown_class(self):
        self.do_request.close()

    @allure.title('register-{case['"title"']}')
    @pytest.mark.parametrize("case", cases)  # case 是对象，因cases列表中包含的是对象
    def test_register(self, case):
        print(case["url"])
        register_url = do_yaml.read("api", "host") + case["url"]  # 构建完成的接口地址
        register_params = HandleParam.do_param(case["data"])  # 取出需要传递的参数（参数化之后的需要替换为实际的）
        register_res = self.do_request.send(register_url,
                                            data=register_params)  # 发起请求，并把请求结果转成json,赋值给register_res
        register_res_dict = register_res.json()
        print(register_res)
        case_title = case["title"]  # 测试用例项名称
        success_msg = do_yaml.read("msg", "success_result")
        fail_msg = do_yaml.read("msg", "fail_result")

        try:
            assert case["expected"] == register_res_dict["msg"]
        except AssertionError as e:
            # 执行失败，把结果写入excel
            self.excel.write_data(row=case["case_id"] + 1, column=do_yaml.read("excel", "result_col"), value=fail_msg)
            do_log.error(f"{case_title}的执行结果为：{fail_msg}\n具体异常为{e}")
            raise e

        else:
            # 执行成功，也把结果写入excel
            self.excel.write_data(row=case["case_id"] + 1, column=do_yaml.read("excel", "result_col"), value=success_msg)
        finally:
            # 把响应报文写入excel
            self.excel.write_data(row=case["case_id"] + 1, column=do_yaml.read("excel", "actual_col"), value=register_res.text)
