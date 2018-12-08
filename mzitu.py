#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from lxml import html
import os
from multiprocessing.dummy import Pool as ThreadPool
def header(referer):
    headers = {
        # 'Host': 'i.meizitu.net',
        # 'Pragma': 'no-cache',
        # 'Accept-Encoding': 'gzip, deflate',
        # 'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        # 'Cache-Control': 'no-cache',
        # 'Connection': 'keep-alive',
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) '
        #               'Chrome/59.0.3071.115 Safari/537.36',
        # 'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers
if __name__ == '__main__':
    jpgLink = 'https://i.meizitu.net/2018/12/07a01.jpg'
    headers = header(jpgLink)
    print(headers)
    print(requests.get(jpgLink, headers=header(jpgLink)).content)
    filename = '%s/%s.jpg' % ('E:/picture/mzitu', '2')
    with open(filename, "wb+") as jpg:
        jpg.write(requests.get(jpgLink, headers=header(jpgLink)).content)
