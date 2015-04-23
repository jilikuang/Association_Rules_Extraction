import sys
from Computation import *


# entry of the program
def main(argv):
    if argv[0] == 'test':
        csv_filename = 'sample/DOHMH_New_York_City_Restaurant_Inspection_Results_reduced_final2.csv'
        min_supp = 0.25
        min_conf = 0.65
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
    output(frequent_items, association_list, min_supp, min_conf)


def display(itemsets, rules, min_supp, min_conf):
    '''
    Display results
    '''
    print '==Frequent itemsets (min_sup=' + str(min_supp*100.0) + '%)'
    # print itemsets
    for s in itemsets:
        print '[' + ', '.join(s[0]) + '], ' + '{:.4%}'.format(s[1])
    print
    print '==High-confidence association rules (min_conf=' + str(min_conf*100.0) + '%)'
    # print rules
    for r in rules:
        print '[' + ', '.join(r[0]) + '] => [' + ', '.join(r[1]) + '], (Conf: ' + '{:.4%}'.format(r[2]) + ', Supp: ' + '{:.4%}'.format(r[3]) + ')'


def output(itemsets, rules, min_supp, min_conf):
    out = open('example-run.txt', 'w')
    out.write('==Frequent itemsets (min_sup=' + str(min_supp*100.0) + '%)\n')
    # print itemsets
    for s in itemsets:
        out.write('[' + ', '.join(s[0]) + '], ' + '{:.4%}'.format(s[1]) + '\n')
    out.write('\n')
    out.write('==High-confidence association rules (min_conf=' + str(min_conf*100.0) + '%)\n')
    # print rules
    for r in rules:
        out.write('[' + ', '.join(r[0]) + '] => [' + ', '.join(r[1]) + '], (Conf: ' + '{:.4%}'.format(r[2]) + ', Supp: ' + '{:.4%}'.format(r[3]) + ')\n')
    out.close()


if __name__ == "__main__":
    main(sys.argv[1:])
