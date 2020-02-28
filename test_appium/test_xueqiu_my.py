from time import sleep
import allure
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_appium.base_page import BasePage
from test_appium.xueqiu_home_page import XueqiuHomePage
from test_appium.xueqiu_init import XueqiuInit
from test_appium.xueqiu_my_page import XueqiuMyPage
from test_appium.xueqiu_search_page import XueqiuSearchPage


@allure.feature("第十期_Appium Desktop 使用_课后作业_登录")
class TestXueqiuMy():
    def setup_class(self):
        self.xueqiuinit = XueqiuInit()
        self.xueqiu_my = XueqiuMyPage(self.xueqiuinit)

    def teardown_class(self):
        self.xueqiuinit.quit()

    @allure.story("【测试】输入手机号错误")
    def test_wrong_phone(self):
        """
        用户名错误，密码正确，断言结果
        """
        self.xueqiu_my.input_phoneandpwd("00000000000", "123456")
        assert "用户名或密码错误" or "请求太频繁，请稍后再试" in self.xueqiu_my.tips
        sleep(3)

    @allure.story("【测试】输入密码错误")
    def test_wrong_password(self):
        """
        用户名正确，密码错误，断言结果
        """
        self.xueqiu_my.input_phoneandpwd("15901273160", "000000")
        assert "用户名或密码错误" or "请求太频繁，请稍后再试" in self.xueqiu_my.tips
        sleep(3)

@allure.feature("第十期_Appium Desktop 使用_课后作业_查询")
class TestSerch():
    def setup_class(self):
        self.xueqiuinit = XueqiuInit()
        self.search = XueqiuSearchPage(self.xueqiuinit)
    def setup(self):
        pass
    def teardown(self):
        self.xueqiuinit.driver.find_element_by_id("action_close").click()
    def teardown_class(self):
        self.xueqiuinit.quit()

    @allure.story("【测试】按关键字查询")
    @pytest.mark.parametrize("key,stocktype,expect_price",[('alibaba','BABA',205),('xiaomi','01810',9.9),('google','GOOGL',1350)])
    def test_search(self,key,stocktype,expect_price):
        """
        数据驱动的参数，预先查询到是有查询结果的，如果断言发生错误，则程序有可能有错误
        """
        #self.search.search(key=key,stocktype=stocktype,expect_price=expect_price)
        #self.xueqiuinit.driver.find_element_by_id("home_search").click()
        self.search.search(key,stocktype,expect_price)

class TestXueqiuHome:

    def setup_class(self):
        self.xueqiuinit = XueqiuInit()
        self.xueqiuhome = XueqiuHomePage(self.xueqiuinit.driver)

    # 滑动屏幕 appdemo ApiDemos-debug.apk
    def test_swipe(self):
        self.xueqiuhome.swipe()

    # 按窗口百分比定位滑动 ApiDemos-debug.apk
    def test_swipe_percent(self):
        self.xueqiuhome.swipe_percent()

    # 根据uiautomator定位滑动 ApiDemos-debug.apk
    def test_uiautomator(self):
        self.xueqiuhome.uiautomator()





