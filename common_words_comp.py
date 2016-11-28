common_words_file = open('CACM/common_words')
common_words = [line.rstrip('\n') for line in common_words_file]
common_words_file.close()


def lower_and_remove_common(word_list):
    token_list = []
    for word in word_list:
        if word not in common_words:
            token_list.append(word.lower())
    return token_list

