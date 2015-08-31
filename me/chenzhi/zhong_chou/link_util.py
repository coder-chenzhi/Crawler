# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
from bs4 import BeautifulSoup
import requests
import time

def get_links(url, filter=None):
    r = requests.get(url)
    page = r.content
    soup = BeautifulSoup(page)
    valid_links = []
    all_links = [i.get("href") for i in soup.find_all("a", href=True)]
    # print("filter %s" % filter)
    if filter is not None:
        for i in all_links:
            if bool(re.match(filter, i)):
                valid_links.append(i)
        return valid_links
    else:
        return all_links

def get_all_items(url):
    description = []
    title = []
    money_raised = []
    percent = []
    day_left = []
    r = requests.get(url)
    page = r.content
    soup = BeautifulSoup(page)
    all_item_div = soup.find_all("div", class_="list-item")

    for div in all_item_div:
        description.append(div.find_all("img")[0].get("alt"))
        title.append(div.find_all("h2")[0].find_all("a")[0].text)
        try:
            money_raised.append(div.find_all("p", class_="z-raising")[0].find_all("i")[0].text.replace(",", ""))
        except:
            try:
                money_raised.append(div.find_all("p", class_="z-raising clearfix")[0].find_all("i")[0].text.replace(",", ""))
            except:
                money_raised.append("已失败")
                percent.append("")
                day_left.append("")
                continue
        percent.append(div.find_all("span", class_="rate1")[0].text)
        day_left.append(div.find_all("span", class_="rate2")[0].text)

    file = open(url.split("/")[-1] + ".csv", "w")
    file.write("标题,详细介绍,已筹金额,进度,结束日期\n".encode('gb18030'))
    for i in range(len(title)):
        file.write((",".join([title[i], description[i], money_raised[i], percent[i], day_left[i]]) + "\n").encode('gb18030'))
    file.close()
    print "Finish parse " + url
    # test_div = all_item_div[0]
    # print test_div
    # print test_div.find_all("img")[0].get("alt")
    # print test_div.find_all("h2")[0].find_all("a")[0].text
    # print test_div.find_all("p", class_="z-raising")[0].find_all("i")[0].text
    # print test_div.find_all("span", class_="rate1")[0].text
    # print test_div.find_all("span", class_="rate2")[0].text

def get_all_subpages(url):
    r = requests.get(url)
    page = r.content
    soup = BeautifulSoup(page)
    all_links = [i.get("href") for i in soup.find_all("a", text="尾页")]
    count = int(all_links[0].split('-')[-1])
    print all_links[0]
    print 'number of pages for this catogory:', count
    return count

if __name__ == "__main__":
    # get_all_items("http://www.zhongchou.cn/browse/id-22")
    url = "http://www.zhongchou.cn/browse/id-10000"
    #count = get_all_subpages(url)
    # get_all_items(url)
    get_all_items(url + "-p-8")
    get_all_items(url + "-p-9")

    # for i in range(2, count + 1):
    #     time.sleep(5)
    #     get_all_items(url + "-p-" + str(i))