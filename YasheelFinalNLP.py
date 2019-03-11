import pandas as pd
import os
import csv


df = pd.read_csv(r"C:\Users\VANDANA\Downloads\Yasheel_bag.csv")
bags_of_words_tags = {}
for index, row in df.iterrows():
    bags_of_words_tags[row[0]] = row[1]
    
print(bags_of_words_tags)


tag_bag_pos=[]
tag_bag_neg=[]
tag_bag_neutral=[]

for element in bag_of_words_tags:
    if (bag_of_words_tags[element]>=0):
        {
                tag_bag_pos.append(element)
        }
    elif (bag_of_words_tags[element]==0):
        {
                tag_bag_neutral.append(element)
        }
    else:
        {
                tag_bag_neg.append(element)
        }

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize 
import re
new_tag_bag_pos={}
new_tag_bag_neg={}
new_tag_bag_neutral={}

stemmer=PorterStemmer()

for i in tag_bag_pos:
    new_tag_bag_pos[stemmer.stem(i)]=bag_of_words_tags[i]
for i in tag_bag_neg:
    new_tag_bag_neg[stemmer.stem(i)]=bag_of_words_tags[i]
for i in tag_bag_neutral:
    new_tag_bag_neutral[stemmer.stem(i)]=bag_of_words_tags[i]

print (new_tag_bag_pos)
print(new_tag_bag_neg)
print(new_tag_bag_neutral)

import pandas as pd
import csv
import re 
df=pd.read_csv(r"C:\Users\VANDANA\Downloads\Edited.csv")

for (idx,row) in df.iterrows():
    
    x = row.iloc[9]
    #print(x)
    #print(x)
    x=x.split(',')
    
    rating_student = 0
    ratio_pos_to_total = 0

    pos=0
    total=0

    for i in x:
        i=str(i)
        i.encode("ascii","ignore")
        #print(i)
        rating_sentence = 0
        words = re.findall(r"[\w']+", i)
        #words=str(words)
        #print (words)
        stemmer=PorterStemmer()
        count_pos=0
        count_neg=0
        for j in words :
            stemmed_word=stemmer.stem(j)
            if (stemmed_word in new_tag_bag_pos):
                rating_sentence = rating_sentence + new_tag_bag_pos[stemmed_word]
            elif (stemmed_word in new_tag_bag_neg) :
                rating_sentence = rating_sentence + new_tag_bag_neg[stemmed_word]
    
        if (rating_sentence > 0):
            pos=pos+1
            
        total=total+1
    
        rating_student = rating_student + rating_sentence
    
    #print(x),
    print(rating_student)
    
    ratio_pos_to_total = ((float)(pos)/(float)(total))
#    print(ratio_pos_to_total)



