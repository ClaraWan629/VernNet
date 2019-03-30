import nltk
from nltk.corpus import sinica_treebank

sinica_Text = sinica_treebank.sents()

#print(len(sinica_Text))
#print(sinica_Text)
# write to a file
output = open('D:\\VerbNet_Clara\\nltk_sinica_treebank\\sinica_raw.txt', 'w', encoding='utf-8')
for sentence in sinica_Text:
    string =''.join(sentence)
    output.write(string + '\n')
output.close()


print('The raw text of sinica has been saved.')


