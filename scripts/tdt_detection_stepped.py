import os
from evaluation.config import TDT_TEST_DIR
from evaluation.config import TDT_DET_EVAL_FILE
import tdt_utils
import csv
import sys

theta = 0.04
docClusterDict = {}
clusterDocDict = {}
tfidf = {}

clusterNo = 0
avgLength = 0
N = 0
V={}

docs = filter(lambda x: not x.startswith('.') and os.path.isfile(os.path.join(TDT_TEST_DIR, x)),
              os.listdir(TDT_TEST_DIR))

doc = docs[0]
docOpen = open(os.path.join(TDT_TEST_DIR, doc), "r")
tfRawD = {}
uniqueWordsInDoc, DVector, lenD, tfRawD = tdt_utils.createDocumentVector(docOpen, tfRawD)
N = 1
tdt_utils.extractVocabulary(V, uniqueWordsInDoc)
avgLength = tdt_utils.updateAvgLength(avgLength, lenD, N - 1)
tfD = tdt_utils.calculateTF(tfRawD, lenD, avgLength)
idf = tdt_utils.calculateIdf(V, N)
tfidf[doc] = tdt_utils.calculateProduct(tfD, idf)
docClusterDict[doc]=0
clusterDocDict[0]=[doc]
count = len(docs)

for doc in docs[1:]:
    docOpen = open(os.path.join(TDT_TEST_DIR, doc), "r")
    tfRawD = {}
    uniqueWordsInDoc, DVector, lenD, tfRawD = tdt_utils.createDocumentVector(docOpen, tfRawD)
    N += 1
    tdt_utils.extractVocabulary(V, uniqueWordsInDoc)
    avgLength= tdt_utils.updateAvgLength(avgLength, lenD, N - 1)
    tfD = tdt_utils.calculateTF(tfRawD, lenD, avgLength)
    idf = tdt_utils.calculateIdf(V, N)
    Dh = tdt_utils.calculateProduct(tfD, idf)
    max_similarity = 0
    for t in tfidf:
        Th = tfidf[t]
        similarityValue = tdt_utils.similarity(Dh, Th, V)
        if similarityValue > max_similarity:
            max_similarity = similarityValue
            document = t
    if max_similarity > theta:
        docClusterDict[doc] = docClusterDict[document]
        clusterDocDict[docClusterDict[document]].append(doc)
    else:
        clusterNo += 1
        docClusterDict[doc] = clusterNo
        clusterDocDict[clusterNo] = [doc]
    tfidf[doc] = Dh
    sys.stdout.write("\rTopic Detection in Progress:\t%d%%" % (N*100/count))
    sys.stdout.flush()

outputCsv = open(TDT_DET_EVAL_FILE, 'wb')
writer = csv.DictWriter(outputCsv, fieldnames=['Cluster %d'%(x) for x in range(1, clusterNo + 2)])
clusterDocs = [clusterDocDict[i] for i in range(0, clusterNo+1)]
lengths = map(lambda x: len(x), clusterDocs)
maxLength = max(lengths)
newClusterDocs = []
for clusterDoc, length in zip(clusterDocs, lengths):
    diff = maxLength - length
    temp = clusterDoc + [' '] * diff
    newClusterDocs.append(temp)

writer.writeheader()
for i in range(0, maxLength):
    temp = {}
    for j in range(0, clusterNo+1):
        temp['Cluster %d'%(j+1)] = newClusterDocs[j][i]
    writer.writerow(temp)
print 'Topic Detection Complete.'