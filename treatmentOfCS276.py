import nltk,os

global_directory = "CS276/pa1-data/"

count = 0

for i in range(0, 9):
    for file in os.listdir(global_directory + str(i)):
        count += 1

print(count)




