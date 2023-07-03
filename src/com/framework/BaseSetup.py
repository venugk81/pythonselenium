import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BaseSetup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://register.rediff.com/register/register.php?FormName=user_details")
        self.driver.implicitly_wait(10)
        print(self.driver.title)
        print("driver is initialized..")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("driver instance terminated")

    def test_method(self):
        print("method")

# if __name__ == '__main__':
#     unittest.main()

# python -m unittest UnitTestSample.py
