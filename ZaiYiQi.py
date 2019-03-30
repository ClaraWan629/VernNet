# extract the context of 在一起 from the raw data
# 2018-02-01
# Clara WAN

import sys
import glob
import nltk
from nltk import FreqDist


# read the files under one directory
path = 'D:\\RawGigaword_all\\*'
files = glob.glob(path)

# read all the files and transfer sentences between <p> and </p> into one individual line
mylist = []
for file in files:
    f = open(file, 'r', encoding='utf-8')
    text = f.readlines()
    temp_string = ""
    sent_status = 0

    for line in text:
        if line.find("<P>") >= 0:
            sent_status = 1
        elif line.find("</P>") >= 0:
            sent_status = 0
            mylist.append(temp_string)
            temp_string = ""
        elif sent_status == 1:
            temp_string += line.strip('\n')

    f.close()

# locate the sentences that contain the target verb and save the sentences into a new list
Pre_bigrams = []
Pre_unigrams = []
Post_bigrams = []
Post_unigrams = []
for line in mylist:
    if line.find("在一起") >= 0:
        index = line.find("在一起")
        Pre_bigrams.append(line[index-2] + line[index-1])
        Pre_unigrams.append(line[index-1])
        if (index + 4) < len(line):
            Post_unigrams.append(line[index+3])
            Post_bigrams.append(line[index+3] + line[index + 4])


fd = nltk.FreqDist(xx for xx in Pre_bigrams)
feature_frequency_prebi = fd.most_common()

fd = nltk.FreqDist(xx for xx in Pre_unigrams)
feature_frequency_preuni = fd.most_common()

fd = nltk.FreqDist(xx for xx in Post_bigrams)
feature_frequency_postbi = fd.most_common()

fd = nltk.FreqDist(xx for xx in Post_unigrams)
feature_frequency_postuni = fd.most_common()

# write the extracted verb file to the output file
outfile = open('D:\\GigaExtractOutputFiles\\在一起_pre_bigrams.txt', 'w', encoding='utf-8')
for xx, f in feature_frequency_prebi:
    outfile.write(xx + '\t' + str(f) + '\n')
outfile.close()

outfile = open('D:\\GigaExtractOutputFiles\\在一起_pre_unigrams.txt', 'w', encoding='utf-8')
for xx, f in feature_frequency_preuni:
    outfile.write(xx + '\t' + str(f) + '\n')
outfile.close()

outfile = open('D:\\GigaExtractOutputFiles\\在一起_post_bigrams.txt', 'w', encoding='utf-8')
for xx, f in feature_frequency_postbi:
    outfile.write(xx + '\t' + str(f) + '\n')
outfile.close()

outfile = open('D:\\GigaExtractOutputFiles\\在一起_post_unigrams.txt', 'w', encoding='utf-8')
for xx, f in feature_frequency_postuni:
    outfile.write(xx + '\t' + str(f) + '\n')
outfile.close()

print('The 在一起 context files are created.')






