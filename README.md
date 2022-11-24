# Corpus_analysis
The goal of this project is to visualise some data collected in a corpus. To do so, I am using 12 json files given by my teacher. These json files contains data and metadata about the words in articles. There are not in this repository because they are too heavy. This programm in entirely coded in python and use the plotly library to show the plots.<br><br>
<b>/!\ TW : These articles come from conspiracy sites, the data collected is therefore sensitive !</b><br><br>

You can use this programm to analyse other files. To do so, create a 'data' folder that will contain some json files (with the same structure !). Do not forget to change the path in <i>load_data</i> in src.print_structure.py !

## Execute the programm

To run the programm, adapt the main.py file according to what you want and run it.

## What can this programme do ?
<ul>
<ol>Print the data structure (in the console)<br>
To do so, use the <i>main_print_structure</i> function in src.print_structure.py</ol>
<ol>Explore the data structure (in the console)<br>
To understand closely the structure of the data, use the <i>explore_data<i> in exploring_data.py. Do not hesitate to modify the function in order to get what you want, this file is useless for the other features.</ol>
<ol>Show the evolution of the number of articles per month<br>
To do so, use the <i>main_month_data</i> funtion in src.print_month_data.py</ol>
<ol>Show the evolution of the occurrence of a word<br>
TO do so, use the <i>evolution_occurrences_annualy/monthy/daily</i> funtions in src.searching_words.py according to what you want. The show the three, use <i>print_all</i> in the same file.<br>
To be sure the word you are searching is in the articles, use <i>word_collecting</i> from src.word_collecting.py</ol> 
<ol>Show the evolution of the occurrence of the most common words<br>
To do so, use the <i>evolution_occurrences_most_common_words_annualy/monthly/daily</i> functions</ol>
</ul>