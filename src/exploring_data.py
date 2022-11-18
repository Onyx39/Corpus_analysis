from src.print_structure import load_data

def explore_data () :
    data = load_data()
    l =  []
    index = 0
    for i in data['metadata-all']['fr']['day']['2019']['1']: 
        l.append(i)
    print('\n', l, len(l), '\n')
    for j in l : 
        print(data['metadata-all']['fr']['day']['2019']['1'][j])
        #index += data['metadata-all']['fr']['day']['2019']['1'][j]
    print('index : ', index)
    """
    dic = {}
    for i in l :
        if i in dic :
            dic[i] += 1
        else : dic[i] = 1
    print(dic, len(dic))
    """
    print('num : ', data['metadata-all']['fr']['month']['2019']['1']['num'])
    for i in data['metadata-all']['fr']['month']['2019']['1'] :
        print('---', i, '---')
        for j in data['metadata-all']['fr']['month']['2019']['1'][i] :
            print(j)
    #for i in data['data-all']['2019']['1']['20']:
    #    print(i)
