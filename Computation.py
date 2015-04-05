import csv
import math

data_rows = []
cat_data_rows_list = []
words_set = set([])
col_with_num = 3
category_num = 5.0


def read_file(file_name):
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data_rows.append(row)


def categorize():
    if len(data_rows) > 0:
        mins = []
        maxs = []
        index = 0
        for col in data_rows[1]:
            if index > col_with_num and col != ' n/a ':
                col = col.replace(',', '')
                col = col.replace('%', '')
                mins.append(float(col))
                maxs.append(float(col))
            else:
                mins.append(0)
                maxs.append(0)
            index += 1
        for row in data_rows[1:]:
            index = 0
            for col in row:
                if index > col_with_num:
                    if col != ' n/a ':
                        col = col.replace(',', '')
                        col = col.replace('%', '')
                        if float(col) < mins[index]:
                            mins[index] = float(col)
                        if float(col) > maxs[index]:
                            maxs[index] = float(col)
                index += 1
        for row in data_rows[1:]:
            index = 0
            cat_data_row = []
            for word in row:
                if index > col_with_num:
                    col_min = mins[index]
                    col_max = maxs[index]
                    if word == ' n/a ':
                        level = 'None'
                    else:
                        word = word.replace(',', '')
                        word = word.replace('%', '')
                        level = math.floor((float(word)-col_min)/((col_max - col_min)/category_num))
                    cat_data_row.append(data_rows[0][index] + '_' + str(level))
                else:
                    cat_data_row.append(word)
                index += 1
            cat_data_rows_list.append(cat_data_row)


def compute_word_collection():
    for row in cat_data_rows_list[1:]:
        for word in row:
            if word not in words_set:
                words_set.add(word)


def compute_frequency(subset):
    count = 0
    for row in cat_data_rows_list[1:]:
        if subset.issubset(row):
            count += 1
    return count


def apriori(min_supp, min_conf):
    high_freq_list = compute_high_freq_list(min_supp)
    high_conf_list = compute_high_conf_list(high_freq_list, min_conf)
    return high_conf_list


def compute_high_freq_list(min_supp):
    min_row_num = (len(data_rows)-1)*min_supp
    high_freq_list = []
    item_set = set([])
    for word in words_set:
        num = compute_frequency(set(word))
        if num >= min_row_num:
            item_set.add(word)
    high_freq_list.append(item_set)
    high_set_k = item_set
    while len(high_set_k) > 0:
        high_set_k_plus_1 = {}
        for s in high_set_k:
            for item in item_set and item not in s:
                new_s = set(s)
                new_s.add(item)
                count = compute_frequency(new_s)
                if count >= min_row_num:
                    high_set_k_plus_1.add(new_s)
        high_freq_list.append(high_set_k_plus_1)
        high_set_k = high_set_k_plus_1
    print high_freq_list
    return high_freq_list


def compute_high_conf_list(high_freq_list, min_conf):
    high_conf_list = []
    return high_conf_list