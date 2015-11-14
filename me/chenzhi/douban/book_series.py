# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'chenzhi'

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    base_url = "http://book.douban.com/series/129?order=time"
    total_page_num = 14
    suffixs = [""]
    for i in range(2, total_page_num+1):
        suffixs.append("&page="+str(i))
    # print suffix
    for s in suffixs:
        url = base_url + s
        r = requests.get(url)
        page = r.content
        soup = BeautifulSoup(page)
        all_item_div = soup.find_all("li", class_="subject-item")

        for item in all_item_div:
            book_name = item.find_all("h2")[0].find_all("a")[0].get('title')
            info = item.find_all("div", class_="pub")[0].text.strip()
            rating = item.find_all("span", class_="rating_nums")
            if len(rating) == 0:
                rating = "少于10人评价"
            else:
                rating = rating[0].text
            print book_name
            print info
            print rating
            print "\n"
