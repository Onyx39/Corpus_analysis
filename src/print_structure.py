import json

def load_data () :
    # list of data
    #files_name = [file_name for file_name in os.listdir() if '.json' in file_name]

    # name of the lightest file
    file_name = 'src/data/topaz-data732--mali--www.fdesouche.com--20190101--20211231.json'

    # open and load file
    f = open(file_name, 'r', encoding='utf-8')
    data = json.loads(f.read())
    f.close()

    return data


# recursive function
def print_structure(data, deep=0):

    s = chr(9474) + ' '

    if isinstance(data, list):  # if data is list
        print(f"{s * deep}{chr(9492)} list of size {len(data)}")
    elif isinstance(data, dict):  # if data is dict
        if len(data.keys()) >= 30:  # if dict is large
            print(f"{s * deep}{chr(9492)} dict with {len(data.keys())} keys")
        elif len(data.keys()) >= 15:  # if dict is medium
            print(f"{s * deep}{chr(9492)} dict with keys: {' '.join(data.keys())}")
        else:  # if dict is small
            i = 0
            for k, v in data.items():
                if i < 3:  # for only 3 first elements
                    print(f"{s * deep}{chr(9492)} {k}")
                    print_structure(v, deep+1)
                else:
                    print(f"{s * deep}{chr(9492)} ...")
                    break
                i += 1

def main_print_structure () :
    data = load_data()
    print_structure(data)
    return True
