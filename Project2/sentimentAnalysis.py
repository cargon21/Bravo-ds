# Programmers: Jordan DeGiacomo & Carson Synter
# Last DOM: 3/16/2020
# Course: CMPSC 310
# Purpose: Write a program that shall calculate word sentiment level, based on the user reviews from the Yelp academic dataset

# Game plan: 1) Load JSON file (small set), final run will have all reviews
#            2) Extract all review text and star ratings
#            3) Break each review into individuals words using NLTK
#            4) Lemmatize the words
#            5) Filter out stop words and words that are not in the words corpus
#            6) For each lemma calculate its star rating, if lemma is used in less than 10 reviews discard it
#            7) Save 500 most negative lemmas and 500 most positive lemmas and their respective sentiment levels in a one two-column CSV file
#               Lemmas in column one and levels in the second, sorted in decending order of sentiment analysis

import json
import csv
import nltk
from collections import Counter
from nltk.corpus import stopwords
from nltk.corpus import words

# open sing json
with open ("../../yelp_academic_dataset_review_small.json") as yelpFile:
    real_yelp_data = json.load(yelpFile)

# create some sample yelp data to experiment on
yelp_data = []
index = 0
for i in real_yelp_data:
    if index > 3:
        break
    yelp_data.append(i)
    index+= 1


wnl = nltk.WordNetLemmatizer()
reviews_ratings = []

for review in yelp_data:
    tokenize = nltk.word_tokenize(review['text'])
    
    lemmatize = [wnl.lemmatize(w) for w in tokenize]
            
    filter_words = [i for i in lemmatize if i not in set(stopwords.words('english')) and i.isalnum()]
    
    reviews_ratings.append([review['stars'], filter_words])
    
    
    
    
    
# reviews_ratings = [[review['stars'], nltk.word_tokenize(review['text'])] for review in yelp_data]

# wnl = nltk.WordNetLemmatizer()



# len([word for word in tokens if word not in set(stopwords.words('english')) and word.isalnum()])

# wnl = nltk.WordNetLemmatizer()

# a = reviews_ratings[0][1]
# li = [wnl.lemmatize(w) for w in a]

# for i in range(150): 
#     print(a[i] + " ---- " + li[i], str(a[i] == li[i]))
