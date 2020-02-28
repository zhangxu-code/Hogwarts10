from time import sleep

from selenium.webdriver.common.by import By

from test_po_new.base_page import BasePage
from test_po_new.profile_page import ProfilePage
from test_po_new.wework_page import Wework


class ContactPage(BasePage):
    _btn_contacts = (By.XPATH, '//nav/a[contains(@id,"menu_contacts")]')
    _btn_add = (By.XPATH, '//div/div/div/a[contains(@class,"qui_btn ww_btn js_add_member")]')
    _username = (By.NAME, "username")
    _englishname = (By.NAME, "english_name")
    _memberAdd_acctid = (By.NAME, "acctid")
    _sex = (By.XPATH, '//label/input[@value=2]')
    _phone = (By.NAME, "mobile")
    _telephone = (By.NAME, "ext_tel")
    _email = (By.NAME, "alias")
    _address = (By.NAME, "xcx_corp_address")
    _title = (By.NAME, "position")
    _shenfen = (By.CSS_SELECTOR, '.js_identity_stat')
    _btnsave = (By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save')
    _add_member_tip = (By.CSS_SELECTOR, '.ww_tip.success')
    _searchmember = (By.CSS_SELECTOR, ".qui_inputText.ww_inputText.ww_searchInput_text")

    _username_tips = (By.CSS_SELECTOR,'.ww_inputWithTips_tips')


    def __init__(self,wework:Wework):
        self.driver = wework.driver
    #添加成员
    def add_member(self,username,englishname,acctid,phone,tel,email,address,title):
        self.find(*self._btn_contacts).click()
        sleep(5)
        self.check_by_js(*self._btn_add)
        sleep(2)
        # 填写用户名
        self.find(*self._username).send_keys(username)
        # 填写别名
        self.find(*self._englishname).send_keys(englishname)
        # 填写帐户
        self.find(*self._memberAdd_acctid).send_keys(acctid)
        # 选择性别
        self.find(*self._sex).click()
        # 填写手机
        self.find(*self._phone).send_keys(phone)
        # 填写座机
        self.find(*self._telephone).send_keys(tel)
        # 填写邮箱
        self.find(*self._email).send_keys(email)
        # 填写地址
        self.find(*self._address).send_keys(address)
        # 选择部门
        # 填写职务
        self.find(*self._title).send_keys(title)
        # 选择身份
        self.find(*self._shenfen).click()
        sleep(2)
        # 点击保存按钮
        self.check_by_js(*self._btnsave)
        sleep(2)

    # 添加/编辑成员页面保存动作后的提示
    def add_member_tip(self):
        return self.find(*self._add_member_tip).text_locator

    #查询成员
    def search_member(self,key):
        self.find(*self._searchmember).send_keys(key)
        return ProfilePage(self.driver)

    def isnull(self,username):
        self.find(*self._btn_contacts).click()
        sleep(5)
        self.check_by_js(*self._btn_add)
        sleep(2)
        # 填写用户名
        self.find(*self._username).send_keys(username)
        self.find(*self._sex).click()
        return self.find(*self._username_tips).text_locator