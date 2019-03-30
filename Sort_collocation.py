# sort the target sentences by collocation of the verb
# 2017-11-10
# Clara WAN

import nltk
from nltk import FreqDist

# read one file
f = open("D:\\GigaExtractOutputFiles\\放-shuffle400.txt", 'r', encoding='utf-8')
text = f.readlines()
f.close()

# identify the collocation-2gram of the verb fang
mylist = []
mark_list = []
for line in text:
    temp_list = []
    mark = ""

    for word in line:
        temp_list.append(word)

    for i in range(len(temp_list)):
        if temp_list[i] == '放':
            mark = '放' + temp_list[i+1]
            break

    newline = mark + '\t' + line
    mylist.append(newline)
    mark_list.append(mark)

fd = nltk.FreqDist(line for line in mark_list)
feature_frequency = fd.most_common()

def secondchar(s):
    return s[1]
mynewlist = sorted(mylist, key = secondchar)

# write the extracted verb file to the output file
outfile = open('D:\\GigaExtractOutputFiles\\Fang-sorted_shuffle400.txt', 'w', encoding='utf-8')
for sentence in mynewlist:
    outfile.write(sentence)
outfile.close()

# write the frequency distribution of 2grams to the output file
outfile2 = open('D:\\GigaExtractOutputFiles\\mark_fd_shuffle400.txt.txt', 'w', encoding='utf-8')
for m,freq in feature_frequency:
    outfile2.write(m + '\t' + str(freq) + '\n')
outfile2.close()
print('The Fang-sorted.txt file and the fd of 2 grams are created.')






