import openpyxl

wb = openpyxl.load_workbook('class_list.xlsx')

ws = wb.active
first_column = ws['B']
class_list = []

for i in range(len(first_column)):
    class_list.append(first_column[i].value)
    #print(first_column[i].value)
    random.shuffle(class_list)

def students_per_group(n):

def number_of_groups(n): 