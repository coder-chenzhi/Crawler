__author__ = 'chenzhi'


def archive_to_endnote(path=None):
    """
    convert each paper to specific format which can be imported into endnote
    :param path: where result will be write to, if is None, output to console
    :return:
    """
    archive_page = "http://sigops.org/sosp/sosp15/archive/index.html"
    abstract_page = "http://sigops.org/sosp/sosp15/archive/abstracts.html"

    from bs4 import BeautifulSoup
    import requests

    r_abstract = requests.get(abstract_page)
    page_abstract = r_abstract.content
    soup_abstract = BeautifulSoup(page_abstract, "html.parser")

    def get_abstract(url):
        # print url
        index = url.split("#")[1]
        a_name = soup_abstract.find(lambda s: s.name == "a" and
                                    s.has_attr("name") and s['name'] == index)
        # print a_name
        abstract_div = a_name.nextSibling.nextSibling
        # print abstract_div
        return abstract_div.find("div", class_="abstract").text.strip()

    r = requests.get(archive_page)
    page = r.content
    soup = BeautifulSoup(page, "html.parser")
    papers = soup.find_all("div", class_="paper")
    for paper in papers:
        year = paper.find("div", class_="marker").text
        title = paper.find("div", class_="paperTitle").text.strip()
        authors = paper.find("div", class_="authors")
        if authors is None:
            continue
        else:
            authors = authors.text.strip()
        abstract = paper.find("div", class_="paperCopy").find(lambda s: s.name == "a" and
                                                              "Abstract" in s["title"])
        if abstract is None:
            continue
        else:
            abstract = "http://sigops.org/sosp/sosp15/archive/" + abstract['href']
            abstract = get_abstract(abstract)
        acm = paper.find("div", class_="paperCopy").find(lambda s: s.name == "a" and
                                                         "ACM" in s["title"])
        if acm is not None:
            acm = acm["href"]
        print "%0 Conference Proceedings"
        print "%D", year
        print "%T", title
        for author in authors.split("\n"):
                print "%A", author
        print "%B", "SOSP", year
        print "%U", acm
        print "%X", abstract
        print "\n"


if __name__ == "__main__":
    archive_to_endnote()