import pickle
import os
'''
 For one topic do the following:
 1) represent the topic using the topic vector
 2) story-topic similarity computation
 3)tf-tdf scores computation
'''

#Step 1: TOPIC REPRESENTATION
def tokenizeAndTopicVectorCreation(fileoutput,T,tfRaw):
    words = fileoutput.split()
    length = len(words)
    T.extend(words)
    DVector = set()
    for word in words:
        DVector.add(word)
        if word not in tfRaw:
            tfRaw[word]=1
        else:
            tfRaw[word]+=1


    return DVector,T,length

def extractVocab(V,DVector):
 #print(DVector)
 while DVector.__len__()!=0:
  x = DVector.pop()
  if x in V:
   V[x] = V[x]+1
  else:
   V[x] = 1
 return V

#def dfUpdate(V,DVector):


topicsFolder = "/Users/vibhabhambhani/Desktop/NLP/Project/trainingData"

#Define folder for topic outputs
topicsFile=open("topics.txt","w")
#Read a folder containing 4 documents of the topic
listOfTopics = next(os.walk(topicsFolder))[1]
dictionaryOfTopics=[]
for topic in listOfTopics:
  T=[]
  tfRaw={}
  print(topic)
  z = os.path.join(topicsFolder,topic)
  docs=[]
  V={}
  for item in os.listdir(z):
   if not item.startswith('.') and os.path.isfile(os.path.join(z, item)):
        docs.append(os.path.join(z, item))
   uniqueWordsInDoc=set()
  lengthofdocs = 0

#For each document split by words
  for doc in docs:
     DVector = {}
     fileop = open(doc,"r")
     uniqueWordsInDoc,T,length= tokenizeAndTopicVectorCreation(fileop.read(),T,tfRaw)
     lengthofdocs = lengthofdocs+length
     V = extractVocab(V,uniqueWordsInDoc)
  #print("Topic Vector")
  #print T
  #print("Vocabulary")
  #print(V)
  print("Length")
  lenAvg=lengthofdocs/2
  N=2
  for i in tfRaw:
      tfRaw[i]=float(tfRaw[i])/lengthofdocs
  dictionaryOfTopics.append({'topic':topic,'T':T,'V':V,'lenAvg':lenAvg,'N':N,'tfRaw':tfRaw,'length':lengthofdocs})
print(dictionaryOfTopics)
pickle.dump(dictionaryOfTopics,topicsFile)


####append splitted-document to the topic vector
####create a vocabulary V which will contain a list of words and the
#### df of the words
####update N
####lenAvg documents

#Step2: TF-IDF SCORE COMPUTATION
#   tf =         tfRaw
#       ---------------------
#       tfRaw +0.5 +1.5 +  lenD
#                         ------
#                         lenAng
#take as input a folder path which contains documents to be classified

#for each document in the folder

#construct D vector

#TF SCORE COMPUTATION

#get the "lenD" length of the document value


#update the "lenAvg" the average length of document value (use N and lenAvg and lenD)

#get all the unique words in a set for D_raw

#get all the raw frequencies of the unique words found in D_raw and store them in a dictionary "tf_raw" which contains
## [term]:number of occurrences in document D

#calculate "tf" dictionary [terms]:modified values -- incorporating the length feature

#IDF SCORE COMPUTATION
#update idf statistics

#update the 'N' number of documents count

#update the vocabulary V which has document frequency in it. df --- for already existing words update the score ---- for new words add them to the vocabulary
##with the no.docs they appear in ---'V'dictionary [term]:no.of docs the term appears in---

#calculate 'idf' scores for all terms in 'D_raw' using 'V' and 'N'values

#Compute tf.idf


#apply tf.idf dictionary [term]:value weighting to D and T vectors --- 2 tf.idf dictionaries -- one for D and one for T

#Step3: Story similarity computation
#'Dh*Vh'=0
#'DhSquared'=0
#'VhSquared'=0
#for each 'h' in 'V' do
####'Dh*Vh'+='Dh'*'Vh' #where Dh = tf.idf for term h
####'DhSquared'+=squared('Dh')
####'VhSquared'+=squared('Vh')
#'cosineDeno'=sqrt('Dh'*'Vh')
#similarity(D,T)='Dh*Vh'/'cosineDeno'