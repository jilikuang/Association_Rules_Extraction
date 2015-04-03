import sys
import csv
import Computation

def main(argv):
    if argv[0] == 'test':
        csv_filename = 'Graduation_Outcomes_-_Citywide_-_Classes_of_2005-2011_-_Ethnicity.csv'
        min_supp = 0.5
        min_conf = 0.5
    else:
        csv_filename = argv[0]
        min_supp = float(argv[1])
        min_conf = float(argv[2])

    fields = None
    data = []

    with open(csv_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        fields = reader.fieldnames
        for row in reader:
            data.append(row)
        csvfile.close()

    Computation.read_file(csv_filename)
    Computation.categorize()
    Computation.compute_word_collection()
    Computation.compute_frequency()
    Computation.apriori(min_supp, min_conf)

if __name__ == "__main__":
    main(sys.argv[1:])
