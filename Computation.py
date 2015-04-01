import csv
import math

data_rows = []
cat_data_rows = []
words = {}
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
                    cat_data_rows.append(word)
                index += 1
            cat_data_rows.append(cat_data_row)


def compute_word_collection():
    for row in cat_data_rows:
        for word in row:
            if word not in words:
                words[word] = []


def compute_frequency():
    count = len(data_rows)
    if count > 0:
        for word in words:
            items = []
            index = 0
            for row in cat_data_rows:
                if word in row:
                    items.append(index)
                index += 1
            words[word] = items


def apriori(min_supp, min_conf):
    return {}


