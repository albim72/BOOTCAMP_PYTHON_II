import numpy as np
import xlsxwriter

workbook = xlsxwriter.Workbook("wykres.xlsx")
worksheet = workbook.add_worksheet("zestawienie")

wykres = workbook.add_chart({'type':'column'})

dane = np.array([
    [6,4,11,5,35,9],
    [9,12,8,16,34,10],
    [18,20,10,3,40,20],
    [2,5,1,15,70,14],
])

bold = workbook.add_format({'bold':True})
worksheet.write_column("A1",dane[0])
worksheet.write_column("B1",dane[1])
worksheet.write_column("C1",dane[2])
worksheet.write_column("D1",dane[3])

worksheet.write("A7",sum(dane[0]),bold)
worksheet.write("B7",sum(dane[1]),bold)
worksheet.write("C7",sum(dane[2]),bold)
worksheet.write("D7",sum(dane[3]),bold)

wykres.add_series({'values':'=zestawienie!$A$1:$A$6'})
wykres.add_series({'values':'=zestawienie!$B$1:$B$6'})
wykres.add_series({'values':'=zestawienie!$C$1:$C$6'})
wykres.add_series({'values':'=zestawienie!$D$1:$D$6'})

worksheet.insert_chart('B9',wykres)
workbook.close()
