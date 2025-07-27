

import openpyxl
wb=openpyxl.Workbook()
sheet=wb.active

c1=sheet3cell(row=1,column=1)
c1.value="Hello"

c2=sheet.cell(row=1,column=2)
c1.value="Hi"

c3=sheet['A2']
c3.value="Good day"

c4=sheet['B2']
c4.value="Happy"

wb.save("sample.xlsx")
