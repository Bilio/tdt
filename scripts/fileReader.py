import traceback

class FileReader(object):
    def __init__(self, fileObj):
        data = fileObj.read()
        data = data.replace('<news>','').replace('</news>','').replace('<headline>','').replace('</headline>','')
        data = data.replace('<description>','').replace('</description>','')
        self.content = data

if __name__ == '__main__':
    import os
    from config import TDT_DEV_DIR
    topic = filter(lambda x: not x.startswith('.'), os.listdir(TDT_DEV_DIR))[0]
    topicPath = os.path.join(TDT_DEV_DIR, topic)
    doc = filter(lambda x: not x.startswith('.') and os.path.isfile(os.path.join(topicPath, x)),
                      os.listdir(topicPath))[0]
    fileReader = FileReader(open(os.path.join(topicPath, doc), 'r'))
