
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import shutil
from bs4 import BeautifulSoup
import requests
import os


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}
PREFIX = "https://manhua-me.oss-cn-hongkong.aliyuncs.com/statics/images/mh"
ROOT_URL = "http://www.kanmanhua.xyz"


def get_img_url(url):
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("连接错误")
        return

    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    all_links = soup.find_all("img")
    img_links = []
    for link in all_links:
        if link.has_attr('data-original'):
            if link['data-original'].startswith(PREFIX):
                img_links.append(link['data-original'])
    return img_links[0]


def get_volumns(url):
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("连接错误")
        return

    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    all_volumns = [(i.get("href"), i.text) for i in soup.find_all("a", href=True) if i.has_attr("sort")]
    return all_volumns


def get_pages(url):
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("连接错误")
        return

    prefix = url.replace(".html", "").replace(ROOT_URL, "")
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    all_pages = [(i.get("href"), i.text) for i in soup.find_all("a", href=True) if i.get("href").startswith(prefix)]
    return [page for page in all_pages if page[1].isdigit()]


if __name__ == '__main__':
    OUTPUT = "D:\\wd500g\\Video\\从零开始的异世界\\"
    h_id = 67923

    HOME_URL_TEMPLATE = "http://www.kanmanhua.xyz/manhua-{h_id}"
    VOLUME_URL_TEMPLATE = "http://www.kanmanhua.xyz/manhua-{h_id}/{v_id}.html"

    home_url = HOME_URL_TEMPLATE.format(h_id=h_id)
    volumes = get_volumns(home_url)
    for v in volumes:
        print("volumes:", v)
        REAL_OUTPUT = os.path.join(OUTPUT, v[1])
        if not os.path.exists(REAL_OUTPUT):
            os.makedirs(REAL_OUTPUT)
        v_id = v[0].split("/")[-1].replace(".html", "")
        volumn_url = VOLUME_URL_TEMPLATE.format(h_id=h_id, v_id=v_id)
        pages = get_pages(volumn_url)

        download_urls = []
        for page in pages:
            page_url = ROOT_URL + page[0]
            download_urls.append((get_img_url(page_url), page[1]))

        for link, index in download_urls:
            r = requests.get(link, stream=True)
            with open(os.path.join(REAL_OUTPUT, str(index)+".jpg"), 'wb') as f:
                shutil.copyfileobj(r.raw, f)
