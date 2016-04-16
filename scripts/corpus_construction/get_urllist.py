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

tennis_main_url = 'http://www.dailythanthi.com/Sports/Tennis/%d'
tennis_urllist = []
for i in range(1,3):
    url = tennis_main_url%i
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    heading = filter(lambda y: u'middle_div' in y['class'], filter(lambda x: x.has_attr('class'), soup.find_all('div')))
    tennis_urllist += map(lambda x: str(x.a['href']), heading)

hockey_main_url = 'http://www.dailythanthi.com/Sports/Hockey/%d'
hockey_urllist = []
for i in range(1,3):
    url = hockey_main_url%i
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')
    heading = filter(lambda y: u'middle_div' in y['class'], filter(lambda x: x.has_attr('class'), soup.find_all('div')))
    hockey_urllist += map(lambda x: str(x.a['href']), heading)

da_urllist = [
    'http://www.dailythanthi.com/News/World/2016/04/10151149/Pakistan-offers-condolences-over-Kerala-temple-tragedy.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/10163702/6-8-Magnitude-Earthquake-Strikes-Pakistan-Tremors.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/11085020/Powerful-quake-jolts-Pakistan-6-killed.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/11200704/Suicide-bombing-kills-12-new-Army-recruits-in-Jalalabad.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/12132359/Hand-grenade-submitted-as-proof-explodes-inside-Pakistan.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/13002948/In-NepalTerrible-tragedyBus-accident23-peopleKills.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/13112709/19-passengers-killed-in-Pakistan-bus-accident-official.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/13140252/Girl-in-Japan-falls-to-her-death-after-watching-anime.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/14011510/In-PakistanBustruckIn-conflict19-peopleKills.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/14133128/Australian-among-12-killed-in-Papua-New-Guinea-plane.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/14193025/Japan-earthquake-of-64-magnitude-hits-southern-part.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/15030915/Crane-collapse-at-Chinese-construction-site-kills.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/16225431/Bhutan-aircraft-had-a-miraculous-escape-after-getting.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/16211122/Japan-Quakes-Disrupt-Sony-Image-Sensor-Production.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/16204112/Scores-trapped-as-Japan-quakes-toll-hits-41.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/16091427/New-Japan-quake-kills-seven-with-widespread-damage.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/09155220/23-killed-in-Peru-bus-crash.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/05215019/71-killed-in-rains-landslides-in-Pakistan.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/05005215/In-PakistanHeavy-rainFlood57-peopleDeath.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/04021335/Pacific-69-magnitude-earthquake-strikes-off-Vanuatu.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/03153458/Tsunami-alert-issued-after-large-quake-hits-off-Vanuatu.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/02143425/Terrible-Wind-Storm-Blew-Away-Roofs-and-Houses--China.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/02010418/Central-Japan-Shaken-by-Offshore-Magnitude61-Earthquake.vpf',
    'http://www.dailythanthi.com/News/World/2016/04/01100925/Earthquake-of-magnitude-6-jolts-Japan-s-Kinki-region.vpf',
    'http://www.dailythanthi.com/News/World/2016/03/26170655/Postquake-cracks-and-holes-develop-in-Mt-Everest.vpf',
    'http://www.dailythanthi.com/News/World/2016/03/25002604/In-ChinaCoalMining-accident19-peopleKills.vpf',
    'http://www.dailythanthi.com/News/World/2016/03/21105400/Russia-rocked-by-huge-earthquake-measuring-66-as-tremor.vpf',
    'http://www.dailythanthi.com/News/World/2016/03/19133344/Two-Indians-among-62-dead-in-FlyDubai-plane-crash.vpf',
    'http://www.dailythanthi.com/News/World/2016/03/19082524/Plane-with-55-passengers-on-board-crashes-in-Russia.vpf'
]

business_main_url = 'http://tamil.thehindu.com/business/business-supplement/?pageNo=%d'
business_urllist = []
for i in range(1,46):
    url = business_main_url%i
    try:
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        heading_class = filter(lambda y: u'headlinessub' in y['class'], filter(lambda x: x.has_attr('class'), soup.find_all('div')))
        business_urllist += map(lambda x: x.a['href'], heading_class[0].find_all('h3'))
    except:
        pass


vehicle_main_url = 'http://tamil.thehindu.com/business/article6426694.ece?widget-art=four-rel'
vehicle_urllist = []
url = vehicle_main_url
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
heading_class = filter(lambda y: u'body' == y['id'], filter(lambda x: x.has_attr('id'), soup.find_all('div')))
vehicle_urllist = map(lambda x: x.a['href'], heading_class[0].find_all('h3'))