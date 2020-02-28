from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_po_new.base_page import BasePage
from test_po_new.sucai_page import SucaiPage


class ManagetoolsPage(BasePage):
    _btn_managetools = (By.XPATH, '//nav/a[contains(@id,"menu_manageTools")]')

    #传入管理工具的模块名称    成员加入、通讯录同步、素材库等
    def choosetool(self,key):
        self.check_by_js(*self._btn_managetools)
        self.find(By.PARTIAL_LINK_TEXT,str(key)).click()