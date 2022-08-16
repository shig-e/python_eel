import pandas as pd 
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

wb = Workbook()
ws = wb.active
df = pd.read_csv("/Users/mayu/Desktop/python/Python-eel/csv", encoding="utf-8")

for row in dataframe_to_rows(df, index=None, header=True):
    ws.append(row)
    
wb.save("楽天.xlsx")