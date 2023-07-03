import pandas as pd

df = pd.read_excel('C:\\pythonprojs\\data\\data_sheet.xlsx',
                   sheet_name='Scenarios_copy')

print(df)
print("=============")
df = df[df["Execute"].str.contains("Y|Yes")]

print(df)
print("=======555555555555555======")
for index, row in df.iterrows():
    try:
        print(row["Scenario Name"], row["Execute"], row['SheetName'])
        sheetNM = str(row['SheetName']).strip()
        print("sheet name ", sheetNM)
        print(type(row['SheetName']))

        df1 = pd.read_excel('C:\\pythonprojs\\data\\data_sheet.xlsx', sheet_name=sheetNM)
        print(df1)
        print("=========", sheetNM)
    except Exception as err:
        print("error: ", err)

list1 = df["SheetName"]  # series
print("list", type(list1[0]))

df.to_excel("C:\\pythonprojs\\data\\data_sheet1.xlsx", index=False, header=True)

# write to excel file.. examples
# https://sparkbyexamples.com/pandas/pandas-write-to-excel-with-examples/