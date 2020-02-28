from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from appium_po.page.base_page import BasePage


class TradePage(BasePage):
    #_a_open = (By.XPATH,"//*[@text='蛋卷基金安全开户']")
    _a_open = (By.XPATH, "//*[@text='A股开户']")
    _phone = (By.ID,"phone-number")
    _code = (By.ID,"code")

    def goto_hs(self):
        self.driver.find_element(By.XPATH,"//*[@text='基金']").click()
        self.driver.find_element(By.XPATH,"//*[@text='沪深']").click()

    def a_open(self,phone,code):
        self.driver.find_element(*self._a_open).click()
        WebDriverWait(self.driver,10,1).until(lambda x:"WEBVIEW_com.xueqiu.android" in self.driver.contexts)
        # print("=========webview load")
        # #返回的是不带webview的组件
        # print(self.driver.page_source)
        #将按原生组件赋值
        # self.driver.find_element(By.ID,"et_telephone").send_keys(phone)
        # self.driver.find_element(By.ID,"et_password").send_keys(code)
        #返回的是带有webview组件树
        self.driver.switch_to.context("WEBVIEW_com.xueqiu.android")
        # print("==================webview enter")
        # #返回Html
        # print(self.driver.page_source)
        #WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(self._a_open))
        # print("==================after")
        # print(self.driver.page_source)
        WebDriverWait(self.driver, 30,1).until(expected_conditions.visibility_of_element_located(self._phone))
        #todo,待Chromium62版本有了这后再用html元素定位赋值
        self.driver.find_element(*self._phone).send_keys(phone)
        self.driver.find_element(*self._code).send_keys(code)


