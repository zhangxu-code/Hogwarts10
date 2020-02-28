import re   #导入正则
import json

from test_wework.scripts.handle_mysql import HandleMysql
from test_wework.scripts.handle_path import USER_ACCOUNTS_FILE_PATH
from test_wework.scripts.handle_yaml import HandleYaml



class HandleParam:
    """
    参数化  字符串前的'r'是防止字符转义的
    """
    not_existed_tel = r"{not_existed_tel}"  # 未注册手机号
    not_existed_id = r"{not_existed_id}"  # 不存在的id

    invest_user_tel = r"{invest_user_tel}"  # 投资人手机号
    invest_user_pwd = r"{invest_user_pwd}"  # 投资人密码
    invest_user_id = r"{invest_user_id}"  # 投资人用户id

    borrow_user_id = r"{borrow_user_id}"  # 借款人用户id
    borrow_user_tel = r"{borrow_user_tel}"  # 借款人手机号

    admin_user_tel = r"{admin_user_tel}"  # 管理员手机号
    # 管理员id

    loan_id_pattern = r'{loan_id}'  # 标id
    not_existed_load_id = r"{not_existed_loan_id}"  # 不存在的标id

    do_user_account = HandleYaml(USER_ACCOUNTS_FILE_PATH)

    @classmethod
    def do_param(cls, data):

        # 不存在的手机号替换
        if re.search(cls.not_existed_tel, data):  # 判断data里是否有not_existed_tel
            do_mysql = HandleMysql()  # 创建HandleMysql对象
            data = re.sub(cls.not_existed_tel, do_mysql.create_not_existed_mobile(), data)  # 判断把未注册的手机号参数替换成实际未注册的手机号
            do_mysql.close()  # 一定要调用关闭

        # 不存在的用户id替换
        if re.search(cls.not_existed_id, data):
            do_mysql = HandleMysql()
            sql = "SELECT id FROM member ORDER BY id DESC LIMIT 0,1;"
            not_existed_id_result = do_mysql.run(sql).get("id") + 10000
            data = re.sub(cls.not_existed_id, str(not_existed_id_result), data)

        # 投资人手机号替换
        if re.search(cls.invest_user_tel, data):  # 判断data里是否有not_existed_tel
            do_mysql = HandleMysql()  # 创建HandleMysql对象
            data = re.sub(cls.invest_user_tel, cls.do_user_account.read("invest", "mobile_phone"),
                          data)  # 判断把已注册的手机号参数替换为已注册的手机号15210428545
            do_mysql.close()  # 一定要调用关闭

        # 投资人密码替换
        if re.search(cls.invest_user_pwd, data):
            data = re.sub(cls.invest_user_pwd, cls.do_user_account.read("invest", "pwd"), data)

        # 投资人用户id替换
        if re.search(cls.invest_user_id, data):
            data = re.sub(cls.invest_user_id, str(cls.do_user_account.read('invest', 'id')), data)

        # 借款人id替换
        if re.search(cls.borrow_user_id, data):
            data = re.sub(cls.borrow_user_id, str(cls.do_user_account.read("borrow", "id")), data)

        # 借款人手机号替换
        if re.search(cls.borrow_user_tel, data):
            data = re.sub(cls.borrow_user_tel, cls.do_user_account.read("borrow", "mobile_phone"), data)

        # 管理员手机号替换
        if re.search(cls.admin_user_tel, data):
            data = re.sub(cls.admin_user_tel, cls.do_user_account.read("admin", "mobile_phone"), data)

        # 标id替换
        if re.search(cls.loan_id_pattern, data):
            rel_loan_id_pattern = getattr(cls, "rel_loan_id_pattern")
            data = re.sub(cls.loan_id_pattern, str(rel_loan_id_pattern), data)

        # 不存在的标id替换
        if re.search(cls.not_existed_load_id, data):
            do_mysql = HandleMysql()
            sql = "select id from loan order by id desc limit 0,1;"
            do_mysql.run(sql)
            rel_not_existed_load_id = do_mysql.run(sql).get("id") + 1000
            do_mysql.close()
            data = re.sub(cls.not_existed_load_id, str(rel_not_existed_load_id), data)

        return data


if __name__ == '__main__':
    str1 = '{"mobile_phone":"","pwd":""}'
    str2 = '{"mobile_phone":"{not_existed_tel}","pwd":"12345678","type":0,"reg_name":"shaoai"}'
    str3 = '{"mobile_phone":"{invest_user_tel}","pwd":"12345678","type":1,"reg_name":"shaoai"}'
    str4 = '{"mobile_phone":{invest_user_tel}, "pwd": "{invest_user_pwd}"}'
    str5 = '{"member_id": {not_existed_id}, "amount": 600}'
    str6 = '{"member_id": {invest_user_id}, "amount": 600.222}'
    str8 = '{"member_id": {invest_user_id},"amount":null}'

    str9 = '{"member_id":{borrow_user_id},"title":"借钱实现财富自由","amount":2000,"loan_rate":12.0,"loan_term":3,"loan_date_type":1,"bidding_days":5}'
    str10 = '{"mobile_phone":"{borrow_user_tel}","pwd":"12345678"}'
    str11 = '{"mobile_phone":"{admin_user_tel}","pwd":"12345678"}'
    str12 = '{"member_id":{invest_user_id}, "loan_id":{not_existed_loan_id},"amount":300}'

    print(HandleParam.do_param(str9))
    print(HandleParam.do_param(str10))
    print(HandleParam.do_param(str11))
    print(HandleParam.do_param(str12))






    #
    # print(HandleParam.do_param(str1))
    # print(HandleParam.do_param(str2))
    # print(HandleParam.do_param(str3))
    # print(HandleParam.do_param(str4))
    # print(HandleParam.do_param(str5))
    # print(HandleParam.do_param(str6))
    # print(json.loads(HandleParam.do_param(str7), encoding="utf8"))