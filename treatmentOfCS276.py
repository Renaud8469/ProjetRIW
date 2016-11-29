import os
from useful_functions import lower_and_remove_common, custom_tokenize

global_directory = "CS276/pa1-data/"


def count_tokens_and_vocabulary_in_dir(i, vocabulary, token_count):
    for filename in os.listdir(global_directory + str(i)):
        words = open(global_directory + str(i) + '/' + filename).readline()
        tokens = custom_tokenize(words)
        token_count += len(tokens)
        for word in lower_and_remove_common(tokens):
            if not vocabulary.get(word):
                vocabulary[word] = 1
    return {'voc': vocabulary, 'count': token_count}


def count_tokens_and_vocabulary():
    vocabulary = {}
    token_count = 0
    for i in range(0, 5):
        result = count_tokens_and_vocabulary_in_dir(i, vocabulary, token_count)
        vocabulary = result['voc']
        token_count = result['count']
    print("This collection has " + str(token_count) + " tokens at half-collection (5 first directories).")
    print("Its vocabulary is made of " + str(len(vocabulary)) + " words at half-collection.")
    for i in range(5, 10):
        result = count_tokens_and_vocabulary_in_dir(i, vocabulary, token_count)
        vocabulary = result['voc']
        token_count = result['count']
    print("This collection has " + str(token_count) + " tokens.")
    print("Its vocabulary is made of " + str(len(vocabulary)) + " words.")

count_tokens_and_vocabulary()

# This collection has 13611296 tokens at half-collection (5 first directories).
# Its vocabulary is made of 150733 words at half-collection.
# This collection has 23912191 tokens.
# Its vocabulary is made of 244580 words.
