import pandas as pd

df = pd.read_excel('C:\\Users\\gopve\\PycharmProjects\\pythonProject\\data\\excel_data.xlsx',
                   sheet_name='Sheet1')

# C:\pythonprojs\data\data_sheet.xlsx

# print whole sheet data
print(df)
print("===========")
for index, row in df.iterrows():
    print(row["TestName"], row["Execute"], row['Description'])
    # row['Result'] = "Pass"
    df.at[index, 'Result'] = "Pass"
    # print(df.at[index, 'Result'])

    # https: // www.scaler.com / topics / pandas / pandas - read - excel /
    # https://pythonbasics.org/read-excel/
    # https://www.shanelynn.ie/pandas-iloc-loc-select-rows-and-columns-dataframe/

    # data = pandas.read_excel("datasets.xlsx")
    # speciesdata = data["Species"].unique()
    # for i in speciesdata:
    #     a = data[data["Species"].str.contains(i)]
    #     a.to_excel(i + ".xlsx")

# https://www.golinuxcloud.com/filter-pandas-dataframe-by-column-value/

df = df.loc[df['Execute'] == 'Y']
print(df)

print("=========")
for row in df.itertuples():
    print(df['Execute'])
    print("end-------")
    # https://www.statology.org/pandas-select-rows-by-index/
    # https://www.statology.org/pandas-select-rows-based-on-column-values/

# # Change the first name of all rows with an ID greater than 2000 to "John"
# data.loc[data['id'] > 2000, "first_name"] = "John"
#
# # Change the first name of all rows with an ID greater than 2000 to "John"
# data.loc[data['id'] > 2000, "first_name"] = "John"
