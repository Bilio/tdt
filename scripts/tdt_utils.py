from __future__ import division
from math import log10
from math import sqrt
from fileReader import FileReader


def createTopicVector(fileObj, T, tfRaw):
    fileContent = FileReader(fileObj).content
    words = fileContent.strip().split()
    length = 0
    DVector = []
    for word in words:
        length += 1
        T.append(word)
        if word not in tfRaw:
            DVector.append(word)
            tfRaw[word] = 1
        else:
            tfRaw[word] += 1
    return DVector, length


def createDocumentVector(fileObj, tfRawD):
    fileContent = FileReader(fileObj).content
    words = fileContent.strip().split()
    length = 0
    uniqueWordsInDoc = []
    for word in words:
        length += 1
        if word not in tfRawD:
            uniqueWordsInDoc.append(word)
            tfRawD[word] = 1
        else:
            tfRawD[word] += 1
    for word in tfRawD:
        tfRawD[word] /= length
    return uniqueWordsInDoc, words, length, tfRawD


def extractVocabulary(Vocabulary, uniqueWordsInDoc):
    for word in uniqueWordsInDoc:
        if word in Vocabulary:
            Vocabulary[word] += 1
        else:
            Vocabulary[word] = 1


def calculateTF(tfRaw, length, avgLength):
    tf = {}
    for i in tfRaw:
        tf[i] = tfRaw[i] / (tfRaw[i] + 0.5 + 1.5 * (length / avgLength))
    return tf


def calculateIdf(V, N):
    idf = {}
    for word in V:
        if (1.0 * N / V[word]) == 1.0:
            Num = (1.0 * N / V[word]) - 0.0001
        else:
            Num = (1.0 * N / V[word])
        idf[word] = log10(Num) / log10(N + 1)
    return idf


def calculateProduct(tf, idf):
    result = {}
    for word in tf:
        result[word] = tf[word] * idf[word]
    return result


def similarity(Dh, Th, Vocabulary):
    Dh_Th = 0
    DhSquared = 0
    ThSquared = 0
    for word in Vocabulary:
        Dvalue = Dh.get(word, 0)
        Tvalue = Th.get(word, 0)
        Dh_Th += Dvalue * Tvalue
        DhSquared += Dvalue ** 2
        ThSquared += Tvalue ** 2
    cosineDeno = sqrt(DhSquared * ThSquared)
    return Dh_Th / cosineDeno

def updateAvgLength(lenAvg, length, N):
    return (lenAvg * N + length) / (N + 1)
