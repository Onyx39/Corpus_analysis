from src.print_structure import main
from src.print_month_data import main2
from src.occurance_counting import create_list_occurancies, graph
from src.word_searching import print_all, create_day_legend
from src.word_collecting import word_collecting
import random as rd
import time as t

start = t.time()

#main()
#main2()
#create_list_occurancies()
#graph(create_list_occurancies())
#test_create_list_occurancies()
#explore_data()
#print_all('france')
#print_all("mali")
#create_day_legend()
l = word_collecting()
word = l[rd.randint(0, len(l))]
print_all(word)

end = t.time()
print("\nThe time of execution of above program is :", round(100*(end-start))/100, "s\n")
