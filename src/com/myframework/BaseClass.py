import unittest
from selenium import webdriver
import pandas as pd


class BaseClass(unittest.TestCase):
    filepath = 'C:\\pythonprojs\\data\\data_sheet.xlsx'

    def setUp(self):
        try:
            self.df = pd.read_excel(self.filepath, sheet_name=None)
            self.keys = self.df.keys()
            print(self.keys)
            print(type(self.keys))
            for key in self.keys:
                print("Key:", key)

            self.df_scenarios = self.df.get("Scenarios_copy")
            self.df_scenarios = self.df_scenarios[self.df_scenarios["Execute"].str.contains("Y")]
            print("scenarios: ", self.df_scenarios)

            # print(self.df)
        except Exception as exp:
            print(exp)

    def tearDown(self):
        self.driver.quit()
        print("driver is terminated..................")

    def test_method1(self):
        print("--------test Method print-------")
        # print(self.df.get("Google"))
        # //for saving single sheet..
        # self.df1 = self.df.get("Google")
        # self.df1.to_excel("C:\\pythonprojs\\data\\data_sheet1.xlsx", sheet_name="Google", index=False, header=True)

        try:

            # self.df1 = self.df.get("Google")
            # self.df1.to_excel("C:\\pythonprojs\\data\\data_sheet1.xlsx", sheet_name="Google", index=False, header=True)

            # for saving multiple sheets:
            # with pd.ExcelWriter('C:\\pythonprojs\\data\\data_sheet1.xlsx') as writer:
            #     self.df.to_excel(writer, sheet_name='Google')

            for index, row in self.df_scenarios.iterrows():
                print(row["Scenario Name"], row["Execute"], row['URL'])

                self.driver = webdriver.Chrome()
                self.driver.get(row['URL'])
                self.driver.implicitly_wait(10)
                print(self.driver.title)
                print("driver is initialized..")


        except Exception as err:
            print("Exception:", err)


if __name__ == '__main__':
    unittest.main()
