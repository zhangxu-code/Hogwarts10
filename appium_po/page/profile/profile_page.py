from appium_po.page.base_page import BasePage


class ProfilePage(BasePage):

    _phone =BasePage.id_locator("rl_login_phone")
    _wechat = BasePage.id_locator("rl_login_wx")
    _weibo = BasePage.id_locator("rl_login_weibo")
    _qq = BasePage.id_locator("rl_login_qq")
    _phone_input = BasePage.id_locator("register_phone_number")
    _phone_captch = BasePage.id_locator("register_code")
    _phone_next = BasePage.id_locator("button_next")
    _md_content = BasePage.id_locator("md_content")
    _toast = BasePage

    def login_by_phone(self,phone,captch):
        self.find(self._phone).click()
        self.find(self._phone_input).send_keys(phone)
        self.find(self._phone_captch).send_keys(captch)
        self.find(self._phone_next).click()
        return self

    def get_tips(self):
        return self.find(self._md_content).text

    def login_by_wechat(self):
        self.find(self._wechat).click()
        return self

    def get_toast(self):
        return self.find(self.toast_locator()).text
    def login_by_weigo(self):
        pass

    def login_by_qq(self):
        pass
