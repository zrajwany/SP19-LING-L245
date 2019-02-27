import sys

vocab = {}

#creates empty dictionary

hs = open('wiki.hist', 'r')
for line in hs.readlines():
	form = line.strip()
	row = form.split(' ')
	if len(row) > 1:
		vocab[row[1]] = int(row[0])
	

#opens file, removes spaces in beginning, adds new forms to vocab dictionary

freq = []
for word in vocab:
	freq.append((vocab[word],word))

#empty list, add every word in vocab dictionary, sorts by frequency

freq.sort(reverse=True)

rank = 1
min = freq[0][0]
ranks = []
for i in range(0,len(freq)):
	if freq[i][0] < min:
		rank += 1
		min = freq[i][0]
	ranks.append((rank, freq[i][0], freq[i][1]))


#goes through freq, sets mininum to the last lowest word

hs.close()
 
for i in ranks:
	print(i)
#print(sys.argv)
