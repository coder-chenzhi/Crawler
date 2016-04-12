# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bs4 import BeautifulSoup
import requests

__author__ = 'chenzhi'

"""
Crawl information of IEEE CLUSTER from DBLP

"""


def crawl_2014():
    def what_i_want(tag):
        return tag.name == "h2" or tag.name == "h3" or \
               (tag.name == "li" and tag.has_attr('itemtype')
                and tag['itemtype'] == "http://schema.org/ScholarlyArticle")

    def output_to_excel(content):
        conference_name = ""
        session_name = ""
        print "Conference\tSession\tTitle\tDOI\tAuthor\t"
        for item in content:
            if item.name == "h2":
                conference_name = item.string.encode("utf-8")
            elif item.name == "h3":
                session_name = item.string.encode("utf-8")
            else:
                # print ""
                # title
                title = item.find(class_="title").text.encode("utf-8")
                # DOI URL
                url = item.find(lambda s: s.name == "a" and
                                        s.has_attr("itemprop") and s['itemprop'] == "url")["href"].encode("utf-8")
                Authors = [tag.text.encode("utf-8") for tag in item.find_all(
                                  lambda s: s.name == "span" and not s.has_attr("class")
                                  and s.has_attr("itemprop") and s['itemprop'] == "name")]
                author = ",".encode("utf-8").join(Authors)
                # print conference_name + "\t" + session_name + "\t" + title + "\t" + url + "\t" + author
                print "\t".encode("utf-8").join([conference_name, session_name, title, url, author])
                # print ""

    def output_to_raw_file(content):
        for item in content:
            if item.name == "h2":
                print "Conference:", item.string
            elif item.name == "h3":
                print "Session:", item.string
            else:
                print ""
                # title
                print "Title:", item.find(class_="title").text
                # DOI URL
                print "URL:", item.find(lambda s: s.name == "a" and
                                        s.has_attr("itemprop") and s['itemprop'] == "url")["href"]
                Authors = [tag.text.encode("utf-8") for tag in item.find_all(
                                  lambda s: s.name == "span" and not s.has_attr("class")
                                  and s.has_attr("itemprop") and s['itemprop'] == "name")]
                print(",".encode("utf-8").join(Authors))
                print ""

    url = "http://dblp.uni-trier.de/db/conf/cluster/cluster2014.html"
    r = requests.get(url)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    content = soup.find_all(what_i_want)  # get session sector
    output_to_excel(content)


def crawl_2013():
    def what_i_want(tag):
        return tag.name == "li" and tag.has_attr('itemtype') \
            and tag['itemtype'] == "http://schema.org/ScholarlyArticle"

    def output_to_excel(content):
        print "Title\tDOI\tAuthor\tPage"
        for item in content:
            # print ""
            # title
            title = item.find(class_="title").text.encode("utf-8")
            # DOI URL
            url = item.find(lambda s: s.name == "a" and
                                    s.has_attr("itemprop") and s['itemprop'] == "url")["href"].encode("utf-8")
            Authors = [tag.text.encode("utf-8") for tag in item.find_all(
                              lambda s: s.name == "span" and not s.has_attr("class")
                              and s.has_attr("itemprop") and s['itemprop'] == "name")]
            author = ",".encode("utf-8").join(Authors)
            page = item.find(lambda s: s.name == "span" and
                                    s.has_attr("itemprop") and s['itemprop'] == "pagination").string.encode("utf-8")
            print "\t".encode("utf-8").join([title, url, author, page])
            # print ""

    def output_to_raw_file(content):
        for item in content:
            print ""
            # title
            print "Title:", item.find(class_="title").text
            # DOI URL
            print "URL:", item.find(lambda s: s.name == "a" and
                                    s.has_attr("itemprop") and s['itemprop'] == "url")["href"]
            Authors = [tag.text.encode("utf-8") for tag in item.find_all(
                              lambda s: s.name == "span" and not s.has_attr("class")
                              and s.has_attr("itemprop") and s['itemprop'] == "name")]
            print(",".encode("utf-8").join(Authors))
            print "Page:", item.find(lambda s: s.name == "span" and
                                    s.has_attr("itemprop") and s['itemprop'] == "pagination").string
            print ""

    url = "http://dblp.uni-trier.de/db/conf/cluster/cluster2013.html"
    r = requests.get(url)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    content = soup.find_all(what_i_want)  # get session sector
    output_to_excel(content)


def crawl_2015_office():
    def what_i_want(tag):
        return tag.name == "div" and tag.has_attr('id') \
            and tag['id'].startswith("session")

    def output_to_excel(content):
        print "Session\tTitle\tAuthor"
        for item in content:
            session = item.next_sibling.next_sibling.find("strong").text.encode("utf-8")
            papers = item.next_sibling.next_sibling.next_sibling.next_sibling
            for paper in papers.find_all("li"):
                title = paper.find("strong").text.replace("\n", "").encode("utf-8")
                authors = paper.find("em").text.encode("utf-8")
                print "\t".encode("utf-8").join([session, title, authors])

    url = "http://www.mcs.anl.gov/ieeecluster2015/conference-program/technical-program/"
    r = requests.get(url)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    content = soup.find_all(what_i_want)  # get session sector
    output_to_excel(content)

def count_university_author():
    path = "G:\KuaiPan\Research\ByConferenceOrJournal\Conference\Cluster\\2015\info.md"
    universities_map = {}
    with open(path) as f:
        content = f.readlines()
    for i, line in enumerate(content):
        if (i-2) % 4 == 0:
            line = line.strip()
            university_list = line.split(", ".encode("utf-8"))
            for university in university_list:
                if university in universities_map:
                    universities_map[university] += 1
                else:
                    universities_map[university] = 1

    for k in universities_map:
        print k + "\t".encode("utf-8") + str(universities_map[k])


def count_university_paper():
    path = "G:\KuaiPan\Research\ByConferenceOrJournal\Conference\Cluster\\2015\info.md"
    universities_map = {}
    with open(path) as f:
        content = f.readlines()
    for i, line in enumerate(content):
        if (i-2) % 4 == 0:
            line = line.strip()
            university_list = line.split(", ".encode("utf-8"))
            university_list = set(university_list)
            for university in university_list:
                if university in universities_map:
                    universities_map[university] += 1
                else:
                    universities_map[university] = 1

    for k in universities_map:
        print k + "\t".encode("utf-8") + str(universities_map[k])

if __name__ == "__main__":
    count_university_paper()