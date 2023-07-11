import pandas as pd
from pandas import ExcelWriter


filepath = 'C:\\pythonprojs\\data\\data_sheet.xlsx'
out_file_path3 = 'C:\\pythonprojs\\data\\data_sheet3.xlsx'

dfs = pd.read_excel(filepath, sheet_name=None)

df_scenarios = dfs.get("Scenarios_copy")
df_sheet1 = dfs.get("Google")
print(df_sheet1)
df_sheet2 = dfs.get("FDIC Check")
print(df_sheet2)

writer = ExcelWriter(out_file_path3)
df_sheet1.to_excel(writer, 'Google')
df_sheet2.to_excel(writer, 'FDIC Check')
writer.close()
