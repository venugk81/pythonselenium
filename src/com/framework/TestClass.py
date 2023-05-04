import unittest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from src.com.framework.BasePage import BaseClass


class TestClass(BaseClass):
    txt_name = "//input[contains(@name, 'name')]"

    def test_method(self):
        search_bar = self.is_element_clickable(self.driver.find_element(By.XPATH, self.txt_name), 10)
        # search_bar = self.driver.find_element(By.XPATH, self.txt_name)

        search_bar.clear()
        search_bar.send_keys("getting started with python")
        print(self.driver.current_url)
        print("Test method is executed..")

    if __name__ == '__main__':
        unittest.main()
