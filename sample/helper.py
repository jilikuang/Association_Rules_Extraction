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


def get_restaurant_type(restaurant):
    types = {}
    type['Asian'] = [
        'Afghan', 'Asian', 'Bangladeshi', 'Chinese', 'Chinese/Cuban', 'Chinese/Japanese',
        'Filipino', 'Indian', 'Indonesian', 'Iranian', 'Japanese', 'Jewish/Kosher', 'Korean',
        'Middle Eastern', 'Pakistani', 'Thai', 'Turkish', 'Vietnamese/Cambodian/Malasian'
    ]
    type['European'] = [
        'Australian', 'Bagels/Pretzeis', 'Czech', 'Eastern European', 'English', 'French',
        'German', 'Greek', 'Irish', 'Italian', 'Mediterranean', 'Pizza', 'Pizza/Italian', 'Polish',
        'Portuguese', 'Russian', 'Scandinavian', 'Spanish', 'Tapas'
    ]
    type['NorthAmerican'] = [
        'American', 'Barbecue', 'Cajun', 'Californian', 'Caribbean', 'Chicken', 'Creole', 'Creole/Cajun',
        'Hamburgers', 'Hawaiian', 'Hotdogs', 'Hotdogs/Pretzels', 'Mexican', 'Polynesian', 'Sandwiches',
        'Sandwiches/Salads/Mixed Buffet', 'Southwestern', 'Steak', 'Tex-Mex'

    ]
    type['SouthAmerican'] = [
        'Brazillian', 'Chilean', 'Latin', 'Peruvian'
    ]
    type['Africa'] = [
        'African', 'Armenian', 'Egyptian', 'Ethiopian', 'Moroccan'
    ]
    type['Other'] = [
        'Bakery', 'Bottled beverages', 'Cafe/Coffee/Tea', 'Continental', 'Delicatessen', 'Donuts',
        'Fruit/Vegetables', 'Ice cream', 'Juice', 'Nuts/Confectionary', 'Pancakes/Waffles', 'Salads',
        'Seafood', 'Soul Food', 'Soups', 'Soups/Sandwiches', 'Vegetarian'
    ]
