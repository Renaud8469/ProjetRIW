import nltk
from get_token_list import *
from useful_functions import *

cacm = open('CACM/cacm.all', 'r')

frequency_list = get_frequency_list(cacm)

print(frequency_list)