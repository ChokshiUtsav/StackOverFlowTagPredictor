import sys
import matplotlib.pyplot as plt
import pandas

file_name = str(sys.argv[1])
file_desc = open(file_name,'r')

tag_dict={}
count=0
for line in file_desc.readlines():
	temp1 = line.split("|")
	freq = int(temp1[1])
	tag = str(temp1[0])
	tag_dict[tag] = freq
	count+=1
	if count==30 :
		break

df=pandas.DataFrame.from_dict(tag_dict,orient='index')
df.plot(kind='bar')
plt.ylabel("Cumulative frequency over all posts")
plt.title("Histogram of 30 most frequent tags")
plt.show()
