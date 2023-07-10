import time

from selenium.webdriver.common.by import By
from src.com.simpletaskautomation.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class BasePage(BaseClass):

    def get_driver(self, url):
        print("driver is initialized")
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        print(self.driver.title)
        time.sleep(10)
        return self.driver

    def close_driver(self):
        if self.driver is not None:
            self.driver.close()
        print("driver is closed")

    def quit_driver(self):
        if self.driver is not None:
            self.driver.quit()
        print("driver is terminated")

    def click(self, ele):
        self.ele.click()

    def type(self, ele, value):
        self.ele.clear()
        self.ele.send_keys(value)

    def is_element_clickable(self, element, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.element_to_be_clickable(element))

    def is_element_visible(self, by, value, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.visibility_of_element_located(by, value))
