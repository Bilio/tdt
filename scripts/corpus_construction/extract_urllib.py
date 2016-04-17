import urllib2
from bs4 import BeautifulSoup
from get_urllist import elections_urllist
from get_urllist import tennis_urllist
from get_urllist import hockey_urllist
from get_urllist import da_urllist
from get_urllist import business_urllist
from get_urllist import vehicle_urllist
from get_urllist import ciff_urllist
from get_urllist import c_floods_urllist

count = 0
for url in elections_urllist:
    try:
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
    except:
        pass

count = 0
for url in tennis_urllist:
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        heading = filter(lambda y: y['id']==u'ContentPlaceHolder1_ArticleDetailHeading', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        description = filter(lambda y: y['id']==u'ContentPlaceHolder1_ArticleDescription', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        if heading != [] and description != []:
            file_name = "news%d"%(count)
            count += 1
            print count
            f = open('../../data/tdt_corpus/Tennis Events/%s.txt'%(file_name), 'w')
            f.write('<news>\n');
            f.write('<headline>');
            f.write(heading[0].text.encode('utf-8').strip())
            f.write('</headline>\n');
            f.write('<description>\n');
            f.write(description[0].text.encode('utf-8').strip())
            f.write('</description>\n');
            f.write('</news>\n');
            f.close()
    except:
        pass

count = 0
for url in hockey_urllist:
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        heading = filter(lambda y: y['id']==u'ContentPlaceHolder1_ArticleDetailHeading', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        description = filter(lambda y: y['id']==u'ContentPlaceHolder1_ArticleDescription', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        if heading != [] and description != []:
            file_name = "news%d"%(count)
            count += 1
            print count
            f = open('../../data/tdt_corpus/Hockey Events/%s.txt'%(file_name), 'w')
            f.write('<news>\n');
            f.write('<headline>');
            f.write(heading[0].text.encode('utf-8').strip())
            f.write('</headline>\n');
            f.write('<description>\n');
            f.write(description[0].text.encode('utf-8').strip())
            f.write('</description>\n');
            f.write('</news>\n');
            f.close()
    except:
        pass

count = 0
for url in da_urllist:
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        heading = filter(lambda y: y['id']==u'ContentPlaceHolder1_ArticleDetailHeading', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        description = filter(lambda y: y['id']==u'ContentPlaceHolder1_ArticleDescription', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        if heading != [] and description != []:
            file_name = "news%d"%(count)
            count += 1
            print count
            f = open('../../data/tdt_corpus/Disasters and Accidents/%s.txt'%(file_name), 'w')
            f.write('<news>\n');
            f.write('<headline>');
            f.write(heading[0].text.encode('utf-8').strip())
            f.write('</headline>\n');
            f.write('<description>\n');
            f.write(description[0].text.encode('utf-8').strip())
            f.write('</description>\n');
            f.write('</news>\n');
            f.close()
    except:
        pass

count = 0
for url in business_urllist:
    try:
        response = urllib2.urlopen(url.encode('utf-8'))
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        heading = filter(lambda y: u'detail-title' in y['class'], filter(lambda x: x.has_attr('class'), soup.find_all('h1')))
        description = filter(lambda y: u'article-body'in y['class'], filter(lambda x: x.has_attr('class'), soup.find_all('div')))
        if heading != [] and description != []:
            file_name = "news%d"%(count)
            count += 1
            print count
            f = open('../../data/tdt_corpus/Business Events/%s.txt'%(file_name), 'w')
            f.write('<news>\n');
            f.write('<headline>');
            f.write(heading[0].text.encode('utf-8').strip())
            f.write('</headline>\n');
            f.write('<description>\n');
            f.write('\n'.join(map(lambda x: x.text.encode('utf-8'), description[0].find_all('p'))))
            f.write('</description>\n');
            f.write('</news>\n');
            f.close()
    except:
        pass

count = 0
for url in vehicle_urllist:
    try:
        response = urllib2.urlopen(url.encode('utf-8'))
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        heading = filter(lambda y: u'detail-title' in y['class'], filter(lambda x: x.has_attr('class'), soup.find_all('h1')))
        description = filter(lambda y: u'article-body'in y['class'], filter(lambda x: x.has_attr('class'), soup.find_all('div')))
        if heading != [] and description != []:
            file_name = "news%d"%(count)
            count += 1
            print count
            f = open('../../data/tdt_corpus/Vehicle World/%s.txt'%(file_name), 'w')
            f.write('<news>\n');
            f.write('<headline>');
            f.write(heading[0].text.encode('utf-8').strip())
            f.write('</headline>\n');
            f.write('<description>\n');
            f.write('\n'.join(map(lambda x: x.text.encode('utf-8'), description[0].find_all('p'))))
            f.write('</description>\n');
            f.write('</news>\n');
            f.close()
    except:
        pass

count = 0

count = 0
for url in ciff_urllist:
    try:
        response = urllib2.urlopen(url.encode('utf-8'))
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        heading = filter(lambda y: u'articleTitle' == y['id'], filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        description = filter(lambda y: u'articlebody'== y['id'], filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        if heading != [] and description != []:
            file_name = "news%d"%(count)
            count += 1
            f = open('../../data/tdt_corpus/Chennai International Film Festival/%s.txt'%(file_name), 'w')
            f.write('<news>\n');
            f.write('<headline>');
            f.write(heading[0].h1.text.encode('utf-8').strip())
            f.write('</headline>\n');
            f.write('<description>\n');
            f.write(description[0].p.text.encode('utf-8'))
            f.write('</description>\n');
            f.write('</news>\n');
            f.close()
    except:
        pass

count = 0
for url in c_floods_urllist:
    try:
        response = urllib2.urlopen(url.encode('utf-8'))
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        heading = filter(lambda y: u'articleTitle' == y['id'], filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        description = filter(lambda y: u'articlebody'== y['id'], filter(lambda x: x.has_attr('id'), soup.find_all('div')))
        if heading != [] and description != []:
            file_name = "news%d"%(count)
            count += 1
            f = open('../../data/tdt_corpus/Chennai Floods/%s.txt'%(file_name), 'w')
            f.write('<news>\n');
            f.write('<headline>');
            f.write(heading[0].h1.text.encode('utf-8').strip())
            f.write('</headline>\n');
            f.write('<description>\n');
            f.write(description[0].p.text.encode('utf-8'))
            f.write('</description>\n');
            f.write('</news>\n');
            f.close()
    except:
        pass

