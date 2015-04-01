import Computation


test_file_name = 'Graduation_Outcomes_-_Citywide_-_Classes_of_2005-2011_-_Ethnicity.csv'
min_supp = 0.5
min_conf = 0.5

Computation.read_file(test_file_name)
Computation.categorize()
Computation.compute_word_collection()
Computation.compute_frequency()
Computation.apriori(min_supp, min_conf)