# read the files under one directory
file = open('D:\\GigaExtractOutputFiles\\Yingying.txt', 'r', encoding='utf-8')
mytext = file.readlines()
file.close()

mylist = []
for line in mytext:
    temp_line=[]
    for ch in line:
        if 0x4e00 <ord(ch)< 0x9fff:
            temp_line.append(ch)
    mylist.append(temp_line)

mynewlist = []
for line in mylist:
    i = 0
    for char in line:
        if char == '的':
            i += 1
    if i == 2:
        mynewlist.append(line)

#write to a file
outfile = open('D:\\GigaExtractOutputFiles\\Yingying-New.txt', 'w', encoding='utf-8')
for line in mynewlist:
    for x in line:
        outfile.write(x)
    outfile.write('\n')
outfile.close()

print('Done Yingying2.txt!')