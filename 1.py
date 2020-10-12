import openpyxl
wb = openpyxl.reader.excel.load_workbook(filename="12.xlsx")
wb.active = 0
sheet = wb.active
#print (sheet['A1'].value)

for i in range (1,12):
    print(sheet['A'+str(i)].value, sheet['B'+str(i)].value, sheet['C'+str(i)].value)