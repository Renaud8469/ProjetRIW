import nltk
import os
from useful_functions import lower_and_remove_common

global_directory = "CS276/pa1-data/"


def count_tokens_cs76():
    token_count = 0
    for i in range(0, 9):
        for filename in os.listdir(global_directory + str(i)):
            words = open(global_directory + str(i) + '/' + filename).readline()
            tokens = nltk.word_tokenize(words)
            token_count += len(tokens)

    return token_count


def count_vocabulary_cs76():
    vocabulary = []
    for i in range(0, 9):
        for filename in os.listdir(global_directory + str(i)):
            words = open(global_directory + str(i) + '/' + filename).readline()
            tokens = nltk.word_tokenize(words)
            for word in tokens:
                if word not in vocabulary:
                    vocabulary.append(word)
    return len(vocabulary)


def count_tokens_and_vocabulary():
    vocabulary = {}
    token_count = 0
    for i in range(0, 9):
        for filename in os.listdir(global_directory + str(i)):
            words = open(global_directory + str(i) + '/' + filename).readline()
            tokens = nltk.word_tokenize(words)
            token_count += len(tokens)
            for word in lower_and_remove_common(tokens):
                if not vocabulary.get(word):
                    vocabulary[word] = 1

    print("This collection has " + str(token_count) + " tokens.")
    print("Its vocabulary is made of " + str(len(vocabulary)) + "words.")


count_tokens_and_vocabulary()
