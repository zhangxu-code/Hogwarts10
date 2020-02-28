from unittest import TestCase

from appium_po.page.xueqiu_page import XueqiuPage


class TestProfile():

    def setup(self):
        self.xueqiu = XueqiuPage()
        self.profile = self.xueqiu.goto_profile()

    #手机登录
    def test_login_by_phone(self):
        assert "验证码已过期" in self.profile.login_by_phone("15901273161","1234").get_tips()

    #微信登录
    def test_login_by_wechat(self):
        self.profile.login_by_wechat()
        assert "请先安装微信" in self.profile.get_toast()
    #微博登录
    def test_login_by_weigo(self):
        self.fail()

    #QQ登录
    def test_login_by_qq(self):
        self.fail()
