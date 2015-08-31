# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bs4 import BeautifulSoup


def get_page_count(content):
    soup = BeautifulSoup(content)
    results = soup.find_all("input", value="跳页")
    if len(results) != 1:
        print "页面有误！跳页出现", len(results)
    for result in results:
        page_count = result.nextSibling
        page_count = page_count.replace('页', '')
        num =  page_count.split('/')
        print num[0], num[1]

if __name__ == "__main__":
    f = open("F:\\temp\\test.htm", "r")
    get_page_count(f.read())