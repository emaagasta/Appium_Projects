
import time
import unittest

from Calculator_Demo.Settup_Connection.Driver_Option import *
from Calculator_Demo.Page.Calculator import *

class test_running(unittest.TestCase):

    Test_case.__test__ = False

    # variabel global
    driver = Appium_Driver_test().setup()
    aritmatika = Test_case(driver)

    def test_sum(self):
        self.driver.implicitly_wait(5)
        num_1= self.aritmatika.input_1("1")
        operation_sum = self.aritmatika.op_sum()
        num_2 = self.aritmatika.input_2("2")
        operation_equal = self.aritmatika.op_equal()

        result = self.aritmatika.get_text()
        if result:
            return self.assertIn(3,result)

    def test_min(self):
        self.driver.implicitly_wait(5)
        num_1 = self.aritmatika.input_1("9")
        operation_sum = self.aritmatika.op_min()
        num_2 = self.aritmatika.input_2("5")
        operation_equal = self.aritmatika.op_equal()

        result = self.aritmatika.get_text()
        if result:
            return self.assertIn(4, result)


    if __name__ == '__main__':
        unittest.main()

