import sys
import csv

def process(mode, incsv, first_col):
    with open(incsv, 'r') as csvin:
        if mode == 'append':
            with open('output.csv', 'a') as csvout:
                reader = csv.reader(csvin)
                writer = csv.writer(csvout)
                first = next(reader)
                print 'Number of column: ' + str(len(first))
                for row in reader:
                    writer.writerow([first_col] + row)
        else:
            with open('output.csv', 'w') as csvout:
                reader = csv.reader(csvin)
                writer = csv.writer(csvout)
                first = next(reader)
                print 'Number of column: ' + str(len(first))
                writer.writerow(['Borough'] + first)
                for row in reader:
                    writer.writerow([first_col] + row)

def csvreduce(incsv):
    with open(incsv, 'rU') as csvin:
        with open('output.csv', 'w') as csvout:
            reader = csv.reader(csvin)
            writer = csv.writer(csvout)
            first = next(reader)
            idx_score = first.index('SCORE')
            idx_grade = first.index('GRADE')
            idx_date = first.index('INSPECTION DATE')
            col_num = len(first)
            writer.writerow(first)
            for row in reader:
                #if len(filter(str.strip, row)) == col_num:
                #if row[idx_score] != '' and row[idx_grade] != '':
                if int(row[idx_score]) <= 30:
                    i = row[idx_date].find('/')
                    #print row[idx_date][0:i]
                    if int(row[idx_date][0:i]) > 9:
                        row[idx_date] = 'Q4'
                    elif int(row[idx_date][0:i]) > 6:
                        row[idx_date] = 'Q3'
                    elif int(row[idx_date][0:i]) > 3:
                        row[idx_date] = 'Q2'
                    else:
                        row[idx_date] = 'Q1'
                    writer.writerow(row)

if __name__ == '__main__':
    if sys.argv[1] == 'new' or sys.argv[1] == 'append':
        process(sys.argv[1], sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'reduce':
        csvreduce(sys.argv[2])
