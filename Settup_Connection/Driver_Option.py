
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# import sys
# sys.path.append(sys.path[0] + "/....")

class Appium_Driver_test(object):

    driver = None
    
    def setup(self):
        options = UiAutomator2Options()
        options.platformVersion = '11'
        options.platform_name = 'Android'
        options.udid = 'emulator-5554'
        options.app_package = 'com.google.android.calculator'
        options.app_activity = 'com.android.calculator2.Calculator'
        options.no_reset = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=options)
        self.driver.implicitly_wait(30)
        return self.driver

    def tearDown(self):
        self.driver.quit()


