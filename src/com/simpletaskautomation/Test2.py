import unittest

from src.com.simpletaskautomation.BasePage import BasePage


class SecondTest(BasePage):

    def test_from_SecondTest(self):
        self.execute_script()

    def tearDown(self):
        print(" tear down..")
        # print("tear down closed.")
        # self.driver.quit()


if __name__ == '__main__':
    unittest.main()
