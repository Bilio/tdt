import urllib2
from bs4 import BeautifulSoup

elections_main_url = 'http://www.dailythanthi.com/News/Election2016/%d'
elections_urllist = []

for i in range(1,21):
    url = elections_main_url%i
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    heading = filter(lambda y: u'middle_div' in y['class'], filter(lambda x: x.has_attr('class'), soup.find_all('div')))
    elections_urllist += map(lambda x: str(x.a['href']), heading)
