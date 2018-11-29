#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : douban250.py
@Author: Wesley
@Date  : 2018/11/23 15:39
@Desc  :
'''
import requests, re
from bs4 import BeautifulSoup


def download_page(url):
    print(url)
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, "lxml")
    # print(soup.text)
    return soup


def parse_soup(soup):
    return_list = []
    # 利用 class 属性找到 grid
    grid = soup.find("ol", attrs={"class": "grid_view"})
    print(grid)
    # 不加 attrs= 也可以
    # grid = soup.find("ol", {"class": "grid_view"})
    if grid:
        # 利用标签获取 list
        movie_list = grid.find_all("li")
        # print(movie_list)
        # 遍历 list
        for movie in movie_list:
            # print(movie)
            # 一个电影有多个名字，这里只取第一个
            title = movie.find("span", attrs={"class": "title"}).getText()
            # print(title)
            rating_num = movie.find("span", attrs={"class": "rating_num"}).getText()
            inq = movie.find("span", attrs={"class": "inq"})
            # 利用 text 配合正则表达式匹配搜索文本
            rating_p = soup.find(text=re.compile('人评价$'))
            # 有些暂时没有一句话评论
            if not inq:
                inq = "暂无"
            else:
                inq = inq.getText()
            return_list.append(title + "，" + rating_p + "，评分：" + rating_num + "，一句话评价：" + inq)

        next_page = soup.find("span", attrs={"class": "next"}).find("a")
        if next_page:
            return return_list, next_page["href"]
        else:
            return return_list, None


if __name__ == "__main__":
    url = "https://movie.douban.com/top250"
    next_url = ""
    # 将结果保存到文件
    while next_url or next_url == "":
        soup = download_page(url + next_url)
        movie_list, next_url = parse_soup(soup)
        # 将 list 拆分成不同行
        # print(movie_list, "\t", next_url)
