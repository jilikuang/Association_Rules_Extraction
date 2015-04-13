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
    with open(incsv, 'r') as csvin:
        with open('output.csv', 'w') as csvout:
            reader = csv.reader(csvin)
            writer = csv.writer(csvout)
            first = next(reader)
            col_num = len(first)
            writer.writerow(first)
            for row in reader:
                if len(filter(str.strip, row)) == col_num:
                    writer.writerow(row)

if __name__ == '__main__':
    if sys.argv[1] == 'new' or sys.argv[1] == 'append':
        process(sys.argv[1], sys.argv[2], sys.argv[3])
    elif sys.argv[1] == 'reduce':
        csvreduce(sys.argv[2])
