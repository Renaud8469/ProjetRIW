from useful_functions import *


def get_id(x):
    return int(''.join(ele for ele in x if ele.isdigit()))


def get_vocabulary_dict(file):
    token_dict = {}
    token_number = 0
    id_to_doc = {}
    latest_mark = ""
    for line in file:
        if ".I " in line:
            id_paper = get_id(line)
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if (".T" in latest_mark) or (".W" in latest_mark) or (".K" in latest_mark):
            if ".T" in latest_mark and line != latest_mark:
                if id_paper in id_to_doc.keys():
                    id_to_doc[id_paper] += line[:-1]
                else:
                    id_to_doc[id_paper] = line[:-1]
            if len(line) > 3:
                total_tokens = custom_tokenize(line)
                current_tokens = lower_and_remove_common(custom_tokenize(line))
                token_number += len(total_tokens)
                for token in current_tokens:
                    word = token
                    if word in token_dict:
                        token_dict[word] += 1
                    else:
                        token_dict[word] = 1
    return token_dict, token_number, id_to_doc


def get_reverse_index(vocabulary, file):
    reverse_index = {}
    all_docs = []
    for key in vocabulary.keys():
        reverse_index[key] = {}
    file.seek(0)
    latest_mark = ""
    for line in file:
        if ".I " in line:
            id_paper = get_id(line)
            all_docs.append(id_paper)
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (
            ".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if (".T" in latest_mark) or (".W" in latest_mark) or (".K" in latest_mark):
            if len(line) > 3:
                current_tokens = lower_and_remove_common(custom_tokenize(line))
                for token in current_tokens:
                    if id_paper in reverse_index[token].keys():
                        reverse_index[token][id_paper] += 1
                    else:
                        reverse_index[token][id_paper] = 1
    return reverse_index, all_docs


def parse_queries(query_file):
    query_dict = {}
    latest_mark = ""
    current_query_id = 0
    for line in query_file:
        if ".I" in line:
            current_query_id = get_id(line)
            query_dict[current_query_id] = ""
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if ".W" in latest_mark and len(line) > 3:
            current_tokens = lower_and_remove_common(custom_tokenize(line))
            for token in current_tokens:
                if len(token) > 1:
                    query_dict[current_query_id] += token + " "
    return query_dict


def parse_answers(answer_file):
    answer_dict = {}
    for line in answer_file:
        current_id = int(line[0:2])
        if current_id in answer_dict.keys():
            answer_dict[current_id].append(int(line[3:7]))
        else:
            answer_dict[current_id] = [int(line[3:7])]
    return answer_dict


# -------------
# Old functions
# -------------


def get_token_list(file):
    token_list = []
    latest_mark = ""
    for line in file:
        if ".I " in line:
            id_paper = get_id(line)
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if (".T" in latest_mark) or (".W" in latest_mark) or (".K" in latest_mark):
            if len(line) > 3:
                current_tokens = custom_tokenize(line)
                token_list = token_list + current_tokens
    return token_list


def get_token_list_half(file):
    token_list = []
    latest_mark = ""
    for line in file:
        if ".I " in line:
            id_paper = get_id(line)
        if (".I " in line) or (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
            latest_mark = line
        if (".T" in latest_mark) or (".W" in latest_mark) or (".K" in latest_mark):
            if len(line) > 3:
                current_tokens = custom_tokenize(line)
                token_list = token_list + current_tokens
        if id_paper >= 1602:
            print(id_paper)
            break
    return token_list
