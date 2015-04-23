types = {}
restaurant_type = {}

types['Asian'] = [
    'Afghan', 'Asian', 'Bangladeshi', 'Chinese', 'Chinese/Cuban', 'Chinese/Japanese',
    'Filipino', 'Indian', 'Indonesian', 'Iranian', 'Japanese', 'Jewish/Kosher', 'Korean',
    'Middle Eastern', 'Pakistani', 'Thai', 'Turkish', 'Vietnamese/Cambodian/Malasian'
]
types['European'] = [
    'Australian', 'Bagels/Pretzeis', 'Czech', 'Eastern European', 'English', 'French',
    'German', 'Greek', 'Irish', 'Italian', 'Mediterranean', 'Pizza', 'Pizza/Italian', 'Polish',
    'Portuguese', 'Russian', 'Scandinavian', 'Spanish', 'Tapas'
]
types['NorthAmerican'] = [
    'American', 'Barbecue', 'Cajun', 'Californian', 'Caribbean', 'Chicken', 'Creole', 'Creole/Cajun',
    'Hamburgers', 'Hawaiian', 'Hotdogs', 'Hotdogs/Pretzels', 'Mexican', 'Polynesian', 'Sandwiches',
    'Sandwiches/Salads/Mixed Buffet', 'Southwestern', 'Steak', 'Tex-Mex'

]
types['SouthAmerican'] = [
    'Brazillian', 'Chilean', 'Latin', 'Peruvian'
]
types['Africa'] = [
    'African', 'Armenian', 'Egyptian', 'Ethiopian', 'Moroccan'
]
types['Other'] = [
    'Bakery', 'Bottled beverages', 'Cafe/Coffee/Tea', 'Continental', 'Delicatessen', 'Donuts',
    'Fruit/Vegetables', 'Ice cream', 'Juice', 'Nuts/Confectionary', 'Pancakes/Waffles', 'Salads',
    'Seafood', 'Soul Food', 'Soups', 'Soups/Sandwiches', 'Vegetarian'
]


# convert exact date to quarter
def date_to_quarter(date):
    i = date.find('/')
    if int(date[0:i]) > 9:
        return 'Q4'
    elif int(date[0:i]) > 6:
        return 'Q3'
    elif int(date[0:i]) > 3:
        return 'Q2'
    else:
        return 'Q1'


# convert exact cuisine type to a category
def get_restaurant_type(cuisine):
    if not restaurant_type:
        for key in type.keys():
            for item in type[key]:
                restaurant_type[item] = key
    return restaurant_type[cuisine]