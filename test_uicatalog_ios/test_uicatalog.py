from appium import webdriver
import unittest


class TestUicata:
    def setup(self):
        caps = {}
        caps["platformName"] = "ios"
        caps["deviceName"] = "小杜的手机"
        caps["platformVersion"] = "13.3"
        caps["udid"] = "45d4d762fe59e8a1d405c8b28cf91a87cc25ca44"
        caps["xcodeOrgId"] = "JW64U698RZ"  # YKARBYYGGZ
        caps["xcodeSigningId"] = "iPhone Developer"
        #caps["bundleId"] = "com.example.apple-samplecode.UICatalognaruto.xiaodu202001"
        #caps["usePrebuiltWDA"] = "true"
        caps["automationName"] = "XCUITest"
        caps["app"] = "/Users/duxiuyan/Library/Developer/Xcode/DerivedData/UIKitCatalog-ciugdkyyljvmfqcrnaauhptgkkiz/Build/Products/Debug-iphoneos/UIKitCatalog.app"
        #模拟器
        # caps = {}
        # caps["platformName"] = "ios"
        # caps["platformVersion"] = "13.3"
        # caps["deviceName"] = "iPhone 11"
        # caps["app"] = "/Users/duxiuyan/Library/Developer/Xcode/DerivedData/UIKitCatalog-ciugdkyyljvmfqcrnaauhptgkkiz/" \
                      #"Build/Products/Debug-iphonesimulator/UIKitCatalog.app"


        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

    def test_buttons(self):
        print()
        # self.driver.find_element_by_accessibility_id("Buttons").click()
        # assert "More Info" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()