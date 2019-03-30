import sys
import glob
import re


# read the files under one directory
path = 'D:\\TaggedGiga_all\\*'
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

#break sentences with punctuations
mynewlist = []
for item in mylist:
    temp_list = re.split('[?.,!;]', item)
    for x in temp_list:
        mynewlist.append(x)

#find out the _的_N patterns
wantedlist= []
for line in mynewlist:
    if line.find('的') >= 0:
        if line.find('N') >= line.find('的') + 5:
            wantedlist.append(line.strip('(COMMACATEGORY)(PERIODCATEGORY)'))

#write to a file
outfile = open('D:\\GigaExtractOutputFiles\\Yingying.txt', 'w', encoding='utf-8')
for sentence in wantedlist:
    outfile.write(sentence + '\n')
outfile.close()

print('The Yingying.txt is created.')

