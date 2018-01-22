import openpyxl
import random
from flask import Flask, request, render_template

app = Flask(__name__)
wb = openpyxl.load_workbook('class_list.xlsx')


ws = wb.active
first_column = ws['B']
class_list = []

for i in range(len(first_column)):
    class_list.append(first_column[i].value)
    #print(first_column[i].value)
    random.shuffle(class_list)

def students_per_group(my_list, n): #n is the number of students per group desired
    return [my_list[x:x+n] for x in range(0, len(my_list), n)]

def number_of_groups(my_list, n): #n is the number of groups desired,
    d = (len(my_list)+n-1) // n
    return students_per_group(my_list, d)
