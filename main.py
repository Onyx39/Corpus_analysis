from src.print_structure import main_print_structure
from src.print_month_data import main_month_data
from src.occurance_counting import create_list_occurrences, graph
from src.searching_words import print_all_1
from src.collecting_words import collecting_words
from src.exploring_data import explore_data
from src.plots_with_menus import print_all_2, evolution_occurrences_most_common_words_annualy, evolution_occurrences_most_common_words_monthly, evolution_occurrences_most_common_words_daily

import random as rd
import time as t

start = t.time()

# Feature 1 
main_print_structure()

# Feature 2
explore_data()

# Feature 3
main_month_data()  #print the evolution of the nomber of articles per month

# Feature 4
graph(create_list_occurrences()) #print the total occurences of all the words for the 3 years

print_all_1('france') #test with 'france'
l = collecting_words() #a list that contains all the words from the articles
word = l[rd.randint(0, len(l))] #get a word at random from the articles.
print_all_1(word)

# Feature 5
evolution_occurrences_most_common_words_annualy(percentage=1)
evolution_occurrences_most_common_words_monthly(percentage=0.2)
evolution_occurrences_most_common_words_daily(number=2)
print_all_2(threshold = 100)

end = t.time()
print("\nThe time of execution of above program is :", round(100*(end-start))/100, "s\n")
