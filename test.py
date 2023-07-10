import csv
import ast

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    i=0
    for row in reader:
        print(ast.literal_eval(row['Board']))
        print(i)
        i=i+1