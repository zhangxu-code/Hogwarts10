from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver

from test_po_new.base_page import BasePage
from test_po_new.managetools_page import ManagetoolsPage
from test_po_new.sucai_page import SucaiPage
from test_po_new.wework_page import Wework


class TestManagetools():
    def setup_class(self):
        self.driver = Wework()
        self.mtools = ManagetoolsPage(self.driver.driver)
        self.sucai = SucaiPage(self.driver.driver)

    def teardown_class(self):
        self.driver.quit()

    # 素材库
    def test_cucai_picture(self):
        """
        测试-上传图片
        """
        self.mtools.choosetool(key="素材库")
        self.sucai.add_picture(picturepath="/Users/duxiuyan/PycharmProjects/Hogwarts10/image/20131204184148_hhXUT.jpeg")
