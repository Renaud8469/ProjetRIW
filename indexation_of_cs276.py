import os
from useful_functions import *

"""
    This file gathers functions used to create an index on CS276 collection.
"""


# This function creates 2 dictionaries to bind documents and documentIDs.
# The first one has a structure { doc : docID } and the other { docID : doc }.
# The first one is mandatory for the index creation, the second one is useful to answer queries.
def make_doc_id_to_doc(directory):
    doc_id_dict = {}
    doc_dict = {}
    count = 0
    for i in range(0, 10):
        for filename in os.listdir(directory + str(i)):
            doc_id_dict[count] = directory + str(i) + '/' + filename
            doc_dict[directory + str(i) + '/' + filename] = count
            count += 1
    return doc_id_dict, doc_dict


# This function creates the index for the CS276 collection.
# Its structure is like this : { term : { docID : #occurences of the term in the doc referenced by docID } }.
def make_dictionary(directory):
    dictionary = {}
    doc_id_dict, doc_dict = make_doc_id_to_doc(directory)
    for i in range(0, 10):
        for filename in os.listdir(directory + str(i)):
            doc_id = doc_dict[directory + str(i) + '/' + filename]
            words = open(directory + str(i) + '/' + filename).readline()
            tokens = custom_tokenize(words)
            for word in lower_and_remove_common(tokens):
                if not dictionary.get(word):
                    dictionary[word] = {doc_id: 1}
                elif not dictionary.get(word).get(doc_id):
                    dictionary[word][doc_id] = 1
                else:
                    dictionary[word][doc_id] += 1
            doc_id += 1
    return doc_id_dict, dictionary


"""
    Main method for execution
"""


def main():
    global_directory = "CS276/pa1-data/"
    # doc_to_doc_id = make_doc_id(global_directory)
    doc_id_dict, dictionary = make_dictionary(global_directory)


if __name__ == '__main__':
    main()
