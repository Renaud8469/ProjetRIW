import nltk

def get_id(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

def get_token_list(file):
    token_list = []
    latestMark = ""
    for line in file:
        if ".I " in line:
            id_paper = get_id(line)
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
            latestMark = line
        if (".T" in latestMark) or (".W" in latestMark) or (".K" in latestMark):
            if len(line) > 3:
                current_tokens = nltk.word_tokenize(line)
                token_list = token_list + current_tokens
    return token_list


