#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 01.py
@Author: Wesley
@Date  : 2018/11/23 15:01
@Desc  :
'''
import requests, bs4, re

url = 'http://www.heibanke.com/lesson/crawler_ex00/'

while True:
    # download the page
    print("forward to page %s ..." % url)
    response = requests.get(url)
    print("the return code : " + str(response.status_code))

    soup = bs4.BeautifulSoup(response.text, "html.parser")

    # 获取页面数字
    comic = soup.select('h3')
    print(comic[0].getText())
    number = re.findall("\d+", comic[0].getText())
    if number == []:
        print('The end.')
        break;
    else:
        url = 'http://www.heibanke.com/lesson/crawler_ex00/' + number[0]  # 拼接新地址
