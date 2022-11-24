# Corpus_analysis
The goal of this project is to visualise some data collected in a corpus. To do so, I am using 12 json files given by my teacher. These json files contains data and metadata about the words in articles. There are not in this repository because they are too heavy.<br>
<u>/!\ TW : These articles come from conspiracy sites, the data collected is therefore sensitive !</u><br>
This programm in entirely coded in python and use the plotly library to show the plots.<br><br>

You can use this programm to analyse other files. To do so, create a 'data' folder that will contain some json files (with the same structure !). Do not forget to change the path in <i>load_data</i> in src.print_structure.py !

## Execute the programm
To run the programm, adapt the main.py file according to what you want and run it.

## What can this programme generate?
<ul>
<li>1. The data structure<br>
To do so, use the <i>main_print_structure</i> function in src.print_structure</li>
<li>2. The evolution of the number of articles per month<br>
To do so, use the <i>main_month_data</i> funtion in src.print_month_data</li>
</ul>