from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def find(self,elementby,value):
        return self.driver.find_element(elementby,value)

    def search(self,keyword):
        self.find(By.ID,"search_input_text").send_keys(keyword)
        return self

    def select(self,index):
        self.driver.find_elements_by_id("name")[index].click()
        return self

    def get_price(self,stocktype):
        price = float(self.driver.find_element_by_xpath(
            "//*[contains(@resource-id,'stockCode') and @text='" + stocktype + "']/../../.."
                                                                               "//*[contains(@resource-id,'current_price')]").text_locator)
        return price

    def get_name(self):
        return self.driver.page_source
