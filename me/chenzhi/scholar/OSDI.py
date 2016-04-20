# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests


proceeding_urls = {
    1994: "http://dl.acm.org/citation.cfm?id=1267638&picked=prox&CFID=772465208&CFTOKEN=92804237",
    1996: "http://dl.acm.org/citation.cfm?id=238721&picked=prox&CFID=772465208&CFTOKEN=92804237",
    1999: "http://dl.acm.org/citation.cfm?id=296806&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2000: "http://dl.acm.org/citation.cfm?id=1251229&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2002: "http://dl.acm.org/citation.cfm?id=1060289&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2004: "http://dl.acm.org/citation.cfm?id=1251254&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2006: "http://dl.acm.org/citation.cfm?id=1298455&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2008: "http://dl.acm.org/citation.cfm?id=1855741&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2010: "http://dl.acm.org/citation.cfm?id=1924943&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2012: "http://dl.acm.org/citation.cfm?id=2387880&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2014: "http://dl.acm.org/citation.cfm?id=2685048&picked=prox&CFID=772465208&CFTOKEN=92804237"
}

tab_urls = {
    1994: "http://dl.acm.org/tab_about.cfm?id=1267638&type=proceeding&sellOnline=0&parent_id=1267638&parent_type=proceeding"

}

base_url = "http://dl.acm.org/"
flat_layout = "&preflayout=flat"


my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}


def get_proceedings_from_url(year):
    r = requests.get(proceeding_urls[year] + flat_layout, headers=my_headers)
    return r.content


def parse(year, content):
    soup = BeautifulSoup(content, "html.parser")
    if year == 2004:
        table = soup.find_all("table", {"class": "text12"})[0]
    else:
        table = soup.find_all("table", {"class": "text12"})[1]
    papers = [a for a in table.find_all("a") if "citation.cfm" in a["href"]]
    paper_rows = [paper.parent.parent.parent for paper in papers]
    for paper, paper_row in zip(papers, paper_rows):
        print "%0 Conference Proceedings"
        print "%D", year
        print "%B", "OSDI", year
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


# not finished
def OSDI_2004():
    program_url = "https://www.usenix.org/legacy/events/osdi04/tech/"
    r = requests.get(program_url, headers=my_headers)
    soup = BeautifulSoup(r.content, "html.parser")
    main_table = soup.find_all("table")[4]
    urls = [url for url in main_table.find_all("a") if url.has_attr("href")
                                        and not url["href"].startswith("#") and not url["href"].startswith("mailto")]
    for url in urls:
        print "%0 Conference Proceedings"
        print "%D 2004"
        print "%T", url.text
        authors = url.parent.next_siblings[1]

        print "%B OSDI 2004"
        print "%U", program_url + url["href"]
    print("\n".join(urls))
    print "Finished."


if __name__ == "__main__":
    parse(2004, get_proceedings_from_url(2004))
    """
    for key in proceeding_urls:
        parse(key, get_proceedings_from_url(key))
    """