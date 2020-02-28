import allure
from selenium.webdriver.common.by import By
from test_appium.base_page import BasePage
from test_appium.xueqiu_init import XueqiuInit


class XueqiuMyPage(BasePage):
    _tv_login_phone = (By.ID, "tv_login_phone")
    _tv_login_with_account = (By.ID, "tv_login_with_account")
    _account = (By.ID, "login_account")
    _password = (By.ID, "login_password")
    _btnlogin = (By.ID, "button_next")
    _tips = (By.ID, "md_content")
    _tips_close = (By.ID, "md_buttonDefaultPositive")
    _el1_click = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout")
    _el2_click = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout")
    _el3_click = (By.XPATH,"//android.widget.RelativeLayout[4]/android.widget.ImageView")

    def __init__(self,init:XueqiuInit):
        self.driver = init.driver
        # 初始化时，将页面上弹出来的那些div点击消掉
        self.waitandclick(*self._el1_click)
        self.waitandclick(*self._el2_click)
        self.waitandclick(*self._el3_click)
        # 点击我的-手机号
        self.waitandclick(*self._tv_login_phone)
        # 点击邮箱手机号密码登录
        self.waitandclick(*self._tv_login_with_account)

    def input_phoneandpwd(self, phone, pwd):
        # 输入错误的手机号
        self.find(*self._account).clear()
        self.find(*self._account).send_keys(phone)
        # 输往密码
        self.find(*self._password).clear()
        self.find(*self._password).send_keys(pwd)
        # 点击登录
        self.waitandclick(*self._btnlogin)
        # 点击登录之后的提示框
        self.tips = self.find(*self._tips).text
        self.waitandclick(*self._tips_close)

