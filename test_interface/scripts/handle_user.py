# -*- conding: utf-8 -*-
# @Time:2019/11/20 19:02
# @Author:lyc
# @File: test_register_users.py
# @Software: PyCharm
from test_interface.scripts.handle_mysql import HandleMysql
from test_interface.scripts.handle_path import USER_ACCOUNTS_FILE_PATH
from test_interface.scripts.handle_requests import HandleRequests
from test_interface.scripts.handle_yaml import do_yaml


def create_new_user(reg_name, pwd="12345678", user_type=1):
    """
    创建一个用户
    :param reg_name: 用户名
    :param pwd: 密码，默认为123456
    :param user_type: 用户类型 默认为1（0：管理员，1：普通会员）
    :return: 存储一个用户信息, 嵌套字典的字典(以用户名为key, 以用户信息所在字典为value)
    """
    do_mysql = HandleMysql()  # 创建数据库对象
    do_request = HandleRequests()  # 创建request对象
    # 构建请求参数，向注册接口发起请求
    do_request.add_headers(do_yaml.read("api", "version"))  # 添加公共请求头
    url = do_yaml.read("api", "host") + '/member/register'  # 构建请求url
    sql = do_yaml.read("mysql", "select_userid_sql")  # 查询用户id的sql语句
    while True:
        mobile_phone = do_mysql.create_not_existed_mobile()  # 生成一个未注册的手机号
        # 构建请求体
        data = {
            "mobile_phone": mobile_phone,
            "pwd": pwd,
            "reg_name": reg_name,
            "type": user_type}
        do_request.sent(url=url, data=data)  # 发起请求
        # 从数据库查询注册后的用户的id
        result = do_mysql.run(sql, args=(mobile_phone,))
        # 判断是否查询到，如果查询到就跳出循环，查询不到继续循环
        if result:
            user_id = result["id"]
            break
            # 构建用户数据字典
    user_dic = {
        reg_name: {
            "id": user_id,
            "mobile_phone": mobile_phone,
            "reg_name": reg_name,
            "pwd": pwd,
            "type": user_type
        }
    }
    # 把用户数据返回
    do_mysql.close()
    do_request.close()
    return user_dic  # 把构建的字典返回


def write_user_info():
    """
    生成三个用户信息
    :return:
    """
    user_datas_dict = {}
    user_datas_dict.update(create_new_user("admin", user_type=0))
    user_datas_dict.update(create_new_user("invest"))
    user_datas_dict.update(create_new_user("borrow"))
    do_yaml.write(user_datas_dict, USER_ACCOUNTS_FILE_PATH)


if __name__ == '__main__':
    write_user_info()
    pass
