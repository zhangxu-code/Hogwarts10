from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestMicroProgram:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "2142f77"
        caps["appPackage"] = "com.tencent.mm"#com.tencent.mm
        caps["appActivity"] = ".ui.LauncherUI"#.ui.LauncherUI
        caps["noReset"] = True
        #caps['automationName'] = 'UIAutomator2'
        caps["chromedriverExecutable"] = '/Users/duxiuyan/projects/chromedriver/2.39/chromedriver'
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def teardown_class(self):
        self.driver.quit()

    def test_xueqiu_micro_grogram(self):
        print(self.driver.page_source)
        WebDriverWait(self.driver,20,1).until(lambda x:"文件传输助手" in self.driver.page_source)
        self.driver.find_element(By.XPATH,"//*[@text='文件传输助手']").click()
        # self.driver.find_element(By.XPATH, "//*[@text='雪球']").click()
        # for i in range(30):
        #     print(i)
        #     print(self.driver.page_source)
        # #self.driver.find_element(By.XPATH,"//*[@text='文件传输助手']").click()
        # #self.driver.find_element(MobileBy.ACCESSIBILITY_ID,"文件传输助手").click()
        # #self.driver.find_element(By.XPATH,"//*[@text='雪球']").click()


