import time

from selenium.webdriver.common.by import By
from src.com.simpletaskautomation.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from pandas import ExcelWriter


class BasePage(BaseClass):

    def get_driver(self, url):
        try:
            print("driver is initialized")
            self.driver = webdriver.Chrome()
            self.driver.get(url)
            self.driver.implicitly_wait(10)
            print(self.driver.title)
            time.sleep(10)
        except Exception as exp:
            print("Failed to launch chrome driver:", exp)
            raise
        return self.driver

    def close_driver(self):
        if self.driver is not None:
            self.driver.close()
        print("driver is closed")

    def quit_driver(self):
        if self.driver is not None:
            self.driver.quit()
        print("driver is terminated")

    def click(self, df_row):
        try:
            ele = self.get_element_by_xpath(df_row['xpath'])
            ele.click()
        except Exception as exp:
            print("Element is not found in the DOM or failed to click on the element: ", exp)
            raise

    def submit(self, df_row):
        try:
            ele = self.get_element_by_xpath(df_row['xpath'])
            ele.submit()
        except Exception as exp:
            print("Element is not found in the DOM or failed to submit the element: ", exp)
            raise

    def type(self, df_row):
        try:
            ele = self.get_element_by_xpath(df_row['xpath'])
            ele.clear()
            ele.send_keys(df_row['Data'])
        except Exception as exp:
            print("Element is not found in the DOM or failed to submit the element: ", exp)
            raise

    def sendkeys(self, df_row):
        try:
            ele = self.get_element_by_xpath(df_row['xpath'])
            ele.send_keys(df_row['Data'])
        except Exception as exp:
            print("Element is not found in the DOM or failed to submit the element: ", exp)
            raise

    def is_element_clickable(self, element, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.element_to_be_clickable(element))

    def is_element_visible(self, by, value, time_out):
        wait = WebDriverWait(self.driver, time_out)
        return wait.until(expected_conditions.visibility_of_element_located((by, value)))

    def get_element_by_xpath(self, locator_value):
        wait = WebDriverWait(self.driver, 10)
        return wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator_value)))

    def type_submit(self, df_row):
        # self.driver.find_element(By.XPATH, df_row['xpath']).send_keys(df_row['Data'])
        # self.driver.find_element(By.XPATH, df_row['xpath']).submit()
        try:
            ele = self.get_element_by_xpath(df_row['xpath'])
            ele.send_keys(df_row['Data'])
            ele.submit()
        except Exception as exp:
            print("Element is not found in the DOM ", exp)
            raise

    def perform_actions(self, index1, df_test):
        blnFlag = "Fail"
        action = df_test['Action']
        try:
            match action:
                case "type_submit":
                    self.type_submit(df_test)  # or
                    # exec("self.type_submit(df_test)")
                    time.sleep(3)
                    blnFlag = "Pass"
                case "click":
                    self.click(df_test)
                    time.sleep(10)
                    blnFlag = "Pass"
                case "type":
                    self.type(df_test)
                    blnFlag = "Pass"
                case "sendkeys":
                    self.sendkeys(df_test)
                    blnFlag = "Pass"
                case "selectbyvalue" | "select by value":
                    print("implement select by value")
                    blnFlag = "In Progress"
                case "selectbyindex":
                    print("implement select by index")
                    blnFlag = "In Progress"
                case "selectbytext":
                    print("implement select by text")
                    blnFlag = "In Progress"
        except Exception as exp:
            print("Failed to perform action on element: ", df_test)
            raise
        finally:
            self.df_sheet.at[index1, 'Status'] = blnFlag

    def execute_script(self):
        writer = ExcelWriter(self.out_file_path3)
        try:
            for index, row in self.df_scenarios.iterrows():
                try:
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
                        # self.df_sheet.at[index1, 'Status'] = "Pass"
                        print("row1['Status']:", row1["Status"])
                        self.perform_actions(index1, row1)
                except Exception as exp:
                    print("Exception Occurred1: ", exp)

                finally:
                    self.df_sheet.to_excel(writer, test_sheet_name)
                    self.df_scenarios.at[index, 'Status'] = "Completed"
        except Exception as exp:
            print("Exception occurred2: ", exp)
            raise
        finally:
            self.df_scenarios.to_excel(writer, 'Scenarios')
            writer.close()
            if self.driver is not None:
                self.driver.quit()
                print("quit driver..")


