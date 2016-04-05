# -*- coding: utf-8 -*-

"""
You can redirect the output to a file, then write a bash scripts to read the file line by line and download each url
example bash scripts like below

#!/bin/bash
while IFS='' read -r line || [[ -n "$line" ]]; do
    wget $line
done < "$1"

"""
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests

ROOT_URL = "https://speakerdeck.com"

MAIN_PAGE = "https://speakerdeck.com/monitorama"

MAIN_FILE_PATH = "F:\\tmp\\SpeakerDeck\\Presentations by Monitorama __ Speaker Deck.html"

SLIDE_FILE_PATH = "F:\\tmp\\SpeakerDeck\\Berlin 2013 - Session - Lindsay Holmwood __ Speaker Deck.html"

my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}


def get_content_from_html(file_path):
    file_content = ""
    with open(file_path, "r") as fin:
        file_content = fin.read()
    return file_content


def get_content_from_url(url, headers=None):
    r = requests.get(url, headers=headers)
    return r.content


def get_all_pages(content):
    soup = BeautifulSoup(content, "html.parser")
    all_links = []
    for span in soup.find_all("span", {"class": "page"}):
        if span.find("a"):
            all_links.append(ROOT_URL + "/" + span.find("a").get("href"))
    return all_links


def get_all_slides_page(content):
    soup = BeautifulSoup(content, "html.parser")
    all_links = []
    for span in soup.find_all("h3", {"class": "title"}):
        if span.find("a"):
            all_links.append(ROOT_URL + "/" + span.find("a").get("href"))
    # print all_links
    return all_links


def get_download_url(content):
    soup = BeautifulSoup(content, "html.parser")
    li = soup.find_all("ul",  {"class": "delimited share"})[0].find_all("li")[-1]
    # print li.find("a").get("href")
    return li.find("a").get("href")


def main():
    all_pages = get_all_pages(get_content_from_url(MAIN_PAGE, headers=my_headers))
    all_pages.append(MAIN_PAGE)
    download_urls = []
    for page in all_pages:
        all_slides_page = get_all_slides_page(get_content_from_url(page, headers=my_headers))
        for silde_page in all_slides_page:
            download_url = get_download_url(get_content_from_url(silde_page, headers=my_headers))
            download_urls.append(download_url)
            print download_url
    return download_urls

if __name__ == "__main__":
    # print get_content_from_html(FILE_PATH)
    # get_all_slides_page(get_content_from_html(MAIN_FILE_PATH))
    get_download_url(get_content_from_html(SLIDE_FILE_PATH))