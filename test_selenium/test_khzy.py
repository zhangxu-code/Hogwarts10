import configparser
import os
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestKhzy:
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ["HOME"],"iselenium.ini"))
        return config

    def setup(self):
        # #使用docker容器的Hub 和 node 启动远程浏览器
        # self.driver = webdriver.Remote("http://localhost:5001/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
        # self.driver.get("https://testerhome.com")
        # self.driver.implicitly_wait(10)

        # #单独使用浏览器 启动
        # self.driver = webdriver.Chrome()
        # self.driver.get("https://testerhome.com")
        # self.driver.implicitly_wait(5)

        #通过jenkins启动
        config = self.get_config()#获取chromedriver路径
        #控制是否采用无界面形式运行
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless == None
            print("没有配置环境变量 using_headless,按照有界面方式运行")
        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == "true":
            print("使用无界面方式运行")
            chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(executable_path=config.get('driver','chrome_driver'),options=chrome_options)
        self.driver.get("https://testerhome.com")
        self.driver.set_window_size(1366, 768)#页面复杂的需要加上这句
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

       #浏览最新帖其中的一个
    # def test_newtizi(self):
    #     sleep(5)
    #     self.driver.find_element_by_partial_link_text("社区").click()
    #     sleep(5)
    #     self.driver.find_element_by_partial_link_text("最新发布").click()
    #     sleep(5)
    #     WebDriverWait(self.driver,15).\
    #         until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'.title a[title*="有道云外"]')))
    #
    # #社团访问霍格沃兹测试学院，断言未登录是被拒绝的
    # def test_nologin_calltesterhome(self):
    #     sleep(5)
    #     self.driver.find_element_by_partial_link_text("社团").click()
    #     sleep(5)
    #     self.driver.find_element(By.CSS_SELECTOR,'.media-heading a[title*="霍格沃兹测试学院(hogwarts)"').click()
    #     sleep(5)
    #     self.driver.find_element(By.CSS_SELECTOR,'.title a[href*="/topics/21374"]').click()
    #     sleep(5)
    #     assert "访问被拒绝" in self.driver.page_source
    #
    #     # 错误用户名和密码登陆并断言
    #     self.driver.find_element(By.NAME,'user[login]').send_keys("duxiuyan160")#输入用户名
    #     self.driver.find_element(By.NAME,'user[password]').send_keys("123456")#输入密码
    #     sleep(5)
    #     self.driver.find_element(By.NAME,'commit').click()
    #     sleep(5)

    #     #取登录返回的信息并断言
    #     assert "您的帐号已被暂时锁定" or "用户名或密码错误" in self.driver.find_element(By.CSS_SELECTOR, '.alert-warning').text

    #搜索”测试媛“，找到成立的那个帖子，进去后断言标题与搜索出来的标题是对应的

    # #@pytest.mark.repeat(3)
    def test_search(self):
        sleep(5)
        self.driver.find_element(By.NAME,"q").click()
        self.driver.find_element(By.NAME,"q").send_keys("测试媛")
        self.driver.find_element(By.NAME,"q").send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH,'//div/a[contains(@href,"/topics/4331")]').click()
        sleep(2)
        assert "测试媛组织成立啦" in self.driver.page_source

    # def test_baidu(self):
    #     sleep(3)
    #     self.driver.find_element_by_id("kw").send_keys("大宝")
    #     self.driver.find_element_by_id("kw").send_keys(Keys.ENTER)
    #     #assert "大宝" in self.driver.page_source
