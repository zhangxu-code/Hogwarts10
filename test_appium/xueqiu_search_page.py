from time import sleep

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from test_appium.base_page import BasePage
from test_appium.xueqiu_init import XueqiuInit

from hamcrest import *


class XueqiuSearchPage(BasePage):
    _search = (By.ID,"home_search")
    _search_input_text = (By.ID,"search_input_text")
    _el1_click = (By.XPATH,
                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout")
    _el2_click = (By.XPATH,
                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout")
    _el3_click = (By.XPATH, "//android.widget.RelativeLayout[4]/android.widget.ImageView")
    _search_name = (By.ID,"name")
    _search_stockName = (By.ID,"stockName")

    def __init__(self,init:XueqiuInit):
        self.driver = init.driver
        # 初始化时，将页面上弹出来的那些div点击消掉
        # self.waitandclick(*self._el1_click)
        # self.waitandclick(*self._el2_click)
        #print(self.driver.page_source)
        #self.driver.tap([(56, 214), (1384, 326)], 100)

    def search(self,key,stocktype,expect_price):
        #self.driver.tap([(56, 214), (1384, 326)], 100)
        #self.driver.tap([(56, 214), (1384, 326)], 100)
        #self.waitandclick(*self._search)
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'home_search') and contains(@class, 'LinearLayout')]").click()
        self.waitandclick(*self._search_input_text)
        self.find(*self._search_input_text).send_keys(key)
        self.waitandclick(*self._search_name)
        price = self.driver.find_element_by_xpath("//*[contains(@resource-id,'stockCode') and @text='"+stocktype+"']/../../.."
                                                                                                         "//*[contains(@resource-id,'current_price')]").text_locator
        assert_that(float(price), close_to(expect_price, expect_price*0.1))


