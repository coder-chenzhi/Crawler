# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests
import re
import time
import random


ROOT_URL = "http://chuansong.me"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}


def get_all_articles(ID):
    url = ROOT_URL + "/account/" + ID
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print "连接错误"
        return

    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    all_links = [i.get("href") for i in soup.find_all("a", href=True)]
    page_links = []
    all_page_links = []
    page_link_pattern = ".*account.*start"
    for link in all_links:
        if bool(re.match(page_link_pattern, link)):
                page_links.append(link)
    ends_page = int(page_links[-2][page_links[-2].rfind("=") + 1:])
    for i in range(0, ends_page+12, 12):
        all_page_links.append("{}?start={}".format(url, i))
    # print("\n".join(all_page_links))
    all_articles = []
    for page_link in all_page_links:
        time.sleep(random.choice([1, 2, 3]))
        r = requests.get(page_link, headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        all_ariticles_div = soup.find_all("div", {"class": "feed_item_question"})
        for div in all_ariticles_div:
            article_title = div.find("a", {"class": "question_link"}).text.strip()
            article_url = ROOT_URL + div.find("a", {"class": "question_link"})['href']
            article_time = div.find("span", {"class": "timestamp"}).text.strip()
            all_articles.append([article_title, article_url, article_time])
            print(article_title + "\t" + article_url + "\t" + article_time)


def get_all_articles_filter_by_time(ID, start, end):
    pass


def get_all_articles_for_year(ID, year):
    pass


if __name__ == "__main__":
    get_all_articles("zuiheikeji")