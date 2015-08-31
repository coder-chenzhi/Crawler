__author__ = 'chenzhi'

from util import get_page_count
from wap import Fetcher
from bs4 import BeautifulSoup

def get_all_conversation_url(msg_url):
    prefix = "http://weibo.cn"
    htmlContent = fetcher.fetch(msg_url, None, 5)
    page_count = get_page_count(htmlContent)
    print 'page_count', page_count
    soup = BeautifulSoup(htmlContent)
    valid_links = []
    all_links = [i.get("href") for i in soup.find_all("a", href=True)]
    for link in all_links:
        if link.startswith("/im/chat?uid="):
            valid_links.append(prefix + link)
    print valid_links

if __name__ == '__main__':
    username = "xx@xx.com"
    password = "xx"
    fetcher = Fetcher(username, password)
    fetcher.login(cookie_filename="cookie.txt")
    msg_url = 'http://weibo.cn/msg/?tf=5_010&vt=4'
    get_all_conversation_url(msg_url)