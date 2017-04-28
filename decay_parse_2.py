import csv

with open('sample.dat', 'r') as fin:
    data = [line.split() for line in fin]
    print(data)
