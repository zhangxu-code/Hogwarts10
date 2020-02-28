from datetime import time
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po_new.contact_page import ContactPage
from test_po_new.wework_page import Wework


class TestContact:

    def setup_class(self):
        self.wework = Wework()
        self.contact = ContactPage(self.wework)

    def teardown_class(self):
        self.wework.quit()


    def test_isnull(self):
        """
        【测试】通讯录-添加成员-姓名不能为空
        """
        assert "请填写姓名" == self.contact.isnull(username="")
    #添加成员用例
    @pytest.mark.parametrize("username,englishname,acctid,phone,tel,email,address,title",
                             [("史晓军" , "大军", "shixiaojun162", "15901273162", "010-82345678", "shixiaojun@qq.com",
                               "河北省三河市燕郊开发区首尔甜城林荫大道25号楼1单元2501", "项目经理")])
    def test_add_member(self,username,englishname,acctid,phone,tel,email,address,title):
        """
        【测试】通讯录-添加成员-成功保存成员
        """
        self.contact.add_member(username,englishname,acctid,phone,tel,email,address,title)
        assert "保存成功" == self.contact.add_member_tip()

    #编辑成员用例
    def test_update_member(self):
        """
        【测试】通讯录-成功编辑成员
        """
        self.contact.search_member("史晓军").edit_member(username="史晓军 %s" % str(time()))
        assert "保存成功" == self.contact.add_member_tip()

