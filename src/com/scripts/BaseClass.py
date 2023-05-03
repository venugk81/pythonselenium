from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BaseClass:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(10)
        print(self.driver.title)

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


# bc = BaseClass()
# x = bc.get_element("name", "q")
# x.send_keys("testing")
# x.submit()
# bc.quit()
