import pandas as pd
import xlsxwriter
import openpyxl


df = pd.DataFrame({
    'Miesiąc':[1,2,3,4,5,6,7,8,9,10,11,12],
    'Wartość sprzedaży':[2340,2189,8970,5460,3425,7890,1234,2567,6789,5432,9854,6782],
    'Procent':[.04,.08,.11,.16,.28,.18,.24,.31,.09,.1,.4,.14]
})

writer = pd.ExcelWriter('procenty.xlsx', engine='xlsxwriter')
df.to_excel(writer,sheet_name='proc')

workbook = writer.book
worksheet = writer.sheets['proc']

format1 = workbook.add_format({'num_format':'#.##00'})
format2 = workbook.add_format({'num_format':'0.0%'})

worksheet.set_column(2,2,20,format1)
worksheet.set_column(3,3,None,format2)

writer.save()

df2 = pd.read_excel('procenty.xlsx',sheet_name='proc')
# pd.read_excel(r'C:\BOOTCAMP_PYTHON_II_22_23\excel_pandas_procent\procenty.xlsx')

print(df2)
