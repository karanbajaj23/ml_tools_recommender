import os
import re
from collections import Counter
from nltk.stem import WordNetLemmatizer

inp_h = open('fileList.txt', 'r')
out_h = open('outWordList.txt', 'w')

wordList = list()
wnl = WordNetLemmatizer()

def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

def record_word(word):
	if(len(word) > 2):
		word = word.lower()
		sword = wnl.lemmatize(word)
		wordList.append(sword)

for file in inp_h:
	(fileName, ext) = os.path.splitext(file)
	numberLess = ''.join([i for i in fileName if not i.isdigit()])
	words = re.split(' |_|-', numberLess)
	for word in words:
		if word:
			possibleWords = camel_case_split(word)
			if(len(possibleWords) > 0):
				for word in possibleWords:
					record_word(word)
			else:
				record_word(word)

wordFreq = Counter(wordList).most_common()

totalWords = len(wordFreq)
print(totalWords)

for word in wordFreq:
	out_h.write(str(word[1]) + '\t' +word[0]+'\n')