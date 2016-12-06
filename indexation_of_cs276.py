import os
from useful_functions import *


def make_doc_id(directory):
    doc_id_list = []
    for i in range(0, 10):
        for filename in os.listdir(directory + str(i)):
            doc_id_list.append(directory + str(i) + '/' + filename)
    return doc_id_list


def make_dictionary(directory):
    dictionary = {}
    doc_count = 0
    for i in range(0, 10):
        for filename in os.listdir(directory + str(i)):
            words = open(directory + str(i) + '/' + filename).readline()
            tokens = custom_tokenize(words)
            for word in lower_and_remove_common(tokens):
                if not dictionary.get(word):
                    dictionary[word] = {doc_count: 1}
                elif not dictionary.get(word).get(doc_count):
                    dictionary[word][doc_count] = 1
                else:
                    dictionary[word][doc_count] += 1
            doc_count += 1


"""
    Main method for execution
"""


def main():
    global_directory = "CS276/pa1-data/"
    doc_to_doc_id = make_doc_id(global_directory)
    print(len(doc_to_doc_id))


if __name__ == '__main__':
    main()
