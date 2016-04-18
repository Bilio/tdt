from xml.dom.minidom import parse


class FileReader(object):
    def __init__(self, fileObj):
        self.content = ''
        try:
            DOMTree = parse(fileObj)
            news = DOMTree.documentElement
            self.content += news.getElementsByTagName('headline')[0].childNodes[0].data
            self.content += '\n'
            self.content += news.getElementsByTagName('description')[0].childNodes[0].data
        except:
            raise RuntimeError('Error in parsing file: "%s"' % (fileObj.name))

if __name__ == '__main__':
    import os
    from config import TDT_DEV_DIR
    topic = filter(lambda x: not x.startswith('.'), os.listdir(TDT_DEV_DIR))[0]
    topicPath = os.path.join(TDT_DEV_DIR, topic)
    doc = filter(lambda x: not x.startswith('.') and os.path.isfile(os.path.join(topicPath, x)),
                      os.listdir(topicPath))[0]
    fileReader = FileReader(open(os.path.join(topicPath, doc), 'r'))
