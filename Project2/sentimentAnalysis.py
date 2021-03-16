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
    yelpData = json.load(yelpFile)
    
    idx = 0
    for i in yelpData:
        print(i)
        idx += 1
        if idx == 100:
            break

reviews_ratings = [[review['stars'], review['text']] for review in yelpData]

# len([word for word in tokens if word not in set(stopwords.words('english')) and word.isalnum()])

wnl = nltk.WordNetLemmatizer()
