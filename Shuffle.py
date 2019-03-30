# this program is used to output shuffled sentences of random patterns in a proper number
# Clara WAN
# 2017-11-13


# read the files under one directory
file = open('D:\\GigaExtractOutputFiles\\氣.txt', 'r', encoding='utf-8')
mytext = file.readlines()
file.close()
print(len(mytext))

jump_num = len(mytext)//500
print(jump_num)

mylist = []

for i in range(3,len(mytext),jump_num):
    mylist.append(mytext[i])


# write the extracted verb file to the output file
outfile = open('D:\\GigaExtractOutputFiles\\氣500.txt', 'w', encoding='utf-8')
for sentence in mylist:
    outfile.write(sentence)
outfile.close()

print('The 氣500.txt file is created.')






