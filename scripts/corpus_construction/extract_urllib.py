import urllib2
from bs4 import BeautifulSoup
from get_urllist import elections_urllist

count = 0
for url in elections_urllist:
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    heading = filter(lambda y: y['id']==u'ContentPlaceHolder1_ArticleDetailHeading', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
    description = filter(lambda y: y['id']==u'ContentPlaceHolder1_ArticleDescription', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
    if heading != [] and description != []:
        file_name = "news%d"%(count)
        count += 1
        print count
        f = open('../../data/tdt_corpus/TamilNadu State Elections/%s.txt'%(file_name), 'w')
        f.write('<news>\n');
        f.write('<headline>');
        f.write(heading[0].text.encode('utf-8').strip())
        f.write('</headline>\n');
        f.write('<description>\n');
        f.write(description[0].text.encode('utf-8').strip())
        f.write('</description>\n');
        f.write('</news>\n');
        f.close()
