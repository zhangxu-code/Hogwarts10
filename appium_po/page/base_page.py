from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    # 黑名单列表
    black_list=[
        (By.ID,"image_cancel"),
        (By.XPATH,"//*[@class='android.widget.ImageView']"),
        (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout"),
        (By.ID,"ib_close"),
    ]
    # 计数器
    max = 0

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def find(self,locator) -> WebElement: #-> 类型推倒
        #处理弹框  异常处理   动态浮动的元素的处理
        try:
            return self.driver.find_element(*locator)
        except Exception as e:
            if BasePage.max > 5:
                raise  e
            BasePage.max = BasePage.max +1
            for black in self.black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) >= 1:
                    elements[0].click()
            return self.find(locator)

    def size(self,locator) -> int:
        return len(self.driver.find_elements(*locator))

    @classmethod
    def id_locator(cls, value):
        return (By.ID,value)

    @classmethod
    def text_locator(cls, value):
        return (By.XPATH,"//*[@text='%s'] %value")

    @classmethod
    def toast_locator(cls):
        return (By.XPATH,"//*[@class='android.widget.Toast']")
