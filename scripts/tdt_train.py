__author__ = 'Vibha Bhambhani and Shakshi Maheswari'
import pickle
import os
from config import TDT_DEV_DIR
from config import MODEL_FILE
import tdt_utils



topicsFile = open(MODEL_FILE, 'wb')

try:
    listOfTopics = filter(lambda x: not x.startswith('.'), os.listdir(TDT_DEV_DIR))
except:
    raise RuntimeError('The directory "%s" does not exist.' % TDT_DEV_DIR)

dictionaryOfTopics = []

for topic in listOfTopics:
    T = []
    tfRaw = {}
    V = {}
    topicPath = os.path.join(TDT_DEV_DIR, topic)
    docsList = filter(lambda x: not x.startswith('.') and os.path.isfile(os.path.join(topicPath, x)),
                      os.listdir(topicPath))
    uniqueWordsInDoc = None
    topicWordCount = 0

    N = len(docsList)
    for document in docsList:
        fileObj = open(os.path.join(topicPath, document), 'r')
        uniqueWordsInDoc, wordCount = tdt_utils.createTopicVector(fileObj, T, tfRaw)
        topicWordCount += wordCount
        tdt_utils.extractVocabulary(V, uniqueWordsInDoc)

    avgLength = topicWordCount / N

    for i in tfRaw:
        tfRaw[i] = float(tfRaw[i]) / topicWordCount
    topicInfo = dict(topic=topic, T=T, V=V, avgLength=avgLength, N=N, tfRaw=tfRaw, length=topicWordCount)
    dictionaryOfTopics.append(topicInfo)
    similarityValueSum = 0
    similarityValue = 0

    for document in docsList:
        fileObj = open(os.path.join(topicPath, document), "r")
        tfRawD = {}
        uniqueWordsInDoc, DVector, lenD, tfRawD = tdt_utils.createDocumentVector(fileObj, tfRawD)
        tfD = tdt_utils.calculateTF(tfRawD, lenD, avgLength)
        tfT = tdt_utils.calculateTF(tfRaw, topicWordCount, avgLength)
        idf = tdt_utils.calculateIdf(V, N)
        Dh = tdt_utils.calculateProduct(tfD, idf)
        Th = tdt_utils.calculateProduct(tfT, idf)
        similarityValue = tdt_utils.similarity(Dh, Th, V)
        similarityValueSum += similarityValue

    similarityValueSum /= N
    topicInfo['Z'] = similarityValueSum

pickle.dump(dictionaryOfTopics, topicsFile)
