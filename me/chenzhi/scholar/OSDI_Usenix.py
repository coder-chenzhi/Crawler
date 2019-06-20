# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests


USENIX_urls = {
    1994: "http://dl.acm.org/citation.cfm?id=1267638&picked=prox&CFID=772465208&CFTOKEN=92804237",
    1996: "http://dl.acm.org/citation.cfm?id=238721&picked=prox&CFID=772465208&CFTOKEN=92804237",
    1999: "http://dl.acm.org/citation.cfm?id=296806&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2000: "http://dl.acm.org/citation.cfm?id=1251229&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2002: "http://dl.acm.org/citation.cfm?id=1060289&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2004: "http://dl.acm.org/citation.cfm?id=1251254&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2006: "http://dl.acm.org/citation.cfm?id=1298455&picked=prox&CFID=772465208&CFTOKEN=92804237",
    2008: "https://www.usenix.org/legacy/events/osdi08/tech/",
    2010: "https://www.usenix.org/legacy/event/osdi10/tech/",
    2012: "https://www.usenix.org/conference/osdi12/technical-sessions",
    2014: "https://www.usenix.org/conference/osdi14/technical-sessions",
    2016: "https://www.usenix.org/conference/osdi16/program"
}

my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}


def get_program_before_2010(year):
    program_url = USENIX_urls[year]
    r = requests.get(program_url, headers=my_headers)
    soup = BeautifulSoup(r.content, "html.parser")
    all_talks = soup.find_all("p", {"class": "techdesc"})
    for talk in all_talks:
        text = talk.text.replace("Awarded Jay Lepreau Best Paper!\n", "")
        # print text
        title = text.split("\n")[0].strip()
        try:
            authors = text.split("\n")[1].strip()
        except:
            authors = "No authors information"
        print(title + "\t" + authors)


def get_program_2010():
    """
    :param year:
    :return:
    """
    program_url = USENIX_urls[2010]
    r = requests.get(program_url, headers=my_headers)
    soup = BeautifulSoup(r.content, "html.parser")
    all_talks = soup.find_all("p", {"class": "fullpaper1"})
    for talk in all_talks:
        text = talk.text.replace("Awarded Jay Lepreau Best Paper!", "")
        # print text
        if "\n\t\t" not in text:
            continue

        title = text.split("\n\t\t")[0].strip()
        try:
            authors = text.split("\n\t\t")[1].strip()
        except:
            authors = "No authors information"
        print(title + "\t" + authors)


def get_program_since_2012(year):
    """
    :param year:
    :return:
    """
    program_url = USENIX_urls[year]
    r = requests.get(program_url, headers=my_headers)
    soup = BeautifulSoup(r.content, "html.parser")
    # print content
    all_talks = soup.find_all("div", {"class": "node-paper"})
    # print "number of talks", len(all_talks)
    for talk in all_talks:
        title = talk.find("h2", {"class": "node-title"}).find("a").text.strip()
        # print("Title:" + title)
        div_content = talk.find("div", {"class": "node-content"})
        if div_content is None:
            # print("content is null")
            print(title + "\tOther information is missing\n")
            continue

        # speaker of this talk
        speakers = ""
        try:
            speakers = div_content.find("div", {"class": "field-name-field-paper-people-text"}).\
                find("div", {"class": "odd"}).find("p").text.strip()
            # print "speakers:" + speakers
        except:
            speakers = "None"

        print(title + "\t" + speakers)


def get_program(year):
    if year >= 2012:
        get_program_since_2012(year)
    elif year == 2010:
        get_program_2010()
    elif year < 2010:
        get_program_before_2010(year)

if __name__ == "__main__":
    get_program(2008)