from appium import webdriver
from selenium.webdriver.common.by import By

from appium_po.page.base_page import BasePage
from appium_po.page.profile.profile_page import ProfilePage
from appium_po.page.stock.search_page import SearchPage
from appium_po.page.trade.trade_page import TradePage


class XueqiuPage(BasePage):
    driver = None
    app = "com.xueqiu.android"
    activity = ".view.WelcomeActivityAlias"
    _home_search = (By.ID,"home_search")
    _myprofile = (By.XPATH,"//*[@text='我的' and contains(@resource-id,'tab_name')]")

    def frist_start(self):
        #设置capbility
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = self.app
        caps["appActivity"] = self.activity
        caps['automationName'] = 'UiAutomator2'
        caps["autoGrantPermissions"] = True
        caps["chromedriverExecutable"] = '/Users/duxiuyan/projects/chromedriver/2.12/chromedriver'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        XueqiuPage.driver = self.driver

    def __init__(self):
        if XueqiuPage.driver == None:
            self.frist_start()
        else:
            self.driver.start_activity(self.app,self.activity) #进入首页

    #我的个人页
    def goto_profile(self):
        self.find(self._myprofile).click()
        return ProfilePage(self.driver)

    #查询功能
    def goto_search(self):
        self.find(self._home_search).click()
        #self.driver.find_element(*self._home_search).click()
        return SearchPage(self.driver)

    #交易页
    def goto_trade(self):
        self.driver.find_element(By.XPATH, "//*[@text='交易' and contains(@resource-id, 'tab_name')]").click()
        return TradePage(self.driver)




