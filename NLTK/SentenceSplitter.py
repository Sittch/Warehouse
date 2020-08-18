import nltk
from nltk import tokenize
from nltk.stem.snowball import SnowballStemmer

rus_stemmer = SnowballStemmer("russian")
output = []

f=open('BrosKTest.txt', encoding='utf-8')
raw=f.read()
text_sents = nltk.sent_tokenize(raw)        

##Check to see if splitter worked
print(text_sents)

for sent in text_sents:
    for word in sent:
        if word[0].isupper():
            print(word)


####Attempt at lemmatization....
##for sent in text_sents:
##    output.append(" ".join([.stem(i) for i in sent.split()]))
##            
##for item in output:
##    print(item)




##rus_stemmer.stem(text_sents)
