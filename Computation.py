import csv

test_file_name = 'Graduation_Outcomes_-_Citywide_-_Classes_of_2005-2011_-_Ethnicity.csv'


def read_file(file_name):
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print str(len(row))
            print row

read_file(test_file_name)