import csv

thetha = 0.5
with open('/media/sharanyavraju/Windows/USC/Applied Natural Language Processing/Final Project/Topic Detection/evaluationdata/System_ArticleTopicClassification.csv', 'rb') as f:
    freader = iter(csv.reader(f, delimiter = ','))
    with open('/media/sharanyavraju/Windows/USC/Applied Natural Language Processing/Final Project/Topic Detection/evaluationdata/Systemoutput.csv', 'wb') as sysoutput:
        sysoutputwriter = csv.writer(sysoutput, delimiter = ',')
        sysoutputwriter.writerow(next(freader))
        for row in freader:
            inputrow = [row[0]]
            for val in row[1:]:
                # print val
                if float(val) > thetha:
                    inputrow.append(1)
                else:
                    inputrow.append(0)
            sysoutputwriter.writerow(inputrow)

fa = 0
ms = 0
nocount = 0
yescount =0


with open('/media/sharanyavraju/Windows/USC/Applied Natural Language Processing/Final Project/Topic Detection/evaluationdata/Systemoutput.csv', 'rb') as sysoutput:
    with open('/media/sharanyavraju/Windows/USC/Applied Natural Language Processing/Final Project/Topic Detection/evaluationdata/HumanAnnotatedoutput.csv', 'rb') as humanoutput:
        sysoutputreader = iter(csv.reader(sysoutput, delimiter=','))
        humanoutputreader = iter(csv.reader(humanoutput, delimiter=','))
        next(sysoutputreader)
        next(humanoutputreader)
        for sysrow, humanrow in zip(sysoutputreader, humanoutputreader):
            for s, h in zip(sysrow, humanrow):
                if h == '0':
                    nocount += 1
                    if s == '1':
                        fa += 1
                elif h == '1':
                    yescount += 1
                    if s == '0':
                        ms += 1
print "False Alarm proportion: "+str(float(fa)/float(nocount))
print "Miss poportion is: "+str(float(ms)/float(yescount))
