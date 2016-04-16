import os
import config
corpusInfo = {}
for dir in os.listdir(config.TDT_CORPUS_DIR):
    corpusInfo[dir] = []
    for doc in os.listdir(os.path.join(config.TDT_CORPUS_DIR, dir)):
        corpusInfo[dir].append(doc)

print corpusInfo
