import unittest
from selenium import webdriver
import pandas as pd

file_name = 'C:\\pythonprojs\\data\\data_sheet.xlsx'

df = pd.read_excel(file_name, sheet_name=None)

print(df.keys())

print(df.get('Google'))



# https://thats-it-code.com/pandas/pandas__read-multiple-sheets-in-an-excel/
# https://sparkbyexamples.com/python/iterate-over-rows-in-pandas-dataframe/?expand_article=1
# https://sparkbyexamples.com/pandas/pandas-read-excel-multiple-sheets-in-pandas/#:~:text=sheet_name%20param%20on%20pandas.,and%20DF%20for%20Dict%20value.
