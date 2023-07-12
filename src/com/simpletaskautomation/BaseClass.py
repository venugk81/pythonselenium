import unittest

import pandas as pd


class BaseClass(unittest.TestCase):

    def setUp(self):
        self.filepath = 'C:\\pythonprojs\\data\\data_sheet.xlsx'
        self.out_file_path = 'C:\\pythonprojs\\data\\data_sheet2.xlsx'
        self.out_file_path3 = 'C:\\pythonprojs\\data\\data_sheet3.xlsx'
        try:
            self.df = pd.read_excel(self.filepath, sheet_name=None)
            self.keys = self.df.keys()
            print(self.keys)
            print(type(self.keys))
            for key in self.keys:
                print("Key:", key)

            self.df_scenarios = self.df.get("Scenarios_copy")
            self.df_scenarios = self.df_scenarios[self.df_scenarios["Execute"].str.contains("Y")]
            print("scenarios: \n", self.df_scenarios)
            # self.df_scenarios.to_excel(self.out_file_path, sheet_name="Scenarios_copy", index=False, header=True)
            # print(self.df)
        except Exception as exp:
            print(exp)

    def tearDown(self):
        print(" tear down..")

