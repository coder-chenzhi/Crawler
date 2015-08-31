# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bs4 import BeautifulSoup


def get_page_count(content):
    soup = BeautifulSoup(content)
    results = soup.find_all("input", value="跳页")

    if len(results) > 1:
        print "页面有误！跳页出现", len(results)
    elif results is None:
        print "没有跳页，默认只有一页"
        return 1
    else:
        result = results[0]
        page_count = result.nextSibling
        page_count = page_count.replace('页', '')
        num =  page_count.split('/')
        print num[1]
        return num[1]


def get_all_links(content):
    prefix = "http://weibo.cn"
    soup = BeautifulSoup(content)
    valid_links = []
    all_links = [i.get("href") for i in soup.find_all("a", href=True)]
    for link in all_links:
        if link.startswith("/im/chat?uid="):
            valid_links.append(prefix + link)
        elif link.startswith(prefix + "/im/chat?uid="):
            valid_links.append(link)
    print valid_links
    return valid_links

if __name__ == "__main__":
    f = open("F:\\temp\\msg.htm", "r")
    get_all_links(f.read())