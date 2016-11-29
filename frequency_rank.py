import nltk
from get_token_list import *
from useful_functions import *

cacm = open('CACM/cacm.all', 'r')

token_cacm = get_token_list(cacm)
token_no_common = lower_and_remove_common(token_cacm)

frequency_list = {}
for token in token_no_common:
    if token in frequency_list:
        frequency_list['token'] = frequency_list['token'] + 1/189000
    else:
        frequency_list = frequency_list.update({'token': 1/189000})

print(frequency_list)