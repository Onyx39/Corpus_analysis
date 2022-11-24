from src.print_structure import load_data
import plotly.express as px
import pandas as pd

def print_all (word) :
    evolution_occurrences_annualy(word)
    evolution_occurrences_monthly(word)
    evolution_occurrences_daily(word)
    return True

def evolution_occurrences_annualy (word) :
    #mettre input
    #word = 'algérie'
    data = load_data()

    l = [0]*3
    years = ['2019', '2020', '2021']
    index = 0
    for i in years :
        if word in data['metadata-all']['fr']['year'][i]['kws'] :
            l[index] = data['metadata-all']['fr']['year'][i]['kws'][word]
        index += 1
    #print(len(l), l)
    year_graph(l, word)
    return True

def year_graph (l, word) :
    year_legend = ["2019", "2020", "2021"]

    bar_chart_data = [year_legend, l]

    month_data_df = pd.DataFrame(bar_chart_data).transpose()
    month_data_df.columns=['year', 'value']

    fig = px.bar(month_data_df, x='year', y="value", title="Occuriency of '" + word + "'")
    fig.show()

def evolution_occurrences_monthly (word) :
    #mettre input
    #word = 'algérie'
    data = load_data()

    l = [0]*(3*12)
    years = ['2019', '2020', '2021']
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    index = 0
    for i in years :
        for j in months :
            if word in data['metadata-all']['fr']['month'][i][j]['kws'] :
                l[index] = data['metadata-all']['fr']['month'][i][j]['kws'][word]
            index += 1
    #print(len(l), l)
    month_graph(l, word)
    return True

def month_graph (l, word) :
    month_legend = ["01/19", "02/19", "03/19", "04/19", "05/19", "06/19", "07/19", "08/19", "09/19", "10/19", "11/19", "12/19", 
                    "01/20", "02/20", "03/20", "04/20", "05/20", "06/20", "07/20", "08/20", "09/20", "10/20", "11/20", "12/20",
                    "01/21", "02/21", "03/21", "04/21", "05/21", "06/21", "07/21", "08/21", "09/21", "10/21", "11/21", "12/21"]

    bar_chart_data = [month_legend, l]

    month_data_df = pd.DataFrame(bar_chart_data).transpose()
    month_data_df.columns=['month', 'value']

    fig = px.bar(month_data_df, x='month', y="value", title="Occuriency of '" + word + "'")
    fig.show()

def evolution_occurrences_daily (word) :
    #mettre input
    #word = 'algérie'
    data = load_data()

    l = [0]*1096
    years = ['2019', '2020', '2021']
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    for i in years :
        for j in months :
            for k in days :
                if k in data['metadata-all']['fr']['day'][i][j] :
                    if word in data['metadata-all']['fr']['day'][i][j][k]['kws'] :
                        l[get_day_index(i, j, k)] = data['metadata-all']['fr']['day'][i][j][k]['kws'][word]

    #print(len(l))
    day_graph(l, word)
    return True

def day_graph(l, word) :

    bar_chart_data = [create_day_legend(), l]

    df = pd.DataFrame(bar_chart_data).transpose()
    df.columns=['day', 'value']

    fig = px.line(df, x='day', y="value", title="Occuriency of '" + word + "'")
    fig.show()


def create_day_legend () :
    list = []
    month_length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_length_warning = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range (len(month_length)) :
        for j in range (1, month_length[i] + 1) :
            list.append(str(j) + '/' + str(i + 1) + '/19')
    for i in range (len(month_length_warning)) :
        for j in range (1, month_length_warning[i] + 1) :
            list.append(str(j) + '/' + str(i + 1) + '/20')
    for i in range (len(month_length)) :
        for j in range (1, month_length[i] + 1) :
            list.append(str(j) + '/' + str(i + 1) + '/21')
        
    return list

def get_day_index (year, month, day) :
    index = 0
    if year == '2020' :
        index += 365
    elif year == '2021' :
        index += 731

    if month == '2' :
        index += 31
    elif month == '3' :
        index += 59
    elif month == '4' :
        index += 90
    elif month == '5' :
        index == 120
    elif month == '6' :
        index += 151
    elif month == '7' :
        index += 181
    elif month == '8' :
        index += 212
    elif month == '9' :
        index += 243
    elif month == '10' :
        index += 273
    elif month == '11' :
        index += 304
    elif month == '12' :
        index += 334

    index += int(day)
    if index > 424 :
        index += 1
    return index
