# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium.webdriver import Chrome as Browser

__author__ = 'chenzhi'

"""
豆瓣“选电影”，页面底部有“加载更多”的一个按钮

初步尝试动态抓取页面

"""

URL = "http://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"


def extract_movies(max_page_num=5):
    browser = Browser()
    browser.get(URL)
    movies = {}
    while True:
        movie_list = browser.find_elements_by_class_name('item')
        for movie in movie_list:
            title = movie.find_element_by_tag_name("p").text.strip()
            rating = movie.find_element_by_tag_name("strong").text.strip()
            movies[title] = rating
        if max_page_num > 0:
            max_page_num -= 1
            if not have_more(browser):
                break
        else:
            break
    browser.close()
    return movies


def have_more(browser):
    try:
        # try button
        navigation = browser.find_elements_by_class_name('more')[0]
        navigation.click()
        print("have more")
        return True
    except Exception as e:
        # there is one next
        print e.message
        print("don't have more")
        return False

if __name__ == '__main__':
    rec_movies = extract_movies()
    for title in rec_movies:
        print title, rec_movies[title]
