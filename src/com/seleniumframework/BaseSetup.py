import unittest
from selenium import webdriver
import pandas as pd


class BaseSetup(unittest.TestCase):

    def setUp(self):

        print("i am inside setup method..")
        self.file_name = 'C:\\pythonprojs\\data\\data_sheet.xlsx'
        self.main_sheet = 'Scenarios_copy'
        df = pd.read_excel(self.file_name, sheet_name=self.main_sheet)
        main_df = df[df["Execute"].str.contains("Y|Yes")]
        print(main_df)
        print("main dfs", main_df['SheetName'][0])
        print("main dfs type", type(main_df['SheetName']))
        lt = main_df['SheetName'].tolist()
        print("series to list ", lt)
        try:
            self.data_dict_df = pd.read_excel(self.file_name, sheet_name=lt)
            print(self.data_dict_df.get('FDIC Check'))
            print("google data frame---------")
            print(self.data_dict_df.get('Google'))
        except Exception as err:
            AssertionError(err)



        # self.driver = webdriver.Chrome()
        # self.driver.get("http://register.rediff.com/register/register.php?FormName=user_details")
        # self.driver.implicitly_wait(10)
        # print(self.driver.title)
        # print("driver is initialized..")

    def tearDown(self):
        pass

    def test_method1(self):
        print("method")


if __name__ == '__main__':
    unittest.main()


# //https://sparkbyexamples.com/pandas/pandas-read-excel-multiple-sheets-in-pandas/
# https://sparkbyexamples.com/pandas/pandas-read-excel-multiple-sheets-in-pandas/#:~:text=sheet_name%20param%20on%20pandas.,and%20DF%20for%20Dict%20value.