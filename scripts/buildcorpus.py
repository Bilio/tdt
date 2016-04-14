from bs4 import BeautifulSoup
import os

file_list = os.listdir('../data/raw/the_hindu/cinema/')
count = len(file_list)
for file_name in file_list:
    print '%s more files..'%(count)
    count -= 1
    soup = BeautifulSoup(open('../data/raw/the_hindu/cinema/' + file_name), 'html.parser')
    heading = filter(lambda y: y['class']==[u'detail-title'], filter(lambda x: x.has_attr('class'), soup.find_all('h1')))
    description = filter(lambda y: y['class']==[u'body'], filter(lambda x: x.has_attr('class'), soup.find_all('p')))
    if heading != [] and description != []:
        f = open('../data/corpus/the_hindu/cinema/%s.txt'%(file_name.split('.htm')[0]), 'w')
        f.write('<news>\n');
        f.write('<headline>');
        f.write(heading[0].text.encode('utf-8').strip())
        f.write('</headline>\n');
        f.write('<description>\n');
        f.write(description[0].text.encode('utf-8').strip())
        f.write('</description>\n');
        f.write('</news>\n');
        f.close()

# file_list = os.listdir('../data/raw/the_hindu/sports/')
# count = len(file_list)
# for file_name in file_list:
#     print '%s more files..'%(count)
#     count -= 1
#     soup = BeautifulSoup(open('../data/raw/the_hindu/sports/' + file_name), 'html.parser')
#     heading = filter(lambda y: y['class']==[u'detail-title'], filter(lambda x: x.has_attr('class'), soup.find_all('h1')))
#     description = filter(lambda y: y['class']==[u'body'], filter(lambda x: x.has_attr('class'), soup.find_all('p')))
#     if heading != [] and description != []:
#         f = open('../data/corpus/the_hindu/sports/%s.txt'%(file_name.split('.htm')[0]), 'w')
#         f.write('<news>\n');
#         f.write('<headline>');
#         f.write(heading[0].text.encode('utf-8').strip())
#         f.write('</headline>\n');
#         f.write('<description>\n');
#         f.write(description[0].text.encode('utf-8').strip())
#         f.write('</description>\n');
#         f.write('</news>\n');
#         f.close()
#
# file_list = os.listdir('../data/raw/dinamalar/cinema/')
# count = len(file_list)
# for file_name in file_list:
#     print '%s more files..'%(count)
#     count -= 1
#     soup = BeautifulSoup(open('../data/raw/dinamalar/cinema/' + file_name), 'html.parser')
#     # import pdb; pdb.set_trace()
#     heading = filter(lambda y: y['id']==u'selContentdet', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
#     if heading != [] and heading[0].h2:
#         f = open('../data/corpus/dinamalar/cinema/%s.txt'%(file_name.split('.htm')[0]), 'w')
#         f.write('<news>\n');
#         f.write('<headline>');
#         f.write(heading[0].h2.text.encode('utf-8').strip())
#         f.write('</headline>\n');
#         f.write('<description>\n');
#         f.write(''.join(map(lambda x: x.text.encode('utf-8'), heading[0].find_all('p'))))
#         f.write('</description>\n');
#         f.write('</news>\n');
#         f.close()
#
# file_list = os.listdir('../data/raw/dinamalar/sports/')
# count = len(file_list)
# for file_name in file_list:
#     print '%s more files..'%(count)
#     count -= 1
#     soup = BeautifulSoup(open('../data/raw/dinamalar/sports/' + file_name), 'html.parser')
#     # import pdb; pdb.set_trace()
#     heading = filter(lambda y: y['class']==[u'review-contain'], filter(lambda x: x.has_attr('class'), soup.find_all('div')))
#     description = filter(lambda y: y['id']==u'articleresultbody', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
#     if description != [] and heading != []:
#         f = open('../data/corpus/dinamalar/sports/%s.txt'%(file_name.split('.htm')[0]), 'w')
#         f.write('<news>\n');
#         f.write('<headline>');
#         f.write(heading[0].h1.text.encode('utf-8').strip())
#         f.write('</headline>\n');
#         f.write('<description>\n');
#         f.write(description[0].text.encode('utf-8').strip())
#         f.write('</description>\n');
#         f.write('</news>\n');
#         f.close()
#
# file_list = os.listdir('../data/raw/dinamalar/news_details/')
# if file_list != []: file_list = file_list[1:]
# count = len(file_list)
# for file_name in file_list:
#     print '%s more files..'%(count)
#     count -= 1
#     if 'news_detail_asp_id' in file_name:
#         soup = BeautifulSoup(open('../data/raw/dinamalar/news_details/' + file_name), 'html.parser')
#         # import pdb; pdb.set_trace()
#         heading = filter(lambda y: y['class']==[u'newsdetwd'], filter(lambda x: x.has_attr('class'), soup.find_all('div')))
#         description = filter(lambda y: y['id']==u'clsclk', filter(lambda x: x.has_attr('id'), soup.find_all('div')))
#         if description != [] and heading != []:
#             f = open('../data/corpus/dinamalar/news_details/%s.txt'%(file_name.split('.htm')[0]), 'w')
#             f.write('<news>\n');
#             f.write('<headline>');
#             f.write(heading[0].text.encode('utf-8').strip())
#             f.write('</headline>\n');
#             f.write('<description>\n');
#             f.write(description[0].text.encode('utf-8').strip())
#             f.write('</description>\n');
#             f.write('</news>\n');
#             f.close()