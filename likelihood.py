import sys
import logging

primary_file_name = str(sys.argv[1])
secondary_file_name = str(sys.argv[2])
tagfreq_file_name = str(sys.argv[3])
primary_file_desc = open(primary_file_name,'r')
secondary_file_desc = open(secondary_file_name,'r')
tagfreq_file_desc = open(tagfreq_file_name,'r')
output_file_desc = open("likelihood.in",'w')
logging.basicConfig(filename='likelihood.log',level=logging.DEBUG)

logging.info("Tag Index Processing Started.")
tag_dict = {}
for line in tagfreq_file_desc.readlines():
	temp = line.split("|")
	tag = str(temp[0])
	freq = int(temp[1])
	tag_dict[tag] = freq
logging.info("Tag Index Processing ended.")

logging.info("Writing to likelihood.in Started.")
count=0
for line in secondary_file_desc.readlines():
	temp = line.strip().split(":")
	word = str(temp[0])
	offset = int(temp[1].split(";")[0])
	primary_file_desc.seek(offset)
	temp = primary_file_desc.readline().split(";")
	for tag_freq_pair in temp:
		tag = str(tag_freq_pair.split("|")[0])
		freq = int(tag_freq_pair.split("|")[1])
		if tag in tag_dict:
			likelihood = float(freq)/tag_dict[tag]
			output_string = word + ";" + tag + "|" + str(likelihood) + "\n"
			output_file_desc.write(output_string)
			count+=1
logging.info("Number of word;tag pairs : " + str(count))
logging.info("Writing to likelihood.in ended.")