from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po_new.base_page import BasePage


class SucaiPage(BasePage):
    _sucailink = (By.PARTIAL_LINK_TEXT, "素材库")
    _picturelink = (By.PARTIAL_LINK_TEXT, "图片")
    _addpicture = (By.CSS_SELECTOR, ".material_upload_input")
    _cancle = (By.CSS_SELECTOR, '.js_uploadProgress_cancel')

    #添加文字
    def add_word(self):
        pass

    #添加图文
    def add_wordandpicture(self):
        pass

    #添加图片
    def add_picture(self,picturepath):
        #点击管理工具页面的素材库
        #self.find(*self._sucailink).click()
        #点击素材页左边导航的图片
        self.find(*self._picturelink).click()

        self.check_by_js(By.CSS_SELECTOR, ".js_upload_file_selector")
        self.find(*self._addpicture).send_keys(picturepath)

        WebDriverWait(self.driver, 15).until \
            (expected_conditions.invisibility_of_element_located(
                (self.find(*self._cancle))))
        self.find(By.CSS_SELECTOR, '.js_next').click()

    #添加语音
    def add_voice(self):
        pass

    #添加视频
    def add_video(self):
        pass

    #添加文件
    def add_file(self):
        pass