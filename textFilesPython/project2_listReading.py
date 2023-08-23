import csv

with open('devices2.txt', 'r') as file:
    reader = csv.reader(file, delimiter=':', lineterminator='\n')
    devices = list()
    for row in reader:
        devices.append(row)
    print(devices)