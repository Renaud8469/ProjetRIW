import nltk

cacm = open('CACM/cacm.all', 'r')

def get_id(x):
    return int(''.join(ele for ele in x if ele.isdigit()))

latestMark = ""
tokensCACM = []

for line in cacm:
    if ".I " in line:
        idPaper = get_id(line)
        print(idPaper)
    if (".T" in line) or (".W" in line) or (".B" in line) or (".A" in line) or (".N" in line) or (".X" in line) or (".K" in line):
        latestMark = line
    if (".T" in latestMark) or (".W" in latestMark) or (".K" in latestMark):
        if len(line) > 3:
            currentTokens = nltk.word_tokenize(line)
            tokensCACM = tokensCACM + currentTokens

tokensNumber = len(tokensCACM)
print(tokensNumber)