
__author__ = 'Vibha Bhambhani and Shakshi Maheswari'
import os
from config import TDT_OUT_DIR
from config import TDT_TEST_DIR
import tdt_utils
import csv

theta = 0.04
#create a dictionary which will store document name and the cluster that they are assigned too
docClusterDict={}
clusterDocDict={}
tfidf={}

#initalize name to clusterno=0
clusterNo=0
#inialize avg length
avgLength = 0
N = 0
V={}


#read all docs
docs = filter(lambda x: not x.startswith('.') and os.path.isfile(os.path.join(TDT_TEST_DIR, x)),
              os.listdir(TDT_TEST_DIR))


doc = docs[0]
docOpen = open(os.path.join(TDT_TEST_DIR, doc), "r")
tfRawD = {}
uniqueWordsInDoc, DVector, lenD, tfRawD = tdt_utils.createDocumentVector(docOpen, tfRawD)
N=1
tdt_utils.extractVocabulary(V, uniqueWordsInDoc)
avgLength = tdt_utils.updateAvgLength(avgLength, lenD, N - 1)
tfD = tdt_utils.calculateTF(tfRawD, lenD, avgLength)
idf = tdt_utils.calculateIdf(V, N)
tfidf[doc] = tdt_utils.calculateProduct(tfD, idf)
docClusterDict[doc]=0
clusterDocDict[0]=[doc]

#for each subsequent document Dk>1 in the stream
count =0
for doc in docs[1:]:

    docOpen = open(os.path.join(TDT_TEST_DIR, doc), "r")
    tfRawD = {}
    uniqueWordsInDoc, DVector, lenD, tfRawD = tdt_utils.createDocumentVector(docOpen, tfRawD)
    N=N+1
    tdt_utils.extractVocabulary(V, uniqueWordsInDoc)
    avgLength= tdt_utils.updateAvgLength(avgLength, lenD, N - 1)
    tfD = tdt_utils.calculateTF(tfRawD, lenD, avgLength)
    idf = tdt_utils.calculateIdf(V, N)
    Dh = tdt_utils.calculateProduct(tfD, idf)
    max=0
    for t in tfidf:
        Th = tfidf[t]
        similarityValue = tdt_utils.similarity(Dh, Th, V)
        #print(similarityValue)
        #print("\n")
        if similarityValue>max:
            max=similarityValue
            document=t
    if max>theta:
        docClusterDict[doc]=docClusterDict[document]
        clusterDocDict[docClusterDict[document]].append(doc)
    else:
        clusterNo=clusterNo+1
        docClusterDict[doc]=clusterNo
        clusterDocDict[clusterNo]=[doc]
    tfidf[doc]=Dh
    print(docClusterDict[doc])
    print(similarityValue)
    count+=1
    print count
print(docClusterDict)
print(clusterDocDict)
    ### use Df to update idf (V) statistics
    ### apply tf*idf to document Dk
    ### store the Dk documents tf*idf to dictionary of tfidf scores
    ### find the most similar story from the past
    ### D' = arg max j  sim(Dk,Dj)
    ### if similarity between Dk and D' i..e.. sim(D',Dk)<theta
    ###### create a new cluster containing just Dk
    ###### write the cluster-number against Dk or add that to the dictionary
    ### else add Dk to the cluster containing D'