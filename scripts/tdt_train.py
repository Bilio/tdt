__author__ = 'Vibha Bhambhani and Shakshi Maheswari'
import pickle
import os
import math
from fileReader import FileReader
from config import TDT_DEV_DIR
from config import MODEL_FILE

def tokenizeAndTopicVectorCreation(fileObj, T, tfRaw):
    fileContent = FileReader(fileObj).content
    words = fileContent.strip().split()
    length = len(words)
    T.extend(words)
    DVector = set()
    for word in words:
        DVector.add(word)
        if word not in tfRaw:
            tfRaw[word] = 1
        else:
            tfRaw[word] += 1
    return DVector, length


def tokenizeAndDocumentVectorCreation(filfileObjeoutput, tfRawD):
    fileContent = FileReader(fileObj).content
    words = fileContent.strip().split()
    length = len(words)
    uniqueWordsInDoc = set()
    for word in words:
        uniqueWordsInDoc.add(word)
        if word not in tfRawD:
            tfRawD[word] = 1
        else:
            tfRawD[word] += 1
    for i in tfRawD:
        tfRawD[i] = float(tfRawD[i]) / length
    return uniqueWordsInDoc, words, length, tfRawD


def extractVocab(V, DVector):
    while DVector.__len__() != 0:
        x = DVector.pop()
        if x in V:
            V[x] = V[x] + 1
        else:
            V[x] = 1
    return V


def calcluatetfD(tfRawD, lenD, lenAvg):
    tfD = {}
    for i in tfRawD:
        tfD[i] = float(tfRawD[i]) / (tfRawD[i] + 0.5 + 1.5 * (lenD / lenAvg))
    return tfD


def calculatetfT(tfRaw, length, lenAvg):
    tfT = {}
    for i in tfRaw:
        tfT[i] = float(tfRaw[i]) / (tfRaw[i] + 0.5 + 1.5 * (length / lenAvg))
    return tfT


def calculateidf(V, N):
    idf = {}
    for word in V:
        if (1.0 * N / V[word]) == 1.0:
            Num = (1.0 * N / V[word]) - 0.0001
        else:
            Num = (1.0 * N / V[word])
        idf[word] = math.log(Num, 10) / math.log((N + 1), 10)
    return idf


def CalcProductDoc(tfD, idf):
    Dh = {}
    for word in tfD:
        Dh[word] = tfD[word] * idf[word]
    return Dh


def CalcProductTopic(tfT, idf):
    Th = {}
    for word in tfT:
        Th[word] = tfT[word] * idf[word]
    return Th


def similarity(Dh, Th):
    Dh_Th = 0
    DhSquared = 0
    ThSquared = 0
    for word in V:
        if word in Dh:
            Dvalue = Dh[word]
        else:
            Dvalue = 0
        if word in Th:
            Tvalue = Th[word]
        else:
            Tvalue = 0
        Dh_Th += 1.0 * Dvalue * Tvalue
        DhSquared += 1.0 * Dvalue * Dvalue
        ThSquared += 1.0 * Tvalue * Tvalue
    cosineDeno = math.sqrt(DhSquared * ThSquared)
    similarity = float(Dh_Th) / cosineDeno * 1.0
    return similarity

if __name__ == '__main__':
    # Define folder for topic outputs
    topicsFile = open(MODEL_FILE, 'wb')

    # Read a folder containing 4 documents of the topic
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
        for document in docsList:
            DVector = {}
            fileObj = open(os.path.join(topicPath, document), 'r')
            uniqueWordsInDoc, wordCount = tokenizeAndTopicVectorCreation(fileObj, T, tfRaw)
            topicWordCount += wordCount
            V = extractVocab(V, uniqueWordsInDoc)
        avgLength = topicWordCount
        N = 1
        for i in tfRaw:
            tfRaw[i] = float(tfRaw[i]) / topicWordCount
        topicInfo = {'topic': topic,
                                   'T': T,
                                   'V': V,
                                   'lenAvg': avgLength,
                                   'N': N,
                                   'tfRaw': tfRaw,
                                   'length': topicWordCount,
                                   }
        dictionaryOfTopics.append(topicInfo)
        similarityValueSum = 0
        similarityValue = 0
        for document in docsList:
            tfRawD = {}
            fileObj = open(os.path.join(topicPath, document), "r")
            uniqueWordsInDoc, DVector, lenD, tfRawD = tokenizeAndDocumentVectorCreation(fileObj, tfRawD)
            tfD = {}
            tfD = calcluatetfD(tfRawD, lenD, topicInfo['lenAvg'])

            # Calculated tfT --- tf of Topic
            tfT = {}
            tfT = calculatetfT(topicInfo['tfRaw'], topicInfo['length'], topicInfo['lenAvg'])

            # update idf statistics
            idf = {}
            idf = calculateidf(V, N)

            # tf.idf for document
            Dh = {}
            Dh = CalcProductDoc(tfD, idf)

            # tf.idf for topic
            Th = {}
            Th = CalcProductTopic(tfT, idf)

            # Step3: Story similarity computation
            similarityValue = similarity(Dh, Th)
            similarityValueSum += similarityValue

        similarityValueSum /= topicInfo['N']
        topicInfo['Z'] = similarityValueSum

    pickle.dump(dictionaryOfTopics, topicsFile)

