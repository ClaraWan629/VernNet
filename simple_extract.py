# extract 放
import sys
import glob


# read the files under one directory
path = 'D:\\TaggedGiga-Sample\\*'
files = glob.glob(path)

mylist = []
for file in files:
    f = open(file, 'r', encoding='utf-8')
    text = f.readlines()

    for line in text:
        if line.find("放") >= 0:
            mylist.append(line)
    f.close()

outfile = open('D:\\Fang-Giga-sample.txt', 'w', encoding='utf-8')
for sentence in mylist:
    outfile.write(sentence + '\n')
outfile.close()

print('The Fang file is created.')


