import pandas as pd

file_name='C:\\pythonprojs\\data\\data_sheet.xlsx'
main_sheet = 'Scenarios_copy'
df = pd.read_excel(file_name, sheet_name=main_sheet)
df = df[df["Execute"].str.contains("Y|Yes")]


# https://www.tutorialspoint.com/how-to-save-pandas-data-into-excel-multiple-sheets
# dict_df = pd.read_excel('c:/apps/courses_schedule.xlsx',
#                    sheet_name=['Technologies','Schedule'])
# https://sparkbyexamples.com/pandas/pandas-read-excel-multiple-sheets-in-pandas/