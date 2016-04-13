# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests


URL_PRE = "https://www.usenix.org"
ROOT_URL = "https://www.usenix.org/conferences/byname/5"
my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0'}
conference_program_urls = {
    2015: "https://www.usenix.org/conference/lisa15/conference-program",
    2014: "https://www.usenix.org/conference/lisa14/conference-program",
    2013: "https://www.usenix.org/conference/lisa13/technical-sessions",
    2012: "https://www.usenix.org/conference/lisa12/technical-sessions",
    2011: "http://static.usenix.org/legacy/events/lisa11/tech/",
    2010: "https://www.usenix.org/legacy/events/lisa10/tech/",
    2009: "https://www.usenix.org/legacy/events/lisa09/tech/",
    2008: "https://www.usenix.org/legacy/events/lisa08/tech/",
    2007: "https://www.usenix.org/legacy/events/lisa07/tech/",
    2006: "https://www.usenix.org/legacy/events/lisa06/tech/"
                       }


def get_page_num():
    r = requests.get(ROOT_URL, headers=my_headers)
    soup = BeautifulSoup(r.content, "html.parser")
    last_page = soup.find_all("li", {"class": "pager-last"})
    if len(last_page) >= 1:
        url = last_page[0].find("a")['href']  # url e.g. "/conferences/byname/5?page=2"
        return int(url.split("=")[1])
    else:
        print("can not find element")
        return None


def get_page_urls():
    page_urls = [ROOT_URL]
    page_num = get_page_num()
    for i in range(page_num):
        page_urls.append(ROOT_URL + "?page=" + str(i+1))
    return page_urls


def get_conference_urls():
    conference_urls = []
    for page_url in get_page_urls():
        r = requests.get(page_url, headers=my_headers)
        soup = BeautifulSoup(r.content, "html.parser")
        urls = [a["href"] for a in soup.find("div", {"class": "view-content"}).find_all("a")]
        for url in urls:
            if url.startswith("/conference"):
                conference_urls.append(URL_PRE + url)
    return conference_urls


def get_program_since_2013(content):
    """
    every talk is warped by a div whose class is "node paper-node", and for each talk div,
    it contains a <h2> tag with class "node-title" and a <div> tag with class "content".
    Some talk will have a <tag> with class "node-links", which means this talk provides some resource to download.
    :param content:
    :return:
    """
    talks = []
    soup = BeautifulSoup(content, "html.parser")
    # print content
    all_talks = soup.find_all("div", {"class": "node-paper"})
    # print "number of talks", len(all_talks)
    for talk in all_talks:
        title = talk.find("h2", {"class": "node-title"}).find("a").text.strip()
        div_content = talk.find("div", {"class": "node-content"})
        if div_content is None:
            talks.append("Title:" + title)
            continue

        try:
            talk_type = div_content.find("div", {"class": "field-name-field-presentation-label"}).\
                find("div", {"class": "even"}).text.strip()
        except:
            talk_type = "None"

        # speaker of this talk
        try:
            speakers = div_content.find("div", {"class": "field-name-field-presented-by"}).\
                find("div", {"class": "even"}).text.strip()
        except:
            speakers = "None"

        try:
            description = div_content.find("div", {'class': "field-name-field-paper-description-long"}).text.strip()
        except:
            description = "None"

        # what resource they provide for this talk
        avaiable_res = []
        if div_content.find("div", {"class": "pdf"}):
            avaiable_res.append("pdf")
        if div_content.find("div", {"class": "slides"}):
            avaiable_res.append("slides")
        if div_content.find("div", {"class": "video"}):
            avaiable_res.append("video")
        if div_content.find("div", {"class": "audio"}):
            avaiable_res.append("audio")
        if len(avaiable_res) == 0:
            avaiable_res.append("None")
        talks.append("Title:{Title}\nType:{Type}\nSpeakers:{Speakers}\nDescription:{Description}\nResource:{Resource}".
                     format(Title=title, Type=talk_type, Speakers=speakers, Description=description,
                            Resource="/".join(avaiable_res)))
    return talks


def get_program_2012(content):
    """
    author <div> class is different form get_program_since_2013()
    :param content:
    :return:
    """
    talks = []
    soup = BeautifulSoup(content, "html.parser")
    # print content
    all_talks = soup.find_all("div", {"class": "node-paper"})
    # print "number of talks", len(all_talks)
    for talk in all_talks:
        title = talk.find("h2", {"class": "node-title"}).find("a").text.strip()
        div_content = talk.find("div", {"class": "node-content"})
        if div_content is None:
            talks.append("Title:" + title)
            continue

        try:
            talk_type = div_content.find("div", {"class": "field-name-field-presentation-label"}).\
                find("div", {"class": "even"}).text.strip()
        except:
            talk_type = "None"

        # speaker of this talk
        try:
            speakers = div_content.find("div", {"class": "field-name-field-paper-people-text"}).\
                find("div", {"class": "even"}).text.strip()
        except:
            speakers = "None"

        # what resource they provide for this talk
        avaiable_res = []
        if div_content.find("div", {"class": "pdf"}):
            avaiable_res.append("pdf")
        if div_content.find("div", {"class": "slides"}):
            avaiable_res.append("slides")
        if div_content.find("div", {"class": "vedio"}):
            avaiable_res.append("vedio")
        if div_content.find("div", {"class": "audio"}):
            avaiable_res.append("audio")
        if len(avaiable_res) == 0:
            avaiable_res.append("None")
        talks.append("Title:{Title}\nType:{Type}\nSpeakers:{Speakers}\nResource:{Resource}".
                     format(Title=title, Type=talk_type, Speakers=speakers, Resource="/".join(avaiable_res)))
    return talks


def get_program_between_2011_and_2006(content):
    pass


def get_program(year):
    content = requests.get(conference_program_urls[year], headers=my_headers).content
    if year >= 2013:
        return get_program_since_2013(content)
    elif year == 2012:
        return get_program_2012(content)
    elif year >= 2006:
        return get_program_between_2011_and_2006(content)


if __name__ == "__main__":
    # print(get_conference_urls())
    print("\n\n".join(get_program(2015)))