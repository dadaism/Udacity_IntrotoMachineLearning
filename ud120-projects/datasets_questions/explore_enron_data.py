#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


#print len(enron_data["SKILLING JEFFREY K"])
''' count feature 'poi' 
count = 0
for k, v in enron_data.iteritems():
	#print k, " is ", v
	if v['poi']:
		count = count + 1
print count
'''

''' count feature 'quantified salary' '''
count = 0
for k, v in enron_data.iteritems():
	#print k, " is ", v
	if v['poi'] == True:
		#if v['total_payments'] != 'NaN':
		count = count + 1
print count

#for k in enron_data:
#	print k
	
#print enron_data["PRENTICE JAMES"]['salary'] == 'NaN'
#print enron_data["COLWELL WESLEY"]
#print enron_data["SKILLING JEFFREY K"]["total_payments"]
#print enron_data["LAY KENNETH L"]["total_payments"]
#print enron_data["FASTOW ANDREW S"]["total_payments"]