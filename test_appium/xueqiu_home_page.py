from selenium.webdriver.common.by import By

from test_appium.base_page import BasePage
from test_appium.xueqiu_init import XueqiuInit


class XueqiuHomePage(BasePage):
    def __init__(self,driver):
        self.driver = driver
    #滑动屏幕 appdemo ApiDemos-debug.apk
    def swipe(self):
        self.driver.swipe(500, 900, 100, 200, 1000)
        self.driver.find_element_by_accessibility_id("Views").click()

        for i in range(5):
            self.driver.swipe(500, 900, 100, 200, 1000)

    #按窗口百分比定位滑动 ApiDemos-debug.apk
    def swipe_percent(self):
        windowsize = self.driver.get_window_size()
        width = windowsize["width"]
        height = windowsize["height"]
        self.driver.swipe(width*0.8, height*0.8, width*0.2, height*0.2, 1000)
        self.driver.find_element_by_accessibility_id("Views").click()

        for i in range(5):
            self.driver.swipe(width * 0.8, height * 0.8, width * 0.2, height * 0.2, 1000)

    #根据uiautomator定位滑动 ApiDemos-debug.apk
    def uiautomator(self):
        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().scrollable(true).instance(0))'
                                                        '.scrollIntoView('
                                                        'new UiSelector().text("Views").instance(0));').click()

        self.driver.find_element_by_android_uiautomator('new UiScrollable('
                                                        'new UiSelector().scrollable(true).instance(0))'
                                                        '.scrollIntoView('
                                                        'new UiSelector().text("Tabs").instance(0));').click()