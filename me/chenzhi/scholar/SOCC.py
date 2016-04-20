# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests


proceeding_urls = {
    2015: "http://dl.acm.org/citation.cfm?id=2806777&CFID=770769122&CFTOKEN=79711298",
    2014: "http://dl.acm.org/citation.cfm?id=2670979&CFID=770769122&CFTOKEN=79711298",
    2013: "http://dl.acm.org/citation.cfm?id=2523616&CFID=770769122&CFTOKEN=79711298",
    2012: "http://dl.acm.org/citation.cfm?id=2391229&CFID=770769122&CFTOKEN=79711298",
    2011: "http://dl.acm.org/citation.cfm?id=2038916&CFID=770769122&CFTOKEN=79711298",
    2010: "http://dl.acm.org/citation.cfm?id=1807128&CFID=770769122&CFTOKEN=79711298#"
}

proceeding_file_path = {
    2015: "F:\\tmp\\acm\\Proceedings of the 6th ACM symposium on Cloud computing.html",
    2014: "F:\\tmp\\acm\\Proceedings of the 5th ACM symposium on Cloud computing.html",
    2013: "F:\\tmp\\acm\\Proceedings of the 4th ACM symposium on Cloud computing.html",
    2012: "F:\\tmp\\acm\\Proceedings of the 3rd ACM symposium on Cloud computing.html",
    2011: "F:\\tmp\\acm\\Proceedings of the 2nd ACM symposium on Cloud computing.html",
    2010: "F:\\tmp\\acm\\Proceedings of the 1st ACM symposium on Cloud computing.html"
}

my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}


def get_proceedings_from_url(year):
    r = requests.get(proceeding_urls[year], headers=my_headers)
    return r.content


def get_proceedings_from_file(year):
    file_path = proceeding_file_path[year]
    with open(file_path, "r") as fin:
        file_content = fin.read()
    return file_content


def parse(year, content):
    soup = BeautifulSoup(content, "html.parser")
    table = soup.select("#prox div table")[0]
    papers = [a for a in table.find_all("a") if "citation.cfm" in a["href"]]
    for paper in papers:
        print "%0 Conference Proceedings"
        print "%D", year
        print "%B", "SOCC", year
        title =  paper.text
        print "%T", title
        paper_url = paper["href"]
        print "%U", paper_url
        authors = paper.parent.parent.parent.nextSibling.nextSibling.text.strip()
        for author in authors.split(","):
                print "%A", author.strip()
        abstract = paper.parent.parent.parent.nextSibling.nextSibling.nextSibling.nextSibling.\
            nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.nextSibling
        if type(abstract) is type(paper):
            abstract = abstract.find_all("span")
            if len(abstract) == 2:
                abstract = abstract[1].text
                print "%X", abstract
        print("\n")


if __name__ == "__main__":
    year = 2015
    parse(year, get_proceedings_from_file(year))
