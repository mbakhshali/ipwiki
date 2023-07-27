from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

dicIP = {}
ls = []
def ip2location(title):
    html = urlopen('https://en.wikipedia.org/w/index.php?title='+title+'&action=history')
    bsObj = BeautifulSoup(html, features="html.parser")
    for links in bsObj.findAll('a', {'class' : 'mw-userlink mw-anonuserlink'}):
        if links is not None:
            if links not in dicIP:
                ip = finder(links.get_text())
                dicIP[links.get_text()] = ip
    return dicIP


def finder(ip):
    locationFile = urlopen('http://ip-api.com/json/' + ip).read().decode('utf-8')
    result = json.loads(locationFile)
    country = result.get('country')
    city = result.get('city')
    dic = {}
    dic[country] = city
    return dic


print(ip2location('Sony'))

print('ok')