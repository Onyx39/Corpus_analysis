from src.print_structure import main_print_structure
from src.print_month_data import main_month_data
from src.occurance_counting import create_list_occurancies, graph
from src.word_searching import print_all, create_day_legend
from src.word_collecting import word_collecting
from src.exploring_data import explore_data
import random as rd
import time as t

start = t.time()

#main_print_structure()
main_month_data()
graph(create_list_occurancies())
#explore_data()
#print_all('france')
#print_all("mali")
l = word_collecting()
word = l[rd.randint(0, len(l))]
print_all(word)

end = t.time()
print("\nThe time of execution of above program is :", round(100*(end-start))/100, "s\n")
