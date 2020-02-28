from time import sleep

from selenium.webdriver.common.by import By

from test_po_new.base_page import BasePage


class ProfilePage(BasePage):
    _btnedit = (By.CSS_SELECTOR,".qui_btn.ww_btn.js_edit")
    _username = (By.NAME, "username")
    _btnsave = (By.CSS_SELECTOR, '.qui_btn.ww_btn.ww_btn_Blue.js_save')

    def edit_member(self,username):
        #点击编辑按钮
        self.find(*self._btnedit).click()
        sleep(1)
        # 更新用户名
        self.find(*self._username).clear()
        self.find(*self._username).send_keys(username)
        self.check_by_js(*self._btnsave)
        sleep(2)

    def enable(self):
        pass

    def disable(self):
        pass

    def delete_member(self):
        pass
