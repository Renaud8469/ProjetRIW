from useful_functions import docs_in_index
from boolean_search import boolean_search
from math import log, sqrt


class Collection:

    def __init__(self, docs, vocabulary, index):
        self.docs = docs
        self.vocabulary = vocabulary
        self.index = index

    def boolean_search(self, query):
        return boolean_search(self.docs, self.index, query)

    def vector_search(self, query):
        """Based on first course in RIW, slide 171"""
        docs = docs_in_index(self.index)
        s = {}
        results = []
        for doc in docs:
            s[doc] = 0
        n_d = s
        query = query.replace(",", "").split()
        n_q = 0
        for word in query:
            w_q = self.get_idf(word)**2
            n_q += w_q
            if word in self.index.keys():
                posting_list = self.index[word].keys()
                for d in posting_list:
                    w_d = self.get_w(d, word)
                    n_d[d] += w_d
                    s[d] += w_d*w_q
        for doc in s:
            if s[doc] > 0:
                results.append((doc, s[doc]/(sqrt(n_q)*sqrt(n_d[doc]))))
        results.sort(key=lambda tup: tup[1], reverse=True)
        return results

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
            size = len(self.vocabulary)
            idf = log(size / len(self.index[word]), 10)
            return idf
        else:
            return 0

    def get_w(self, doc, word):
        return self.get_log_tf(doc, word) * self.get_idf(word)
