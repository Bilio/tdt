from __future__ import division

import popen2
from math import log10
from math import sqrt
from fileReader import FileReader

stemmer = './snowball/stemwords'

stemmed_words = {}

stopwords = map(lambda x: x.strip(), open('stopwords.txt', 'r').read().strip().split('\n'))

def stemWord(str):
    if str in stemmed_words:
        return stemmed_words[str]
    fin, fout = popen2.popen2(stemmer + " -l ta")
    fout.write(str)
    fout.write("\n")
    fout.close()
    res = fin.readlines()
    fin.close()
    if not res:
        stemmed_words[str] = str
        return str
    stemmed_words[str] = res[0]
    return res[0]

def modify_word(str):
    if str.strip() == '':
        return None
    if str.endswith('.'):
        str = str[:-1]
    return stemWord(str)
    # return str

def createTopicVector(fileObj, T, tfRaw):
    fileContent = FileReader(fileObj).content
    fileContent = ''.join(map(lambda x: ' ' if x != '.' and ord(x) < 48 or 57 < ord(x) < 65 else x, list(fileContent)))
    words = fileContent.strip().split()
    length = len(words)
    DVector = set()
    T.extend(words)
    for word in words:
        word = modify_word(word)
        if word:
            DVector.add(word)
            if word not in tfRaw:
                tfRaw[word] = 1
            else:
                tfRaw[word] += 1
    return DVector, length


def createDocumentVector(fileObj, tfRawD):
    fileContent = FileReader(fileObj).content
    fileContent = ''.join(map(lambda x: ' ' if x != '.' and ord(x) < 48 or 57 < ord(x) < 65 else x, list(fileContent)))
    words = fileContent.strip().split()
    length = len(words)
    uniqueWordsInDoc = set()
    for word in words:
        word = modify_word(word)
        if word:
            uniqueWordsInDoc.add(word)
            if word not in tfRawD:
                tfRawD[word] = 1
            else:
                tfRawD[word] += 1
    #for word in tfRawD:
        #tfRawD[word] /= length
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
        if (N / V[word]) == 1.0:
            Num = 1.0001
        else:
            Num = (N / V[word])
        idf[word] = log10(Num) / log10(N + 1)
        if idf[word] < 0: print idf[word], Num
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
        DhSquared += Dvalue * Dvalue
        ThSquared += Tvalue * Tvalue
    cosineDeno = sqrt(DhSquared * ThSquared)
    return Dh_Th / cosineDeno


def updateAvgLength(lenAvg, length, N):
    return (lenAvg * N + length) / (N + 1)
