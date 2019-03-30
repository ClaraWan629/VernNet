# extract a term from the raw data
# 2017-11-09
# Clara WAN

import sys
import glob


# read the files under one directory
path = 'E:\\RawGigaword_sample\\*'
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
mynewlist = []
for line in mylist:
    if line.find("耳語") >= 0:
        mynewlist.append(line)

# write the extracted verb file to the output file
outfile = open('E:\\GigaExtractOutputFiles\\耳語.txt', 'w', encoding='utf-8')
for sentence in mynewlist:
    outfile.write(sentence + '\n')
outfile.close()

print('The 耳語.txt file is created.')






