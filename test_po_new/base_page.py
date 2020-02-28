from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
    # 封装找到元素方法
    def find(self, elementby, value):
        return self.driver.find_element(elementby, value)

    # 封装  通过js，进行点击事件
    def check_by_js(self, elementby, value):
        #WebDriverWait(self.driver, 10,1,ignored_exceptions=(TimeoutException)).until(expected_conditions.element_to_be_clickable((elementby, value)))
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(elementby, value))

