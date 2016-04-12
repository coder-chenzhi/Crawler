# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests

FILE_PATH_2014 = "F:\\tmp\\SpeakerDeck\\Monitorama 2014 PDX.html"
URL_2014 = "http://monitorama.com/2014/pdx.html#schedule"
FILE_PATH_2015 = "F:\\tmp\\SpeakerDeck\\Monitorama 2015 PDX.html"
URL_2015 = "http://monitorama.com/2015/pdx.html#schedule"
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}


def get_content_from_html(file_path):
    file_content = ""
    with open(file_path, "r") as fin:
        file_content = fin.read()
    return file_content


def get_content_from_url(url, headers=None):
    r = requests.get(url, headers=headers)
    return r.content


def get_talks(content):
    soup = BeautifulSoup(content, "html.parser")
    talk_div = soup.find_all("div", {"class": "wrap talk"})
    for div in talk_div:
        title = div.find("h5").text
        author = div.find("span").text
        print title + " - " + author


def main():
    # content = get_content_from_html(FILE_PATH_2015)
    content = get_content_from_url(URL_2015, headers=my_headers)
    get_talks(content)

if __name__ == "__main__":
    main()
