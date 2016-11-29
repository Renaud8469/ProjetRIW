import nltk

common_words_file = open('CACM/common_words')
common_words = {}
for line in common_words_file:
    common_words[line.rstrip('\n')] = 1
common_words_file.close()


def lower_and_remove_common(word_list):
    token_list = []
    for word in word_list:
        if not common_words.get(word):
            token_list.append(word.lower())
    return token_list


def custom_tokenize(entry_string):
    tokenizer = nltk.tokenize.RegexpTokenizer('[a-zA-Z]+')
    return tokenizer.tokenize(entry_string)
