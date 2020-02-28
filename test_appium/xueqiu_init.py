from time import sleep

from appium import webdriver
from time import sleep

from appium import webdriver
import pytest
from hamcrest import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class XueqiuInit:
    def __init__(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        # caps["appPackage"] = "io.appium.android.apis"
        # caps["appActivity"] = ".ApiDemos"
        caps['automationName'] = 'uiautomator2'
        caps["autoGrantPermissions"] = True
        #caps["newCommandTimeout"] = 20000
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)
        # print(self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView[2]").location)
        # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView[2]").click()
        # print(self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView").location)
        # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ImageView").click()

    def quit(self):
        self.driver.quit()
