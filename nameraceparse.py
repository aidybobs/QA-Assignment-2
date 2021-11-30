import csv

with open('names.csv', 'r') as names:
    csv_reader = csv.reader(names)
    races = next(csv_reader)