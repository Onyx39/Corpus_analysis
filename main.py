#from src.print_structure import main_print_structure
from src.print_month_data import main_month_data
from src.occurance_counting import create_list_occurrences, graph
from src.searching_words import print_all
from src.collecting_words import collecting_words
#from src.exploring_data import explore_data
from src.plots_with_menus import evolution_occurrences_most_common_words_annualy, evolution_occurrences_most_common_words_monthly, evolution_occurrences_most_common_words_daily

import random as rd
import time as t

start = t.time()

#main_print_structure()
main_month_data()  #print the evolution of the nomber of articles per month
graph(create_list_occurrences()) #print the total occurences of all the words for the 3 years
#explore_data()
#print_all('france')
#print_all('mali')
l = collecting_words()
word = l[rd.randint(0, len(l))]
print_all(word)
evolution_occurrences_most_common_words_annualy(pourcentage=1)
evolution_occurrences_most_common_words_monthly(pourcentage=0.2)
evolution_occurrences_most_common_words_daily(nombre=2)

end = t.time()
print("\nThe time of execution of above program is :", round(100*(end-start))/100, "s\n")
