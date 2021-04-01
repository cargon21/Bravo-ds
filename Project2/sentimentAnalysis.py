#----------------------------------------------------------------------------------
# - Programmers: Jordan DeGiacomo & Carson Synter
# - Last DOM: 3/16/2020
# - Course: CMPSC 310
# - Purpose: Write a program that shall calculate word sentiment level, based on 
#   the user reviews from the Yelp academic dataset
# - Final Execution time: ~ 2.5 minutes
#----------------------------------------------------------------------------------

import json
import csv
import nltk
import sys
from nltk.corpus import stopwords
from nltk.corpus import words
from statistics import mean 

# Open the JSON file
try:
    with open ("../../yelp_academic_dataset_review_small.json") as yelpFile:
        yelp_data = json.load(yelpFile)
except Exception as e:
    print(f"there was an error opening the file: {e})")
    sys.exit()

# Sets of english words and stopwords
stopwords = set(stopwords.words('english'))
corpus = set(words.words("en"))

wnl = nltk.WordNetLemmatizer() #  Word lemmatizer
reviews_ratings = {}

for review in yelp_data:
    
    # Lemmatize each review
    lemmatize = [wnl.lemmatize(w) for w in nltk.word_tokenize(review['text'].lower())]
    
    # Filter the review
    filter_words = set([i for i in lemmatize if i not in stopwords and i.isalnum() and i in corpus])
    
    for word in filter_words:
        if word not in reviews_ratings.keys(): # New entry if non existent
            reviews_ratings[word] = [review['stars']]
        else:
            reviews_ratings[word].append(review['stars']) # Add the review to the word

# Remove lemmas used in fewer than 10 ratings                                     
for key, value in reviews_ratings.copy().items():
    if len(value) < 10:
        del reviews_ratings[key]
    else:
        reviews_ratings[key] = mean(value)

final = list(sorted(reviews_ratings.items(), key=lambda item: item[1], reverse = True))

file_name = "reviews.csv"

#DZ: You have extra line breaks at the end of each line.
# Open and write to the CSV file
with open(file_name, 'w') as csvfile:
       writer = csv.writer(csvfile)
       writer.writerow(("Word", "AVG Rating"))
       
       writer.writerow(("Word", "Highest Ratings"))
       writer.writerows(final[0:500])
       
       writer.writerow(("Word", "Lowest Ratings"))
       writer.writerows(final[-501:-1])
    
print("Program executed successfully :)")
