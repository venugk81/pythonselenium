import time


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BaseClass:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(10)
        print(self.driver.title)
        time.sleep(10)

    def quit(self):
        self.driver.close()
        self.driver.quit()
        print("close and quit driver")

    def get_driver(self):
        return self.driver

    def get_element(self, str_by_type, str_by_value):
        match str_by_type:
            case "xpath":
                return self.driver.find_element(By.XPATH, str_by_value)
            case "name":
                return self.driver.find_element(By.NAME, str_by_value)
            case default:
                return None

    def clic_element(self, ele):
        self.ele.click()

    def click(self, ele):
        self.ele.click()

    def is_element_clickable(self, element, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.element_to_be_clickable(element))

    def is_element_visible(self, by, value, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.visibility_of_element_located(by, value))


# bc = BaseClass()
# x = bc.get_element("name", "q")
# x.send_keys("testing")
# x.submit()
# bc.quit()
