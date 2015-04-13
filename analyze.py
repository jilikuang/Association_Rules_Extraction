import sys

def analyze(string):
    '''
    Analyze the string and return the estimate type and value
    '''
    # Percentage
    if string.endswith('%'):
        num_str = string.rstrip('%').replace(',','')
        return float(num_str) / 100
    # Number
    if string.replace(',', '').replace('.', '', 1).isdigit():
        num_str = string.replace(',', '')
        if num_str.rfind('.') < 0:
            return int(num_str)
        else:
            return float(num_str)
    # Default
    return string

# For test
if __name__ == '__main__':
    result = analyze(sys.argv[1])
    print str(type(result)) + str(result)
