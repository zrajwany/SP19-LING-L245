import sys

vocab = []

#creates empty list

hs = open('wiki.hist', 'r')
for line in hs.readlines():
	form = line.strip()
	row = form.split(' ')
	if len(row) > 1:
		vocab.append(row[1])


	
for line in sys.stdin.readlines():
	lines = line.split(" ")
	for x in lines:
		if x in vocab:
			print(x)
		else:
			print ("*" + x)




hs.close()
 







#for i in ranks:
	#print(i)