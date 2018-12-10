#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : dytt_crawler.py
@Author: Wesley
@Date  : 2018/11/29 16:19
@Desc  : 
'''
import requests, bs4, re

url = 'https://www.dytt8.net/index.htm'

print("forward to page %s ..." % url)
response = requests.get(url)
response.encoding = "GBK"
print(response.text)

soup = bs4.BeautifulSoup(response.text, "lxml")
# print(soup.text)
comic = soup.find_all("a")
print(comic[0].getText())
# number = re.findall("\d+", comic[0].getText())
# if number == []:
#     print('The end.')
#     break;
# else:
#     url = 'http://www.heibanke.com/lesson/crawler_ex00/' + number[0]  # 拼接新地址
