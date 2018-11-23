#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File  : 02.py
@Author: Wesley
@Date  : 2018/11/23 15:16
@Desc  : 
'''
import requests

url = 'http://www.heibanke.com/lesson/crawler_ex01/'

playload = {'username': 'liuhaha', 'password': '1'}

for i in range(31):
    playload['password'] = i
    print(u'传入参数为：' + str(playload))

    r = requests.post(url, data=playload)

    if u"成功" in r.text:
        print(u'闯关成功！')
        break