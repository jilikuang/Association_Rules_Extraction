import sys
from Computation import *


# entry of the program
def main(argv):
    if argv[0] == 'test':
        csv_filename = 'Graduation_Outcomes_-_Citywide_-_Classes_of_2005-2011_-_Ethnicity.csv'
        min_supp = 0.45
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

    display(frequent_items, association_list, min_supp, min_conf)


def display(itemsets, rules, min_supp, min_conf):
    '''
    Display results
    '''
    print '==Frequent itemsets (min_sup=' + str(min_supp*100.0) + '%)'
    # print itemsets
    for s in itemsets:
        print '[' + ', '.join(s[0]) + '], ' + '{:.2f}'.format(s[1]*100.0) + '%'
    print
    print '==High-confidence association rules (min_conf=' + str(min_conf*100.0) + '%)'
    # print rules
    for r in rules:
        print '[' + ', '.join(r[0]) + '] => [' + ', '.join(r[1]) + '], (Conf: ' + '{:.2f}'.format(r[2]*100.0) + '%, Supp: ' + '{:.2f}'.format(r[3]*100.0) + '%)'


if __name__ == "__main__":
    main(sys.argv[1:])
