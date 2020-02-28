from time import sleep

import pytest
from appium import webdriver
from hamcrest import  *
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestXueqiu:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps['automationName'] = 'UIAutomator2'
        caps["autoGrantPermissions"] = True
        caps["showChromedriverLog"] = True  #打印更细节的chromedriver log
        caps["avd"] = "Pixel_2_API_27"  #自动启动安卓模拟器
        #caps["networkSpeed"] = "gsm"    #模拟器限速
        ##以下两个参数结合着使用，用于不重新启动app
        # caps["dontStopAppOnReset"] = "true"
        # caps["noReset"] = "true"
        # ##用于启动appium加速的设置
        # caps["skipUnlock"] = True
        # caps["skipLogcatCapture"] = True
        # caps["disableAndroidWatchers"] = True
        # caps["ignoreUnimportantViews"] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

        ###有升级按钮时用的代码
        # def click_cancel(x):
        #     size = len(self.driver.find_elements(By.ID,"image_cancel"))
        #     if size >=1:
        #         print("displayed")
        #         self.driver.find_element(By.ID,"image_cancel").click()
        #     else:
        #         print("no displayed")
        #     return size >=1
        # WebDriverWait(self.driver,10,1,ignored_exceptions=[TimeoutException]).until(expected_conditions.visibility_of_element_located((By.ID,"image_cancel")))
        # WebDriverWait(self.driver,5,1,ignored_exceptions=[TimeoutException]).until_not(click_cancel)
        # _el1_click = (By.XPATH,
        #               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout")
        # _el2_click = (By.XPATH,
        #               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout")
        # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout").click()
        # self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout").click()

    def setup(self):
        pass

    def teardown(self):
        self.driver.find_element_by_id("action_close").click()
        pass

    def teardown_class(self):
        sleep(10)
        self.driver.quit()

    @pytest.mark.parametrize("keyword, stock_type, expect_price", [
        ('alibaba', 'BABA', 170),
        ('xiaomi', '01810', 8.5)
    ])
    def test_search(self, keyword, stock_type, expect_price):
        self.driver.find_element_by_id("home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)

    #appium支持的截屏的API
    def test_screenshot(self):
        print(self.driver.start_recording_screen())
        self.driver.save_screenshot("1.png")
        trade = self.driver.find_element(By.XPATH,"//*[@text='交易']")
        trade.screenshot("2.png")
        trade.click()
        sleep(3)
        print(self.driver.stop_recording_screen())

    #appium支持的logr的API
    def test_log(self):
        print(self.driver.log_types)
        print(self.driver.get_log("logcat"))

    #appium支持的网络的API
    def test_network(self):
        self.driver.send_sms("15901273160","hello shixiaojun,I am duxiuyan")
        sleep(2)
        self.driver.make_gsm_call("15901273160","call")

    #appium支持的性能的API
    def test_perf(self):
        print(self.driver.get_performance_data_types())
        sleep(20)
        for p in self.driver.get_performance_data_types():
            print(self.driver.get_performance_data("com.xueqiu.android", p))

    #获取短信内容，比如取验证码
    def test_notification(self):
        self.driver.open_notifications()
        sleep(3)
        print(self.driver.page_source)
        print(self.driver.find_element(By.ID,"android:id/big_text").text)
        self.driver.keyevent(4)
        #self.driver.launch_app()
