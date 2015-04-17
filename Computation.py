import re
import csv
import math
from analyze import *

data_rows = []
cat_data_rows_list = []
words_set = set()
category_num = 5.0
fields = []


# read the excel file into rows
def read_file(file_name):
    with open(file_name, 'rbU') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        global fields
        fields = next(reader)
        for row in reader:
            data_rows.append(row)


def data_is_number(data, col_idx):
    if type(analyze(data)) is str:
        return False
    if re.search("[Yy][Ee][Aa][Rr]", fields[col_idx]):
        return False
    if re.search("ZIPCODE", fields[col_idx]):
        return False
    return True


# Since a lot cell contains float number, we need to categorize them and make the numbers more meaningful
def categorize():
    if len(data_rows) > 0:
        mins = []
        maxs = []
        index = 0
        for col in data_rows[0]:
            if col != ' n/a ' and data_is_number(col, index):
                mins.append(analyze(col))
                maxs.append(analyze(col))
            else:
                mins.append(0)
                maxs.append(0)
            index += 1
        for row in data_rows:
            index = 0
            for col in row:
                if col != ' n/a ' and data_is_number(col, index):
                    if analyze(col) < mins[index]:
                        mins[index] = analyze(col)
                    if analyze(col) > maxs[index]:
                        maxs[index] = analyze(col)
                index += 1
        for row in data_rows:
            index = 0
            cat_data_row = []
            for word in row:
                if word == ' n/a ':
                    cat_data_row.append(word)
                else:
                    if data_is_number(word, index):
                        col_min = mins[index]
                        col_max = maxs[index]
                        level = math.floor((analyze(word)-col_min)/((col_max - col_min)/category_num))
                        range = str((col_max - col_min)/category_num*level) + "-" + str((col_max - col_min)/category_num*(level+1))
                        cat_data_row.append(fields[index] + '_' + range)
                    else:
                        cat_data_row.append(word)
                index += 1
            cat_data_row_set = set(cat_data_row)
            cat_data_rows_list.append(cat_data_row_set)


# compute the word collection
def compute_word_set():
    for row in cat_data_rows_list:
        for word in row:
            if word not in words_set:
                words_set.add(word)


# compute the number of times when the subset appears in the rows
def compute_frequency(subset):
    count = 0
    for row in cat_data_rows_list:
        if subset.issubset(row):
            count += 1
    return count


# start the apriori algorithm
def apriori(min_supp, min_conf):
    high_freq_set_list = compute_high_freq_set_list(min_supp)
    high_conf_set_list = compute_high_conf_ass_list(high_freq_set_list, min_conf)
    return high_conf_set_list


# compute the frequent item_set list has larger support than min_support
# each element in the list is a list of length 2, list[0] is the set itself, list[1] is the support
def compute_high_freq_set_list(min_supp):
    min_row_num = len(data_rows)*min_supp
    high_freq_set_list = []
    item_set = []
    high_freq_set_list_k = []
    for word in words_set:
        num = compute_frequency(set([word]))
        if num >= min_row_num:
            item_set.append(word)
            high_freq_set_list_k.append([set([word]), float(num)/len(data_rows)])
    while len(high_freq_set_list_k) > 0:
        high_freq_set_list.extend(high_freq_set_list_k)
        high_freq_set_list_k_plus_1 = []
        high_freq_set_set_k_plus_1 = ([])
        for set_list in high_freq_set_list_k:
            for item in item_set:
                if item not in set_list[0]:
                    new_s = set(set_list[0])
                    new_s.add(item)
                    count = compute_frequency(new_s)
                    if count >= min_row_num and new_s not in high_freq_set_set_k_plus_1:
                        high_freq_set_list_k_plus_1.append([new_s, float(count)/len(data_rows)])
                        high_freq_set_set_k_plus_1.append(new_s)
        high_freq_set_list_k = high_freq_set_list_k_plus_1
    return high_freq_set_list


# compute the association rules that has higher confidence than min_confidence
def compute_high_conf_ass_list(high_freq_set_list, min_conf):
    high_conf_ass_list = []
    for item_set in high_freq_set_list:
        association_list = compute_association_list(item_set)
        for association in association_list:
            conf = compute_conf(association)
            if conf >= min_conf:
                association[2] = conf
                association[3] = item_set[1]
                high_conf_ass_list.append(association)
    return high_conf_ass_list


# each association is a list of set of length 4, list[0] stands for the left set and list[1] is the right
# list[2] is the confidence and list[3] is the support
def compute_association_list(item_set):
    association_list = []
    compute_association_list_helper(association_list, set(), item_set[0])
    return association_list


# compute all the possible association rules of an item_set
def compute_association_list_helper(ass_list, left_set, right_set):
    if len(left_set) > 0 and len(right_set) > 0:
        ass_list.append([left_set, right_set, 0.0, 0.0])
    if len(right_set) > 0:
        for item in right_set:
            new_right_set = set(right_set)
            new_right_set.remove(item)
            new_left_set = set(left_set)
            new_left_set.add(item)
            compute_association_list_helper(ass_list, new_left_set, new_right_set)


# compute the confidence of an association rule
def compute_conf(association):
    left_count = 0
    right_count = 0
    for row in cat_data_rows_list:
        if association[0].issubset(row):
            left_count += 1
            if association[1].issubset(row):
                right_count += 1
    return float(right_count)/float(left_count)
