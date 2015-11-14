# -*- coding: utf-8 -*-
from __future__ import unicode_literals
__author__ = 'chenzhi'


from selenium.webdriver import Chrome as Browser
from selenium.webdriver.common.by import By

_author__ = 'chenzhi'

"""

抓取动态内容

瀑布流式，滑倒页面底部就会加载更多

"""

BASE_URL = "http://www.mogujie.com/"

DEFAULT_NEXT_POSITION = 1000


def extract_hongren(max_page_num=5):
    suffix = "hongren"
    browser = Browser()
    browser.get(BASE_URL + suffix)
    items = {}
    while True:
        item_list = browser.find_elements_by_class_name('wall_item')
        for item in item_list:
            href = item.find_element(By.CSS_SELECTOR, ".pic_box.pic").get_attribute("href")
            desc = item.find_elements_by_class_name("desc")[0].text.strip()
            items[href] = desc
        if max_page_num > 0:
            max_page_num -= 1
            if not scroll_to_next(browser):
                break
        else:
            break
    browser.close()
    return items


def scroll_to_next(browser):
    try:
        template = "window.scrollTo(0,%d)"
        current = browser.execute_script("return window.scrollY;")
        print "current scroll position " + str(current)
        script = template % (int(current) + DEFAULT_NEXT_POSITION)
        browser.execute_script(script)
        return True
    except Exception as e:
        print(e.message)
        return False


if __name__ == '__main__':
    items = extract_hongren()
    for href in items:
        print href, items[href]