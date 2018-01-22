import openpyxl

wb = openpyxl.load_workbook('class_list.xlsx')

ws = wb.active
first_column = ws['B']