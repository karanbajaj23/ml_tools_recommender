from sklearn.cluster import KMeans
import numpy as np
import csv

csvfile = open('finalWordVec.csv', 'r')
vecFile = csv.reader(csvfile, delimiter=' ', quotechar='|')
out_h = open('finalVecClusters.txt', 'w')

bigArray = []

words = []

for vecLine in vecFile:
	words.append(vecLine[0])
	vec = vecLine[1:]
	npVec = np.array(vec)
	bigArray.append(npVec)

X = np.array(bigArray)
kmeans = KMeans(n_clusters=15, random_state=0).fit(X)

labels = kmeans.labels_
groups = dict()
for i in range(0, len(words)-1):
	label = labels[i]
	if label not in groups:
		groups[label] = list()
	groups[label].append(words[i])

for key in groups:
	out_h.write(str(key) + '\n')
	for word in groups[key]:
		out_h.write(word + '\t')
	out_h.write('\n')