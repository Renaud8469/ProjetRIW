from get_token_list import get_vocabulary_dict, get_reverse_index
from boolean_search import boolean_search
from math import log

class Collection:

    def __init__(self, file):
        self.file = file
        self.vocabulary = get_vocabulary_dict(self.file)
        self.index = get_reverse_index(self.vocabulary[0], self.file)


    def boolean_search(self, query):
        boolean_search(self.index, query)


    def vector_search(self, query):
        size = len(self.vocabulary[0])
        s = [0]*size
        query = query.replace(",", "").split()
        for word in query:
            


    def get_log_tf(self, doc, word):
        if word in self.index.keys():
            if doc in self.index[word].keys():
                return 1 + log(self.index[word][doc], 10)
            else:
                return 0
        else:
            return 0


    def get_idf(self, word):
        if word in self.index.keys():
            size = len(self.vocabulary[0])
            idf = log(size / len(self.index[word]), 10)
            return idf
        else:
            return 0


    def get_w(self, doc, word):
        return self.get_log_tf(doc, word) * self.get_idf(word)