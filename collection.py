from get_token_list import get_vocabulary_dict, get_reverse_index
from boolean_search import boolean_search

class Collection:

    def __init__(self, file):
        self.file = file
        self.vocabulary = get_vocabulary_dict(self.file)
        self.index = get_reverse_index(self.vocabulary, self.file)


    def boolean_search(self, query):
        boolean_search(self.index, query)


    def vectorial_search(self, query):

