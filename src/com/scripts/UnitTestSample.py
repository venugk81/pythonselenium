import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class UnitTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(10)
        print(self.driver.title)
        print("driver is initialized..")

    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("driver instance terminated")

    def test_method(self):
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.clear()
        search_bar.send_keys("getting started with python")
        search_bar.send_keys(Keys.RETURN)
        print(self.driver.current_url)


if __name__ == '__main__':
    unittest.main()

# python -m unittest UnitTestSample.py
