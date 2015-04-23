import sys
import csv

types = {}
restaurant_type = {}

# mapping from cuisine type to category
types['Asian'] = [
    'Afghan', 'Asian', 'Bangladeshi', 'Chinese', 'Chinese/Cuban', 'Chinese/Japanese',
    'Filipino', 'Indian', 'Indonesian', 'Iranian', 'Japanese', 'Jewish/Kosher', 'Korean',
    'Middle Eastern', 'Pakistani', 'Thai', 'Turkish', 'Vietnamese/Cambodian/Malaysia'
]
types['European'] = [
    'Australian', 'Bagels/Pretzeis', 'Czech', 'Eastern European', 'English', 'French',
    'German', 'Greek', 'Irish', 'Italian', 'Mediterranean', 'Pizza', 'Pizza/Italian', 'Polish',
    'Portuguese', 'Russian', 'Scandinavian', 'Spanish', 'Tapas', 'Bagels/Pretzels'
]
types['NorthAmerican'] = [
    'American', 'Barbecue', 'Cajun', 'Californian', 'Caribbean', 'Chicken', 'Creole', 'Creole/Cajun',
    'Hamburgers', 'Hawaiian', 'Hotdogs', 'Hotdogs/Pretzels', 'Mexican', 'Polynesian', 'Sandwiches',
    'Sandwiches/Salads/Mixed Buffet', 'Southwestern', 'Steak', 'Tex-Mex',
    'Latin (Cuban, Dominican, Puerto Rican, South & Central American)'
]
types['SouthAmerican'] = [
    'Brazilian', 'Chilean', 'Latin', 'Peruvian'
]
types['Africa'] = [
    'African', 'Armenian', 'Egyptian', 'Ethiopian', 'Moroccan'
]
types['Other'] = [
    'Bakery', 'Bottled beverages', 'Cafe/Coffee/Tea', 'Continental', 'Delicatessen', 'Donuts',
    'Fruit/Vegetables', 'Ice cream', 'Juice', 'Nuts/Confectionary', 'Pancakes/Waffles', 'Salads',
    'Seafood', 'Soul Food', 'Soups', 'Soups/Sandwiches', 'Vegetarian', 'Ice Cream, Gelato, Yogurt, Ices',
    'Caf_/Coffee/Tea', 'Caf/Coffee/Tea', 'Not Listed/Not Applicable', 'Other',
    'Bottled beverages, including water, sodas, juices, etc.', 'Juice, Smoothies, Fruit Salads',
    'Soups & Sandwiches', 'Fruits/Vegetables'
]


# convert exact date to quarter
def date_to_quarter(date):
    i = date.find('/')
    if 6 > int(date[0:i]) > 2:
        return 'Spring'
    elif 9 > int(date[0:i]) >= 6:
        return 'Summer'
    elif 12 > int(date[0:i]) >= 9:
        return 'Fall'
    else:
        return 'Winter'


# convert exact cuisine type to a category
def get_restaurant_type(cuisine):
    if not restaurant_type:
        for key in types.keys():
            for item in types[key]:
                restaurant_type[item] = key
    return restaurant_type[cuisine]
def process(incsv, mode, first_col):
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


#
def csvtrim(incsv, cols=None):
    with open(incsv, 'rU') as csvin:
        with open('output.csv', 'w') as csvout:
            reader = csv.reader(csvin)
            writer = csv.writer(csvout)
            fields = next(reader)
            col_num = len(fields)
            if cols is not None:
                to_drop = sorted(map(int, cols), reverse=True)
                for i in to_drop:
                    del fields[i]
            writer.writerow(fields)
            for row in reader:
                if len(filter(str.strip, row)) == col_num:
                    if cols is not None:
                        for i in to_drop:
                            del row[i]
                    row = map(str.strip, row)
                    row = map(lambda s: s.decode('utf-8', 'ignore').encode('ascii', 'ignore'), row)
                    writer.writerow(row)


#
def csvmodify(incsv):
    with open(incsv, 'rU') as csvin:
        with open('output.csv', 'w') as csvout:
            reader = csv.reader(csvin)
            writer = csv.writer(csvout)
            fields = next(reader)
            idx_date = fields.index('INSPECTION DATE')
            fields.insert(idx_date+1, 'INSPECTION SEASON')
            idx_cuisine = fields.index('CUISINE DESCRIPTION')
            fields.insert(idx_cuisine, 'CUISINE REGION')
            idx_score = fields.index('SCORE')
            writer.writerow(fields)
            for row in reader:
                row.insert(idx_date+1, date_to_quarter(row[idx_date]))
                row.insert(idx_cuisine+1, get_restaurant_type(row[idx_cuisine]))
                if int(row[idx_score]) > 30:
                    row[idx_score] = '30'
                writer.writerow(row)


if __name__ == '__main__':
    '''
    The usage of csvproc: <input CSV file> <operation> <arguments...>
    '''
    if sys.argv[2] == 'trim':
        if len(sys.argv) < 3:
            csvtrim(sys.argv[1])
        else:
            csvtrim(sys.argv[1], sys.argv[3:])
    elif sys.argv[2] == 'modify':
        csvmodify(sys.argv[1])
