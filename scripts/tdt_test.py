from __future__ import division
import shutil
import os
import pickle
from evaluation.config import MODEL_FILE
from evaluation.config import TDT_OUT_DIR
from evaluation.config import TDT_TEST_DIR
from evaluation.config import LOG_FOLDER
from evaluation.config import TDT_TEST_OUT_FILE
import tdt_utils
import csv
import sys

outputCsv = open(TDT_TEST_OUT_FILE,'wb')
fieldnames = ['Filename']

root = TDT_OUT_DIR
topics = pickle.load(open(MODEL_FILE, "rb"))
logger = open(os.path.join(LOG_FOLDER, 'output.txt'), 'w')
docs = filter(lambda x: not x.startswith('.') and os.path.isfile(os.path.join(TDT_TEST_DIR, x)),
              os.listdir(TDT_TEST_DIR))

for topic in topics:
    dir_path = os.path.join(root, topic['topic'])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    fieldnames.append(topic['topic'])

writer = csv.DictWriter(outputCsv, fieldnames=fieldnames)
writer.writeheader()
count = len(docs)

i = 1
for doc in docs:
    results = []
    logger.write('DOC NAME: %s\n'%(os.path.join(TDT_TEST_DIR, doc)))
    docOpen = open(os.path.join(TDT_TEST_DIR, doc), "r")
    tfRawD = {}
    uniqueWordsInDoc, DVector, lenD, tfRawD = tdt_utils.createDocumentVector(docOpen, tfRawD)
    similarityWIthTopics = {"Filename": doc}
    for topic in topics:
        V = topic['V']
        N = topic['N'] + 1
        tdt_utils.extractVocabulary(V, uniqueWordsInDoc)
        avgLength = tdt_utils.updateAvgLength(topic['avgLength'], lenD, N - 1)
        tfD = tdt_utils.calculateTF(tfRawD, lenD, avgLength)
        tfT = tdt_utils.calculateTF(topic['tfRaw'], topic['length'], avgLength)
        idf = tdt_utils.calculateIdf(V, N)
        topic['V']=dict(V)
        Dh = tdt_utils.calculateProduct(tfD, idf)
        Th = tdt_utils.calculateProduct(tfT, idf)
        similarityValue = tdt_utils.similarity(Dh, Th, V)
        normalizedValue = similarityValue / topic['Z']
        results.append([topic['topic'], normalizedValue])
        similarityWIthTopics[topic['topic']] = str(normalizedValue)

    writer.writerow(similarityWIthTopics)
    results = sorted(results, key=lambda x: x[1], reverse=True)
    logger.write('\n'.join(map(lambda x: '%s==%s'%(x[0], x[1]), results)))
    logger.write('\n')
    shutil.copyfile(os.path.join(TDT_TEST_DIR, doc), os.path.join(TDT_OUT_DIR, results[0][0], doc))
    logger.write('--------------------------------------------\n')
    sys.stdout.write("\rTopic Tracking in Progress:\t%d%%" % (i*100/count))
    sys.stdout.flush()
    i += 1

