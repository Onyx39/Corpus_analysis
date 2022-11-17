import pandas as pd
import plotly.express as px
from src.print_structure import load_data

# Creer le permier bar chart
def month_data (data) :
    month_data = []
    for i in data["metadata-all"]["fr"]["month"]["2019"] :
        month_data.append(i)
    for i in data["metadata-all"]["fr"]["month"]["2020"] :
        month_data.append(i)
    for i in data["metadata-all"]["fr"]["month"]["2021"] :
        month_data.append(i)

    month_legend = ["01/19", "02/19", "03/19", "04/19", "05/19", "06/19", "07/19", "08/19", "09/19", "10/19", "11/19", "12/19", 
                    "01/20", "02/20", "03/20", "04/20", "05/20", "06/20", "07/20", "08/20", "09/20", "10/20", "11/20", "12/20",
                    "01/21", "02/21", "03/21", "04/21", "05/21", "06/21", "07/21", "08/21", "09/21", "10/21", "11/21", "12/21"]

    bar_chart_data = [month_legend, month_data]

    month_data_df = pd.DataFrame(bar_chart_data).transpose()
    month_data_df.columns=['month', 'value']

    fig = px.bar(month_data_df, x='month', y="value", title="Evolution of the number of articles")
    fig.show()

def main2() :
    data = load_data()
    month_data(data)