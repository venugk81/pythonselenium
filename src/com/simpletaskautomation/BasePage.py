import time

from selenium.webdriver.common.by import By
from src.com.simpletaskautomation.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pandas import ExcelWriter


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

    def submit(self, ele, value):
        self.ele.send_keys(value)
        self.ele.submit()

    def type(self, ele, value):
        self.ele.clear()
        self.ele.send_keys(value)

    def is_element_clickable(self, element, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.element_to_be_clickable(element))

    def is_element_visible(self, by, value, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.visibility_of_element_located(by, value))

    def get_element_by_xpath(self, locator_value):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.visibility_of_element_located(By.XPATH, locator_value))

    def type_submit(self, df_row):
        self.driver.find_element(By.XPATH, df_row['xpath']).send_keys(df_row['Data'])
        self.driver.find_element(By.XPATH, df_row['xpath']).submit()

    def perform_actions(self, df_test):
        action = df_test['Action']
        match action:
            case "type_submit":
                self.type_submit(df_test)

    def execute_script(self):
        try:
            writer = ExcelWriter(self.out_file_path3)
            for index, row in self.df_scenarios.iterrows():
                print(row["Scenario Name"], row["Execute"], row['URL'], row)
                # driver initialization
                self.chrome_driver = self.get_driver(row['URL'])
                test_sheet_name = row["SheetName"]
                print("execute test steps for ", test_sheet_name)
                self.df_sheet = self.df.get(test_sheet_name)

                self.df_sheet = self.df_sheet[self.df_sheet["Execute"].str.contains("Y")]
                print("Test cases: \n", self.df_sheet)
                # Test Tabs iteration
                for index1, row1 in self.df_sheet.iterrows():
                    print(row1["Step"], row1["Action"], row1['xpath'], row1['Data'])
                    self.df_sheet.at[index1, 'Status'] = "Pass"
                    print("row1['Status']:", row1["Status"])
                    self.perform_actions(row1)
                self.df_sheet.to_excel(writer, test_sheet_name)
                self.df_scenarios.at[index, 'Status'] = "Completed"
            self.df_scenarios.to_excel(writer, 'Scenarios')
            self.driver.close()
            writer.close()
        except Exception as exp:
            print(exp)
