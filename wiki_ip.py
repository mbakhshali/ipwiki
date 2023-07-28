from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

dicIP = {}
ls = []


url = 'https://en.wikipedia.org/w/index.php?title=Ministry_of_Communications_(India)&action=history'

while True:
    def ip2location(url):
        html = urlopen(url)
        bsObj = BeautifulSoup(html, features="html.parser")
        for links in bsObj.findAll('a', {'class' : 'mw-userlink mw-anonuserlink'}):
            if links is not None:
                if links not in dicIP:
                    ip = finder(links.get_text())
                    dicIP[links.get_text()] = ip
        if len(dicIP) <=0:
            return 'Nothing found!'


    def finder(ip):
        locationFile = urlopen('http://ip-api.com/json/' + ip).read().decode('utf-8')
        result = json.loads(locationFile)
        country = result.get('country')
        city = result.get('city')
        dic = {}
        dic[country] = city
        return dic

    ip2location(url)
    html = urlopen(url)
    bsObj = BeautifulSoup(html, features="html.parser")

    nextPage = bsObj.find('a', {'class' : 'mw-nextlink'})

    if nextPage is not None:
        if len(nextPage) == 1:
            url = 'https://en.wikipedia.org'+nextPage.attrs['href']
            ip2location(url)
    else:
        break

print(dicIP)
