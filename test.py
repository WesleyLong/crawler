#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : test.py
@Author: Wesley
@Date  : 2018/11/29 16:34
@Desc  : 
'''
import requests, bs4

url = 'https://www.baidu.com'
response = requests.get(url)
response.encoding = "utf-8"
# print(response.text)
soup = bs4.BeautifulSoup(response.text, "lxml")
print(soup.text)
comic = soup.find_all("a", attrs={"class": "mnav"})
# for a in comic:
#     print(a.getText())
