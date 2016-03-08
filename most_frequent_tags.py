import sys
import heapq
import logging

file_name = str(sys.argv[1])
input_file_desc = open(file_name,'r')
logging.basicConfig(filename='most_frequent_tags.log',level=logging.DEBUG)

tag_dict = {}
logging.info("------------------------------------")

logging.info("Primary Index Processing Started.")
count = 0
for line in input_file_desc.readlines():
	words = line.strip().split(";")
	for w in words :
		temp = w.split("|")
		tag = temp[0]
		freq = int(temp[1])
		if tag not in tag_dict:
			tag_dict[tag]=freq
		else :
			tag_dict[tag]+=freq
	logging.info("line #"+str(count)+" has been processed")
	count+=1
input_file_desc.close()
logging.info("Primary Index Processing Ended.")

logging.info("Writing to tagfreq.in Started.")
output_file_desc = open("tagfreq.in",'w')

tag_freq_list = []
for tag in tag_dict:
	freq = tag_dict[tag]
	output_string = tag + "|" + str(freq) + "\n"  
	output_file_desc.write(output_string)
	tag_freq_list.append((freq,tag))
output_file_desc.close()
logging.info("Writing to tagfreq.in Ended.")

logging.info("Extracting 1000 most frequent tags Started.")
most_tag_freq_list = heapq.nlargest(1000,tag_freq_list)
logging.info("Extracting 1000 most frequent tags Started.")

logging.info("Writing to 1000_tagfreq.in Started.")
output_file_desc = open("1000_tagfreq.in",'w')
for tup in most_tag_freq_list:
	output_string = tup[1] + "|" + str(tup[0]) + "\n"  
	output_file_desc.write(output_string)
output_file_desc.close()
logging.info("Writing to 1000_tagfreq.in Started.")