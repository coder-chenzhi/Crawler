__author__ = 'chenzhi'

"""
test using proxy in urllib2

"""

import urllib2
from bs4 import BeautifulSoup

if __name__ == '__main__':
    profile_url = 'http://google.com'
    urllib2.install_opener(
        urllib2.build_opener(
            urllib2.ProxyHandler({'http': '127.0.0.1:8087'})
        )
    )
    req=urllib2.Request(profile_url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0'})
    p=urllib2.urlopen(req)
    soup=BeautifulSoup(p, 'html.parser')
    with open("test.html", "w") as f:
        f.write(str(soup))
    print soup
