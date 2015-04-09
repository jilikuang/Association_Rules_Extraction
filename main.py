import sys
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

    read_file(csv_filename)
    categorize()
    compute_word_set()
    frequent_items = compute_high_freq_set_list(min_supp)
    association_list = compute_high_conf_ass_list(frequent_items, min_conf)
    display(frequent_items, association_list)


# print association according to the requirement
# each association is a list of set with length 2
def display(frequent_items, association_list):
    print "==Frequent itemsets"
    print frequent_items
    print ""
    print "==High-confidence association rules"
    print association_list


if __name__ == "__main__":
    main(sys.argv[1:])
