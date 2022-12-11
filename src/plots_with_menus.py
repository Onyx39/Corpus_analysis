from src.searching_words import create_day_legend, get_day_index
from src.occurance_counting import create_list_occurrences
from src.print_structure import load_data
import plotly.graph_objects as go
import pandas as pd

def print_all_2 (number=None, threshold=None, percentage=None) :
    evolution_occurrences_most_common_words_annualy (number, threshold, percentage)
    evolution_occurrences_most_common_words_monthly (number, threshold, percentage)
    evolution_occurrences_most_common_words_daily (number, threshold, percentage)
    return True

def evolution_occurrences_most_common_words_annualy (number=None, threshold=None, percentage=None) :
    l = create_list_occurrences()
    if number != None :
        l = l[:number]
    elif threshold != None :
        for i in range(len(l)) :
            if l[i][1] < threshold :
                l = l[:i]
                break
    elif percentage != None :
        stop = int(percentage/100*len(l))
        l = l[:stop]

    longueur = len(l)
    article_data = load_data()
    years = ["2019", "2020", "2021"]
    data = []
    buttons = list([dict(label="All",
                     method="update",
                     args=[{"visible": [True]*len(l)},
                           {"title": "Occurrences of the most common words"}])])

    True_index = -1
    for i in l :
        True_index += 1
        word = i[0]
        occurrences = [0]*3
        index = 0
        for i in years :
            if word in article_data['metadata-all']['fr']['year'][i]['kws'] :
                occurrences[index] = article_data['metadata-all']['fr']['year'][i]['kws'][word]
            index += 1

        bar_chart = [years, occurrences]

        df = pd.DataFrame(bar_chart).transpose()
        df.columns=['year', 'value']

        data.append(go.Bar(name=word, x=df['year'], y=df['value']))

        visible_list = [False]*longueur
        visible_list[True_index] = True
        buttons.append(dict(label=word,
                     method="update",
                     args=[{"visible": visible_list},
                           {"title": "Occurrences of '" + word + "'"}]))

    plot = go.Figure(data=data)
    plot.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=buttons)])

    plot.show()
    return True


def evolution_occurrences_most_common_words_monthly (number=None, threshold=None, percentage=None) :
    l = create_list_occurrences()
    if number != None :
        l = l[:number]
    elif threshold != None :
        for i in range(len(l)) :
            if l[i][1] < threshold :
                l = l[:i]
                break
    elif percentage != None :
        stop = int(percentage/100*len(l))
        l = l[:stop]


    longueur = len(l)
    article_data = load_data()
    data = []
    buttons = list([dict(label="All",
                     method="update",
                     args=[{"visible": [True]*len(l)},
                           {"title": "Occurrences of the most common words"}])])

    years = ['2019', '2020', '2021']
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    month_legend = ["01/19", "02/19", "03/19", "04/19", "05/19", "06/19", "07/19", "08/19", "09/19", "10/19", "11/19", "12/19", 
                    "01/20", "02/20", "03/20", "04/20", "05/20", "06/20", "07/20", "08/20", "09/20", "10/20", "11/20", "12/20",
                    "01/21", "02/21", "03/21", "04/21", "05/21", "06/21", "07/21", "08/21", "09/21", "10/21", "11/21", "12/21"]

    
    True_index = -1
    for z in l :
        True_index += 1
        word = z[0]
        occurrences = [0]*(3*12)
        index = 0
        for i in years :
            for j in months :
                if word in article_data['metadata-all']['fr']['month'][i][j]['kws'] :
                    occurrences[index] = article_data['metadata-all']['fr']['month'][i][j]['kws'][word]
                index += 1

        bar_chart = [month_legend, occurrences]

        df = pd.DataFrame(bar_chart).transpose()
        df.columns=['month_legend', 'value']

        data.append(go.Bar(name=word, x=df['month_legend'], y=df['value']))

        visible_list = [False]*longueur
        visible_list[True_index] = True
        buttons.append(dict(label=word,
                     method="update",
                     args=[{"visible": visible_list},
                           {"title": "Occurrences of '" + word + "'"}]))

    plot = go.Figure(data=data)
    plot.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=buttons)])

    plot.show()
    return True

def evolution_occurrences_most_common_words_daily (number=None, threshold=None, percentage=None) :
    l = create_list_occurrences()
    if number != None :
        l = l[:number]
    elif threshold != None :
        for i in range(len(l)) :
            if l[i][1] < threshold :
                l = l[:i]
                break
    elif percentage != None :
        stop = int(percentage/100*len(l))
        l = l[:stop]


    longueur = len(l)
    article_data = load_data()
    data = []
    buttons = list([dict(label="All",
                     method="update",
                     args=[{"visible": [True]*len(l)},
                           {"title": "Occurrences of the most common words"}])])

    
    occurences = [0]*1096
    years = ['2019', '2020', '2021']
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    days_legend = create_day_legend()
    True_index = -1
    for z in l :
        True_index += 1
        word = z[0]
        for i in years :
            for j in months :
                for k in days :
                    if k in article_data['metadata-all']['fr']['day'][i][j] :
                        if word in article_data['metadata-all']['fr']['day'][i][j][k]['kws'] :
                            occurences[get_day_index(i, j, k)] = article_data['metadata-all']['fr']['day'][i][j][k]['kws'][word]

        bar_chart = [days_legend, occurences]

        df = pd.DataFrame(bar_chart).transpose()
        df.columns=['day_legend', 'value']

        data.append(go.Bar(name=word, x=df['day_legend'], y=df['value']))

        visible_list = [False]*longueur
        visible_list[True_index] = True
        buttons.append(dict(label=word,
                     method="update",
                     args=[{"visible": visible_list},
                           {"title": "Occurrences of '" + word + "'"}]))

    plot = go.Figure(data=data)
    plot.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=buttons)])

    plot.show()


    return True