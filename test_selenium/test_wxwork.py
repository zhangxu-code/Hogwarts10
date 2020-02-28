from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWxwork:
    def setup(self):
        # optionschrome = webdriver.ChromeOptions()
        # optionschrome.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=optionschrome)

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

        url = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
        self.driver.get(url)
        addcookies = {
            "wwrtx.d2st": "a9501192",
            "wwrtx.sid": "TTtkFFYVLizAtcJmpWktuzmQiiiyA8ONTV8rEybLGXbqiUbi16uf_mT7DIBvZmJu",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324961087009",
            "wxpay.vid": "1688853757250284",
            "wwrtx.vst": "26YCZdldqTaQfJSXNVeEGv4cFdGCmXL0vnz0DzLnrXu5a8dXGr_Fm8dNtZRvLaGEtFsCjEmPr7LSbeyomLEECYXwowy8UdN7xEhWpF9b_O3CR-UqGZWcJ6VErbst5iCG6QEl0uq2H5z4xsUePkNlt5jeB8mizSxZueU-17THNKRUNKclVYcoXw9-PiQFJSC3A-tr-gftw_YL7B6aKY9FiQXRXcvBn8irhMpCRP9jsAJisLS4MMjsYczSXHi0PDyGqNhUoy1CBbUIJW1Y5ZmfFw",
            "wwrtx.vid": "1688853757250284"
        }
        for k, v in addcookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)

    def test_upload_file(self):
        # element = self.driver.find_element(By.CSS_SELECTOR,".js_upload_file_selector")
        #         # self.driver.execute_script("arguments[0].click()",element)
        self.check_by_js(By.CSS_SELECTOR,".js_upload_file_selector")

        self.driver.find_element(By.CSS_SELECTOR,".material_upload_input").\
            send_keys("/Users/duxiuyan/PycharmProjects/Hogwarts10/image/20131204184148_hhXUT.jpeg")

        print(self.driver.page_source)
        WebDriverWait(self.driver,15).until\
            (expected_conditions.invisibility_of_element_located((self.driver.find_element(By.CSS_SELECTOR,'.js_uploadProgress_cancel'))))
        self.driver.find_element(By.CSS_SELECTOR,'.js_next').click()

    def check_by_js(self,elementby,value):
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(elementby,value))

    def test_add_member(self):
        #填写用户名
        self.driver.find_element(By.ID,"username").send_keys("史晓军")
        #填写别名
        self.driver.find_element(By.ID,"memberAdd_english_name").send_keys("大军")
        #填写帐户
        self.driver.find_element(By.ID,"memberAdd_acctid").send_keys("shixiaojun162")
        #选择性别
        self.driver.find_element(By.XPATH,'//label/input[@value=2]').click()
        #填写手机
        self.driver.find_element(By.ID,"memberAdd_phone").send_keys("15901273167")
        #填写座机
        self.driver.find_element(By.ID,"memberAdd_telephone").send_keys("010-82345678")
        #填写邮箱
        self.driver.find_element(By.ID,"memberAdd_mail").send_keys("shixiaojun@qq.com")
        #填写地址
        self.driver.find_element(By.ID,"memberEdit_address").send_keys("河北省三河市燕郊开发区首尔甜城林荫大道25号楼1单元2501")
        #选择部门

        #填写职务
        self.driver.find_element(By.ID,"memberAdd_title").send_keys("项目经理")
        #选择身份
        self.driver.find_element(By.CSS_SELECTOR,'.js_identity_stat').click()
        sleep(2)
        #点击保存按钮
        #self.driver.execute_script("window.scrollTo(0,600)")
        #self.driver.find_element((By.CSS_SELECTOR,'.qui_btn.ww_btn.js_btn_save'[1])).click()
        self.check_by_js(By.CSS_SELECTOR,'.qui_btn.ww_btn.js_btn_save')
        sleep(2)

    #利用cookie越过扫码
    def test_cookie(self):
        url = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
        #self.driver.get(url)
        addcookies = {
            "wwrtx.d2st":"a7818017",
            "wwrtx.sid":"TTtkFFYVLizAtcJmpWktuyDIBnkZ8tPjD53ZuVYrp0C0dk0uGpFGTrVpyo9vncKV",
            "wwrtx.ltype":"1",
            "wxpay.corpid":"1970324961087009",
            "wxpay.vid":"1688853757250284",
            "wwrtx.vst":"c0OlyLbhA6pBhT2fhnSR6WEaqZAslFDTf9-nupiuUIC_WtSvtcuqXZlnQ75Ri91qdpjbSuyeFMU6ZvDIcZCXS2xdemghQYJ9BauAMaYT216XX6kP_nzfKt9ipKK9n8uMi7tVX4XFpQUwefuOto02GsseOy-3s7ilAPT_fUfEjyxuslsAoW2DTIVmJdQb0JynYQV35nfXEh0b-13wfZisJ1yUNlfpuhVXZWpzlT3EHPl9VaJfUM5aJXPwsKD7dei2HmiXEMACE98MmS-K_gm0Dg",
            "wwrtx.vid":"1688853757250284",
        }
        for k,v in addcookies.items():
            self.driver.add_cookie({"name":k, "value":v})
        self.driver.get(url)
