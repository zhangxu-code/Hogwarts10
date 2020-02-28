from selenium import webdriver


class Wework:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        url = "https://work.weixin.qq.com/wework_admin/loginpage_wx"
        self.driver.get(url)
        addcookies = {
            "wwrtx.d2st": "a6630671",
            "wwrtx.sid": "TTtkFFYVLizAtcJmpWktu1gEf0bryys5WOl3QqQ0JINFjtliQ6Q0_2qYlxl9Pk2M",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324961087009",
            "wxpay.vid": "1688853757250284",
            "wwrtx.vst": "JnWMwzmt3FqVDN1QXBMsboPLWMR0Tyep-bEJuLCtZIHKq6kJsKv6nQKKyQML1rCvPUSEDZidPgx7Kp9Biehc5OgH8gX-mhoxuKifvhiNXEnkCugJFzz0NqGD4gifRsNuV47Hwp4y4mHzyL-tdtK-LxHBMPx0xVt7giLBqhXjHkLe_KcWTwKJKfYCKkFzJyXXW6lWYsPTRKSL-rBIsKbqQPXa0mVib14iNn7Gu_Tsu9DypZwjNbnE0D78FusggZoWcOHaI6tTxzHsQn7PJDXdyQ",
            "wwrtx.vid": "1688853757250284",
        }
        for k, v in addcookies.items():
            self.driver.add_cookie({"name": k, "value": v})
        self.driver.get(url)

    def quit(self):
        self.driver.quit()