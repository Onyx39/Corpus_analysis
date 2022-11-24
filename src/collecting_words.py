from src.print_structure import load_data

def word_collecting () :

    data = load_data()
    word_list = []

    years = ['2019', '2020', '2021']
    months = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    days = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
    for i in years :
        for j in months :
            for k in days :
                if k in data['metadata-all']['fr']['day'][i][j] :
                    for l in data['metadata-all']['fr']['day'][i][j][k]['kws'] :
                        if l not in word_list :
                            word_list.append(l)
    #print(word_list, len(word_list))
    return word_list
