import openpyxl

path="student.xlsx"

wb_obj=openpyxl.load_workbook(path)

sheet_obj=wb_obj.active

#cell obj is created by using sheet obj's cell() method
cell_obj=sheet_obj.cell(row=1, column=1)
print(cell_obj.value)

