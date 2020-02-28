#from appium.webdriver.webdriver import WebDriver
from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def find(self,elementby,value):
        #self.driver.execute_script("arguments[0].click()", self.driver.find_element(elementby, value))
        return self.driver.find_element(elementby,value)

    def waitandclick(self,elementby,value):
        WebDriverWait(self.driver, 10, 1, ignored_exceptions=(TimeoutException)).until(
            expected_conditions.element_to_be_clickable((elementby, value)))
        self.find(elementby,value).click()

