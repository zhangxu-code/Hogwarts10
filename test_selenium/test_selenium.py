import logging
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

#logging.basicConfig(level=logging.DEBUG)
from selenium.webdriver.support.wait import WebDriverWait


class TestSelenium:
    def setup(self):
        optionchrome = webdriver.ChromeOptions()
        optionchrome.debugger_address = "127.0.0.1:9222"

        self.driver = webdriver.Chrome(options=optionchrome)
        self.driver.implicitly_wait(3)
        self.driver.get("https://testerhome.com")

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get("http://www.baidu.com")

    def test_firefox(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://testerhome.com")

    def test_search(self):
        self.driver.get('https://testerhome.com')
        search=self.driver.find_element_by_name("q")
        search.send_keys("selenium")

    # def test_1122(self):
    #     self.driver.find_element(By.NAME, "q").click()
    #     #搜到先到先得帖子
    #     self.driver.find_element(By.NAME, "q").send_keys("先到先得")
    #     self.driver.find_element(By.NAME, "q").send_keys(Keys.ENTER)
    #     #点击先到先得帖子链接
    #     self.driver.find_element(By.CSS_SELECTOR, '.title [href*="/topics/19682"]').click()
    #     #打开第二个链接
    #     #self.driver.find_element(By.XPATH, '//p[contains(text(),"问卷")]/a').click()
    #     self.driver.find_element(By.CSS_SELECTOR,'[href*="/topics/21405"]')
    #     sleep(3)
    #
    #     for w in self.driver.window_handles:
    #         logging.info(w)
    #     logging.info(self.driver.title)
    #     self.driver.switch_to_window(self.driver.window_handles[-1])
    #     logging.info(self.driver.title)
    #
    #     ActionChains(self.driver).
    #


        #self.driver.find_element(By.XPATH, '//ol/li/a[contains(@href,"[jvm-sandbox-repeater 学习笔记][入门使用篇] 1 安装与启动")]').click()

    def test_1124(self):
        self.driver.find_element(By.NAME,"q").click()
        self.driver.find_element(By.NAME,"q").send_keys("支付宝开源的 Android 专项测试工具")
        self.driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR,'.title [href*="topics/19832"]').click()
        #点击目录按钮
        self.driver.find_element(By.CSS_SELECTOR,'.toc-container button[datas-toggle*="dropdown"]').click()
        sleep(3)
        #从目录中选中一项进行点击查看
        #aas = self.driver.find_element(By.XPATH,'//div/ul/li[contains(@class,"toc-item toc-level")]')
        #topics = self.driver.find_elements_by_xpath('//div/div/ul[@class="list"]/li')
        # #print(topics)
        # for a in topics:
        #     self.driver.set_window_size(600,800)
        #     a.click()
        #     sleep(2)
        #
        # #     topic.click()
        self.driver.find_element(By.XPATH,'//div/ul/li[contains(@class,"toc-item toc-level")][2]').click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,600)")
        sleep(2)

    def test_explicit_wait(self):
        self.driver.find_element_by_partial_link_text("社区").click()
        #sleep(2)
        self.driver.find_element_by_partial_link_text("最新发布")
        WebDriverWait(self.driver,15).until\
            (expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".title a")))
        sleep(5)

    def test_form_login(self):
        pass
    



