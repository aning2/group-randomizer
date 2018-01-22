import openpyxl

wb = openpyxl.load_workbook('class_list.xlsx')

ws = wb.active
first_column = ws['B']
class_list = []

for i in range(len(first_column)):
    class_list.append(first_column[i].value)
    #print(first_column[i].value)
    random.shuffle(class_list)

def students_per_group(n): #n is the number of students per group desired
    return [class_list[x:x+n] for x in range(0, len(class_list), n)]

def number_of_groups(n): #n is the number of groups desired
    d = (len(class_list)//n)
    return students_per_group(d)