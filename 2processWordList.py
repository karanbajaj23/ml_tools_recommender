from nltk.corpus import stopwords

inp_h = open('outWordList.txt', 'r')
out_h = open('finalWordList.txt', 'w')

stopWords = set(stopwords.words('english'))

totalFreq = 0
finalWords = list()

for wordLine in inp_h:
	wordList = wordLine.split()
	freq = wordList[0]
	word = wordList[1]
	if word not in stopWords:
		totalFreq += int(freq)
		finalWords.append(tuple([freq, word]))

for wordTup in finalWords:
	wordP = int(wordTup[0])/totalFreq*100
	if wordP > 0.01:
		out_h.write(str(wordP) + '\t' + wordTup[1] + '\n')
	else:
		break