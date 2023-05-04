import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class UpdateTimeEntry(unittest.TestCase):
    url = ""
    txt_name = "//input[contains(@name, 'name')]"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://register.rediff.com/register/register.php?FormName=user_details")
        self.driver.implicitly_wait(10)
        print(self.driver.title)
        print("driver is initialized..")

    def tearDown(self):
        if self.driver is not None:
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()

    def is_element_clickable(self, element, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.element_to_be_clickable(element))

    def is_element_visible(self, by, value, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.visibility_of_element_located(by, value))

    def test_method(self):
        try:
            search_bar = self.is_element_clickable(self.driver.find_element(By.XPATH, self.txt_name), 10)
            # search_bar = self.driver.find_element(By.XPATH, self.txt_name)
            search_bar.clear()
            search_bar.send_keys("getting started with python")
            print(self.driver.current_url)
            print("Test method is executed..")
        except Exception as err:
            print(err + "- WebPage is not loaded")

    if __name__ == '__main__':
        unittest.main()
