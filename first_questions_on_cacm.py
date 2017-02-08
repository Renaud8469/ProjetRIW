import nltk
from indexation_of_cacm import *
from first_questions_on_cs276 import *

cacm = open('CACM/cacm.all', 'r')

frequency_list = get_vocabulary_dict(cacm)[0]
frequency_list_sorted = get_voc_freq_rank(frequency_list)

show_plot_log_freq_rank(frequency_list_sorted)
