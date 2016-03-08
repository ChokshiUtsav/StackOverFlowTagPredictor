import sys
import logging

file_name = str(sys.argv[1])
input_file_desc = open(file_name,'r')
logging.basicConfig(filename='prior.log',level=logging.DEBUG)

logging.info("------------------------------------")

logging.info("Tag Index Processing Started.")
count = 0
total_freq = 0.0
for line in input_file_desc.readlines():
	temp = line.split("|")
	freq = int(temp[1])
	total_freq += freq
	logging.info("line #"+str(count)+" has been processed")
	count+=1
input_file_desc.close()
logging.info("Total Frequency : " + str(total_freq))
logging.info("Tag Index Processing Ended.")

logging.info("Writing to prior.in Started.")
input_file_desc = open(file_name,'r')
output_file_desc = open("prior.in",'w')
count = 0
for line in input_file_desc.readlines():
	temp = line.split("|")
	tag = str(temp[0])
	freq = int(temp[1])
	prior = float(freq)/total_freq
	output_string = tag + "|" + str(prior) + "\n"
	output_file_desc.write(output_string)  
	logging.info("line #"+str(count)+" has been processed")
	count+=1
input_file_desc.close()
output_file_desc.close()
logging.info("Writing to prior.in Ended.")