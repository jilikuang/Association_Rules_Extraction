import sys
import csv
from Computation import *

def main(argv):
    if argv[0] == 'test':
        csv_filename = 'Graduation_Outcomes_-_Citywide_-_Classes_of_2005-2011_-_Ethnicity.csv'
        min_supp = 0.4
        min_conf = 1.0
    else:
        csv_filename = argv[0]
        min_supp = float(argv[1])
        min_conf = float(argv[2])

    """
    fields = None
    data = []

    with open(csv_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        fields = reader.fieldnames
        for row in reader:
            data.append(row)
        csvfile.close()
    """

    read_file(csv_filename)
    categorize()
    compute_word_set()
    association_list = apriori(min_supp, min_conf)
    display(association_list)


# print association according to the requirement
# each association is a list of set with length 2
def display(association_list):
    print association_list


if __name__ == "__main__":
    main(sys.argv[1:])
