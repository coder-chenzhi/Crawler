# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests
import json
import pprint
import threading
import Queue

my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}


def get_urls_from_file(file_path):
    with open(file_path) as f:
        urls = f.readlines()
    return urls


def crawl_each_paper_url(url, queue):
    paper = {}
    abstract_url = url.replace("citation", "tab_abstract")

    r = requests.get(url, headers=my_headers)
    content = r.content
    soup = BeautifulSoup(content, "html.parser")

    title = soup.find_all("h1")[0].text
    paper["title"] = title
    authors_profile = soup.find_all("a", {"title": "Author Profile Page"})
    # authors_affiliation = soup.find_all("a", {"title": "Institutional Profile Page"})
    if len(authors_profile) != len(authors_profile):
        print(title, url, "the number of authors is not equal to affiliation.")
    else:
        authors_data = []
        for i in range(len(authors_profile)):
            author_url = "http://dl.acm.org/" + authors_profile[i]["href"]
            author_name = authors_profile[i].text
            authors_affiliation = authors_profile[i].parent.parent.contents[5].\
                find_all("a", {"title": "Institutional Profile Page"})
            if len(authors_affiliation) != 0:
                affiliation_url = "http://dl.acm.org/" + authors_affiliation[0]["href"]
                affiliation_name = authors_affiliation[0].text
            else:
                affiliation_url = "None"
                affiliation_name = authors_profile[i].parent.parent.contents[5].text
            authors_data.append({"author_name": author_name,
                                 "author_url": author_url,
                                 "affiliation_name": affiliation_name,
                                 "affiliation_url": affiliation_url})
        paper["authors"] = authors_data
    print("crawl", abstract_url)
    r = requests.get(abstract_url, headers=my_headers)
    content = r.content
    soup = BeautifulSoup(content, "html.parser")
    abstract = soup.find_all("p")[0].text
    paper["abstract"] = abstract
    # pprint.pprint(paper)
    queue.put(paper)


if __name__ == "__main__":
    in_file_path = "ICSE2010PaperURL.txt"
    out_path = "ICSE2010.json"
    urls = get_urls_from_file(in_file_path)
    # urls = ["http://dl.acm.org/citation.cfm?id=1806823&CFID=756107655&CFTOKEN=59443197"]
    papers = {"items": []}
    result = Queue.Queue()
    threads = []
    for i, url in enumerate(urls):
        print("crawl", i)
        t = threading.Thread(target=crawl_each_paper_url, name=i, args=(url, result), )
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    for _ in urls:
        papers["items"].append(result.get())

    # pprint.pprint(papers)
    with open(out_path, 'w') as outfile:
        json.dump(papers, outfile)