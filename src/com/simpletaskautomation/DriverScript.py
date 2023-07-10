import unittest

import pandas as pd

from src.com.simpletaskautomation.BasePage import BasePage


class DriverScript(BasePage):

    def test_execution(self):

        try:
            with pd.ExcelWriter(self.out_file_path, mode="a", engine="openpyxl") as writer:
                # Scenarios iteration
                for index, row in self.df_scenarios.iterrows():
                    print(row["Scenario Name"], row["Execute"], row['URL'], row)

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
                        print(row1["Status"])

                    self.df_sheet.to_excel(writer, sheet_name=test_sheet_name, index=False)
                    self.df_scenarios.at[index, 'Status'] = "Completed"

                    self.driver.close()
        except Exception as err:
            print("Exception:", err)

    def tearDown(self):
        print("tear down closed.")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
