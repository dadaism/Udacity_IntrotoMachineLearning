#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification

    the list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    the actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project

    the data is stored in lists and packed away in pickle files at the end

"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

from nltk.corpus import stopwords
sw = stopwords.words("english")

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
        if temp_counter % 200 == 0 :
            print temp_counter, " processed"
        if True:
            path = os.path.join('..', path[:-1])
            # print path
            email = open(path, "r")

            ### use parseOutText to extract the text from the opened email
            text = parseOutText(email)
            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            name_list = ["sara", "shackleton", "chris", "germani"]
            text = text.replace("sara", "").replace("shackleton", "").replace("chris", "").replace("germani", "")
            text = text.replace("sshacklensf", "").replace("cgermannsf", "")
            #text =  ' '.join([word for word in text.split() if word not in name_list])
  
            ### remove stop words
            # text =  ' '.join([word for word in text.split() if word not in sw])
            # print text
            ### append the text to word_data
            word_data.append(text)
            
            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            if name == "sara":
                from_data.append(0)
            elif name == "chris":
                from_data.append(1)
            email.close()

print temp_counter    
print "emails processed"
from_sara.close()
from_chris.close()

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )

#word_data = pickle.load( open("your_word_data.pkl", "rb") )
#from_data = pickle.load( open("your_email_authors.pkl", "rb") )

### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

count_vect = CountVectorizer(stop_words = "english")
X_train_counts = count_vect.fit_transform(word_data)
# print X_train_counts.shape
tf_transformer = TfidfTransformer(use_idf=True).fit(X_train_counts)
X_train_tf = tf_transformer.transform(X_train_counts)
#print X_train_tf.shape
#print len(count_vect.get_feature_names())
#print count_vect.get_feature_names()[34597]
'''import nltk
sw = stopwords.words("english")
for word in sw:
    text = text.replace(word)

print tex
'''