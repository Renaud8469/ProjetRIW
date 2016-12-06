import nltk
from get_token_list import *
from treatmentOfCS276 import *

cacm = open('CACM/cacm.all', 'r')

frequency_list = get_vocabulary_dict(cacm)[0]
frequency_list_sorted = get_voc_freq_rank(frequency_list)

show_plot_freq_rank(frequency_list_sorted)