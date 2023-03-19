from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

class Test_case(object):

    def __init__(self, driver: webdriver) -> None:
        self.driver = driver

    def input_1(self,a):
        num1 = self.driver.find_element(AppiumBy.XPATH,"//android.widget.ImageButton[@content-desc='"+a+"']").click()

    def input_2(self,b):
        num2 = self.driver.find_element(AppiumBy.XPATH,"//android.widget.ImageButton[@content-desc='"+b+"']").click()

    def op_sum(self):
        op_sum = self.driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/op_add").click()

    def op_min(self):
        op_min = self.driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/op_sub").click()

    def op_equal(self):
        op_equal = self.driver.find_element(AppiumBy.ID, "com.google.android.calculator:id/eq").click()

    def get_text(self):
        self.driver.implicitly_wait(10)
        result = self.driver.find_element(AppiumBy.ID,"com.google.android.calculator:id/result_final").text







