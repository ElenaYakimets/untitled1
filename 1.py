import openpyxl
wb = openpyxl.reader.excel.load_workbook(filename="12.xlsx")
print(wb.sheetnames)
