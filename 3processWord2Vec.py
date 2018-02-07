from gensim.models.keyedvectors import KeyedVectors
from sklearn.cluster import KMeans
import numpy as np
import csv

inp_h = open('finalWordList.txt', 'r')

model = KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

bigArray = []
csvfile = open('finalWordVec.csv', 'w')
vecFile = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

for wordLine in inp_h:
	wordList = wordLine.split()
	word = wordList[1]
	try:
		vec = model[word]
		if (vec.size > 0):
			vecFile.writerow([word]+vec.tolist())
			bigArray.append(vec)			
	except:
		print('Couldn\'t process '+word+'\n')