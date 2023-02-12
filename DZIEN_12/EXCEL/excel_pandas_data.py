import pandas as pd
import xlsxwriter

df = pd.DataFrame({'Dane':[10,20,35,45,50,70,95,110,150,200,260,300,360]})

writer = pd.ExcelWriter('pandas_data.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name='ramka')
writer.save()
