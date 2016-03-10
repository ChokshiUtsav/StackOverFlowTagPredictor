import sys
import math
import heapq
import logging

test_file_name = str(sys.argv[1])
test_file_desc = open(test_file_name,'r')

prior_file_name = str(sys.argv[2])
prior_file_desc = open(prior_file_name,'r')

likelihood_file_name = str(sys.argv[3])
likelihood_file_desc = open(likelihood_file_name,'r')

logging.basicConfig(filename='naivebayes.log',level=logging.DEBUG)

logging.info("Processing Prior Index started.")
prior_dict={}
for line in prior_file_desc.readlines():
	temp = line.split("|")
	tag = str(temp[0])
	prob = float(temp[1])
	prior_dict[tag] = prob 
logging.info("Processing Prior Index ended.")


logging.info("Processing Likelihood Index started.")
likelihood_dict={}
for line in likelihood_file_desc.readlines():
	temp = line.split("|")
	tag_word = str(temp[0])
	prob = float(temp[1])
	likelihood_dict[tag_word] = prob 
logging.info("Processing Likelihood Index ended.")


total_labels = 0.0
true_labels = 0.0
total_classified = 0.0
true_classified = 0.0


logging.info("Test data processing started.")
for line in test_file_desc.readlines():
	temp = line.strip().split("#@#")
	title_words = temp[0].strip().split()
	tag_words = temp[1].strip().split("|")
	total_labels += len(tag_words)

	assigned_tags = []
	for tag in prior_dict.keys():
		logging.info("Processing tag : " + str(tag))
		total_prob = 0.0
		prior_prob =  prior_dict[tag]
		for word in title_words:
			logging.info("Processing title word : " + str(word))
			key = word+";"+tag
			if key in likelihood_dict:
				prob = prior_prob*likelihood_dict[key]
			else:
				prob = 0.0
			total_prob += prob
		assigned_tags.append((total_prob,tag))

	predicted_tags = heapq.nlargest(3,assigned_tags)
	
	flag = 0
	for tup in predicted_tags:
		if tup[1] in tag_words:
			flag = 1
			true_labels+=1

	if flag == 1:
		true_classified += 1

	total_classified += 1
logging.info("Test data processing started.")

logging.info("Printing accuracy.")
accuracy = (true_labels/total_labels)*100
print "Label-wise Accuracy is  : " + str(accuracy)
print "Total labels : " + str(total_labels)
print "True labels : " + str(true_labels)
accuracy = (true_classified/total_classified)*100
print "Subset-wise Accuracy is  : " + str(accuracy)
print "Total classified titles : " + str(total_classified)
print "True classified titles : " + str(true_classified)