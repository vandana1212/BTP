bag_of_words_tags={};
bag_of_words_tags["film"]=-3
bag_of_words_tags["television"]=-3
bag_of_words_tags["studio"]=-1
bag_of_words_tags["education"]=3
bag_of_words_tags["tv"]=-3
bag_of_words_tags["author"]=2
bag_of_words_tags["book"]=2
bag_of_words_tags["campus"]=2
bag_of_words_tags["software"]=5
bag_of_words_tags["hotel"]=0
bag_of_words_tags["resort"]=0
bag_of_words_tags["social"]=-3
bag_of_words_tags["club"]=-3
bag_of_words_tags["website"]=2
bag_of_words_tags["media"]=3
bag_of_words_tags["news"]=3
bag_of_words_tags["company"]=1
bag_of_words_tags["publisher"]=2
bag_of_words_tags["artist"]=-1
bag_of_words_tags["musician"]=-1
bag_of_words_tags["music"]=0
bag_of_words_tags["band"]=0
bag_of_words_tags["entertainment"]=-3
bag_of_words_tags["community"]=-3
bag_of_words_tags["organisation"]=2
bag_of_words_tags["city"]=1
bag_of_words_tags["personal"]=-1
bag_of_words_tags["blog"]=0
bag_of_words_tags["internet"]=-2
bag_of_words_tags["building"]=1
bag_of_words_tags["college"]=2
bag_of_words_tags["university"]=2
bag_of_words_tags["comedian"]=-5
bag_of_words_tags["actor"]=-3
bag_of_words_tags["society"]=1
bag_of_words_tags["cultural"]=1
bag_of_words_tags["research"]=4
bag_of_words_tags["retail"]=-4
bag_of_words_tags["app"]=-2
bag_of_words_tags["school"]=1
bag_of_words_tags["programme"]=-2
bag_of_words_tags["engineering"]=2
bag_of_words_tags["service"]=2
bag_of_words_tags["shoe"]=-2
bag_of_words_tags["shop"]=-2
bag_of_words_tags["clothes"]=-1
bag_of_words_tags["shoe"]=-2
bag_of_words_tags["politician"]=-2
bag_of_words_tags["restaurant"]=-2
bag_of_words_tags["centre"]=1
bag_of_words_tags["Sport"]=1
bag_of_words_tags["recreation"]=-2
bag_of_words_tags["fun"]=-3
bag_of_words_tags["arts"]=1
bag_of_words_tags["humanities"]=1
bag_of_words_tags["business"]=2
bag_of_words_tags["magazine"]=1
bag_of_words_tags["interest"]=-3
bag_of_words_tags["peformance"]=-2
bag_of_words_tags["cause"]=2
bag_of_words_tags["games"]=-3
bag_of_words_tags["toys"]=-3
bag_of_words_tags["monument"]=1
bag_of_words_tags["product"]=-1
bag_of_words_tags["photographer"]=-3
bag_of_words_tags["science"]=3
bag_of_words_tags["technology"]=4
bag_of_words_tags["developer"]=5
bag_of_words_tags["season"]=-3
bag_of_words_tags["consultant"]=3
bag_of_words_tags["furniture"]=-2
bag_of_words_tags["youth"]=3
bag_of_words_tags["organization"]=1
bag_of_words_tags["public"]=0
bag_of_words_tags["nonprofit"]=2
bag_of_words_tags["non-governmental"]=2
bag_of_words_tags["athlete"]=-2
bag_of_words_tags["sport"]=1
bag_of_words_tags["event"]=-1
bag_of_words_tags["venue"]=-2
bag_of_words_tags["clothing"]=-2
bag_of_words_tags["brand"]=-2
bag_of_words_tags["tutor"]=3
bag_of_words_tags["teacher"]=4
bag_of_words_tags["health"]=2
bag_of_words_tags["beauty"]=1
bag_of_words_tags["food"]=-3
bag_of_words_tags["beverage"]=-3
bag_of_words_tags["show"]=-3
bag_of_words_tags["market"]=0
bag_of_words_tags["accessories"]=-2
bag_of_words_tags["cinema"]=-3
bag_of_words_tags["non-profit"]=2
bag_of_words_tags["producer"]=-2
bag_of_words_tags["travel"]=-2
bag_of_words_tags["writer"]=2
bag_of_words_tags["mental"]=2
bag_of_words_tags["medical"]=3
bag_of_words_tags["agricultural"]=3
bag_of_words_tags["cooperative"]=2
bag_of_words_tags["character"]=-3
bag_of_words_tags["journalist"]=2
bag_of_words_tags["motivational"]=3
bag_of_words_tags["speaker"]=2
bag_of_words_tags["e-commerce"]=-3
bag_of_words_tags["information"]=1
bag_of_words_tags["consultation"]=2
bag_of_words_tags["fictional"]=-3
bag_of_words_tags["lawyer"]=22
bag_of_words_tags["theatrical"]=-1
bag_of_words_tags["play"]=-1
bag_of_words_tags["entrepreneur"]=2
bag_of_words_tags["tech"]=5
bag_of_words_tags["test"]=2
bag_of_words_tags["preparation"]=2
bag_of_words_tags["professional"]=2
bag_of_words_tags["armed"]=3
bag_of_words_tags["computer"]=2
bag_of_words_tags["caterer"]=-3
bag_of_words_tags["pizza"]=-3
bag_of_words_tags["league"]=-2
bag_of_words_tags["organic"]=1
bag_of_words_tags["grocery"]=-2
bag_of_words_tags["broadcasting"]=2
bag_of_words_tags["production"]=2
bag_of_words_tags["video"]=-4
bag_of_words_tags["career"]=3
bag_of_words_tags["counselor"]=2
bag_of_words_tags["kitchen"]=-1
bag_of_words_tags["cooking"]=-1
bag_of_words_tags["chef"]=-3
bag_of_words_tags["amusement"]=-4
bag_of_words_tags["watches"]=-4
bag_of_words_tags["jewelry"]=-4
bag_of_words_tags["retail"]=-4
bag_of_words_tags["lounge"]=-3
bag_of_words_tags["club"]=1
bag_of_words_tags["stadium"]=-1
bag_of_words_tags["arena"]=-1
bag_of_words_tags["telecommunication"]=0

tag_bag_pos=[]
tag_bag_neg=[]
tag_bag_neutral=[]

for element in bag_of_words_tags:
    if (bag_of_words_tags[element]==1):
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
 
#x='Musician/Band', 'Education Website', 'Musician/Band', 'Product/Service', 'Artist', 'Photographer', 'App Page', 'Artist', 'Personal Blog', 'Science, Technology & Engineering', 'Musician/Band', 'Social Service', 'TV Season', 'Entertainment Website', 'Educational Consultant', 'Social Club', 'App Page', 'Community', 'Musician/Band', 'Community', 'Comedian', 'Album', 'Musician/Band', 'Community Service', 'Public Figure', 'Musician/Band', 'College & University', 'College & University', 'Furniture', 'News & Media Website', 'Local Business', 'Performing Arts', 'Sports', 'Event', 'Games/Toys', 'Organization', 'Youth Organization', 'Community Organization', 'Media/News Company', 'Public Figure', 'Performing Arts', 'Blogger', 'Sports', 'Public Figure', 'Board Game', 'College & University', 'Comedian', 'Public Figure', 'Entrepreneur', 'Song', 'Artist', 'Community', 'Entertainment Website', 'Public Figure', 'Musician/Band', 'College & University', 'School', 'Musician/Band', 'Community', 'Non-Governmental Organization (NGO)', 'Interest', 'Artist', 'Musician/Band', 'Athlete', 'Sport', 'Artist', 'Musician', 'Community', 'Community', 'Nonprofit Organization', 'Musician/Band', 'Performing Arts', 'Just For Fun', 'Festival', 'Education', 'Organization', 'Education', 'College & University', 'Arts & Entertainment', 'Performance & Event Venue', 'Musician/Band', 'Musician/Band', 'Personal Coach', 'Community', 'Musician/Band', 'Clothing (Brand)', 'Tutor/Teacher', 'Community', 'College & University', 'Science Website', 'Video Game', 'App Page', 'Games/Toys', 'Entertainment Website', 'Website', 'Games/Toys', 'App Page', 'Health/Beauty', 'Food & Beverage Company'

import pandas as pd
import csv
import re 
df=pd.read_csv(r"C:\Users\VANDANA\Downloads\Edited.csv")

for (idx,row) in df.iterrows():
    
    x = row.iloc[10]
    #print(x)
    print(x)
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



