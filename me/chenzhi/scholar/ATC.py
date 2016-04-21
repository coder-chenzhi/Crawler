# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests

tab_urls = {
    2015: "2813767", 2014: "2643634", 2013: "2535461", 2012: "2342821", 2011: "2002181",
    2010: "1855840", 2009: "1855807", 2008: "1404014", 2007: "1364385", 2006: "1267359",
    2005: "1247360", 2004: "1247415", 2003: "1247340", 2002: "647057", 2001: "647055",
    2000: "1267724", 1999: "1268708", 1998: "1268256", 1997: "1268680", 1996: "1268299",
}

base_url = "http://dl.acm.org/"
proceeding_url_format = "http://dl.acm.org/tab_about.cfm?id={id}&type=proceeding&sellOnline=0&parent_id={id}&parent_type=proceeding"
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}


def get_proceedings_from_url(year):
    r = requests.get(proceeding_url_format.format(id=tab_urls[year]), headers=my_headers)
    return r.content


def parse(year, content):
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find_all("table", {"class": "text12"})[0]
    papers = [a for a in table.find_all("a") if "citation.cfm" in a["href"]]
    paper_rows = [paper.parent.parent.parent for paper in papers]
    for paper, paper_row in zip(papers, paper_rows):
        print "%0 Conference Proceedings"
        print "%D", year
        print "%B", "ATC", year
        title = paper.text
        print "%T", title
        paper_url = base_url + paper["href"]
        print "%U", paper_url
        next_rows = list(paper_row.next_siblings)
        authors = next_rows[1].text.strip()
        for author in authors.split(","):
                print "%A", author.strip()
        for row in next_rows:
            # judge if we have arrived at next paper,
            if row not in paper_rows:
                # judge if this row is a valid row
                if type(row) is type(paper):
                    abstract = row.find("span", {"style": "display:none;"})
                    if abstract is not None:
                        abstract = abstract.text.strip()
                        print "%X", abstract
                        continue
            else:
                break
        print("\n")


if __name__ == "__main__":
    """
    for key in tab_urls:
        parse(key, get_proceedings_from_url(key))
    """
    year = 2009
    parse(year, get_proceedings_from_url(year))
