from collection import Collection
from get_token_list import *


cacm = open('CACM/cacm.all', 'r')
vocabulary = get_vocabulary_dict(cacm)[0]
index = get_reverse_index(vocabulary, cacm)

cacm_collection = Collection(cacm, vocabulary, index)

boolean = cacm_collection.boolean_search("physics OR computer")
vector = cacm_collection.vector_search("physics")