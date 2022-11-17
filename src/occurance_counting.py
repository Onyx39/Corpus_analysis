from src.print_structure import load_data
import plotly.express as px
from math import inf
import pandas as pd
import json
import os


def create_list_occurancies () :

    data = load_data()

    
    #files_name = [file_name for file_name in os.listdir('./data') if '.json' in file_name]
    #for i in range(len(files_name)) :
    #    files_name[i] = 'data/' + files_name[i]
    #print(files_name)


    l = [['begin', inf], ['end', 0]]
    data_all = data['metadata-all']['fr']['all']['kws']
    n = len(data_all)
    for i in data_all :
        l = insert(l, i, data['metadata-all']['fr']['all']['kws'][i])
        print(len(l), '    ->   ', round(10000*(len(l)-2)/n)/100, '%\n')
    l = l[1:len(l)-1]
    print('\n', n == len(l), '\n')
    print_firsts(l)
    return l

def insert (l, name, value) :
    #print(l, type(l))
    for i in range(len(l)):
        #print(l[i][1])
        if value >= l[i][1] :
            #print('Entrer !')
            l.insert(i, [name, value])
            return l
    l.append([name, value])
    return l


def print_firsts (l) :
    for i in range (50) :
        print(l[i])


def graph (l) :
    l1, l2 = [], []
    compteur = 0
    for i in l :
        if i[1] <= 50 :
            break
        else :
            l1.append(i[0])
            l2.append(i[1])
            compteur += i[1] #compteur total = 37129
    bar_chart_data = [l1, l2]

    df = pd.DataFrame(bar_chart_data).transpose()
    df.columns = ['word', 'number']


    fig = px.bar(df, x='word', y="number", title="Occurences of words")
    fig.show()

    print(compteur)
    print('Mali : ', 100*421/compteur, '%')