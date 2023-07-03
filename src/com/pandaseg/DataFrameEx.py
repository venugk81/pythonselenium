import pandas as pd

df = pd.read_excel('C:\\pythonprojs\\data\\data_sheet.xlsx', sheet_name='Scenarios')

print(df)
print(df[df["Execute"].str.contains("Y")])
print("============")
print(df[df["Execute"].str.contains("Y|Yes")])

df1 = df[df["Execute"].str.contains("Y|Yes")]

print("======head method============")
print(df.head())

# https://www.statology.org/pandas-drop-rows-with-condition/
#     https: // www.statology.org / pandas - filter - rows - containing - string /
# https://www.statology.org/pandas-filter-multiple-conditions/
# https://www.statology.org/pandas-not-in/

# for row in df.itertuples():
#     print(row)
#     print(row[1])

print("=========iterate through each row and select===========")
# iterate through each row and select
# 'TestName' and 'Execute' column respectively.
# for row in df1.itertuples():
#     print(getattr(row, "TestName"), getattr(row, "Execute"))


print("=========iterrows===========")
for index, row in df1.iterrows():
    print(row["TestName"], row["Col1"], row['Status'])
    # row['Status'] = "Pass"
    df1.at[index, 'Status'] = "Pass"
    print(df1.at[index, 'Status'])
# https://re-thought.com/how-to-change-or-update-a-cell-value-in-python-pandas-dataframe/
print("done-------------------")
print(df1)



df1.to_excel("C:\pythonprojs\data\data_sheet1.xlsx", index=False, header=True)

# You can access cell value via .loc but you can't updated it this way!