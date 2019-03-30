# giga pos tagged
# transfer <p> to sentences
# strip tagged words to words only
# Clara
# 2017-11-07
# a case of Fang 放
import sys
import glob


# read the files under one directory
path = 'E:\\TaggedGiga_all\\*'
files = glob.glob(path)

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

## locate 放(V
mylist_special = []
for line in mylist:
    if line.find(" 煩(V") >= 0:
        mylist_special.append(line)

## seprate words from tags
mynewlist = []
for sentence in mylist_special:
    tagged_words = sentence.split(" ")
    words = []
    for tagword in tagged_words:
        temp_words = tagword.split("(")
        words.append(temp_words[0])
    newsentence = "".join(words)
    mynewlist.append(newsentence)

#write the stripped sentencese to a file
outfile = open('E:\\GigaExtractOutputFiles\\煩.txt', 'w', encoding='utf-8')
for sentence in mynewlist:
    outfile.write(sentence + '\n')
outfile.close()

print('The 煩.txt is created.')


