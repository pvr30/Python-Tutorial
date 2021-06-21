# csv = commas separated value
import csv

with open("file.csv", 'r') as csv_file:

    reader = csv.reader(csv_file)

    for line in reader:
        print(line)

"""        
 output be like this.
['name', 'branch', 'number']
['Vishal', 'ECE', '9081139612']
['Harsh', 'BioMedical', '8866498339']
['Sahil', 'ECE', '9726341324']

"""