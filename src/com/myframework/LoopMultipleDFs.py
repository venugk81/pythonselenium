import unittest
import pandas as pd


class LoopDfs(unittest.TestCase):
    filepath = 'C:\\pythonprojs\\data\\data_sheet.xlsx'
    out_file_path = 'C:\\pythonprojs\\data\\data_sheet2.xlsx'

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
            print("scenarios: \n", self.df_scenarios)
            self.df_scenarios.to_excel(self.out_file_path, sheet_name="Scenarios_copy", index=False, header=True)
            # print(self.df)
        except Exception as exp:
            print(exp)

    def tearDown(self):
        with pd.ExcelWriter('C:\\pythonprojs\\data\\data_sheet1.xlsx') as writer:
            keys = self.df.keys()
            for key in keys:
                df1 = self.df.get(key)
                df1.to_excel(writer, sheet_name=key, index=False)

        print("tear down closed.")





    def test_1(self):
        print("--------test Method print-------")
        try:
            with pd.ExcelWriter(self.out_file_path, mode="a", engine="openpyxl") as writer:
                for index, row in self.df_scenarios.iterrows():

                    print(row["Scenario Name"], row["Execute"], row['URL'], row)
                    test_sheet_name = row["SheetName"]
                    print("execute test steps for ", test_sheet_name)
                    self.df_sheet = self.df.get(test_sheet_name)

                    self.df_sheet = self.df_sheet[self.df_sheet["Execute"].str.contains("Y")]
                    print("Test cases: \n", self.df_sheet)

                    for index1, row1 in self.df_sheet.iterrows():
                        print(row1["Step"], row1["Action"], row1['xpath'], row1['Data'])
                        self.df_sheet.at[index1, 'Status'] = "Pass"
                        print(row1["Status"])
                    self.df_sheet.to_excel(writer,  sheet_name=test_sheet_name, index=False)

        except Exception as err:
            print("Exception:", err)


if __name__ == '__main__':
    unittest.main()
