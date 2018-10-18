# -*- coding: utf-8 -*-
"""
创建时间：Sun Aug  5 09:42:55 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：autologin51job.py

自动登录前程无忧
"""

import requests
from lxml import etree

url = 'http://www.51job.com/'
login_url = 'https://login.51job.com/login.php?url='
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4467.400 QQBrowser/10.0.424.400'}

form_data = {'action': 'save',
             'from_domain': 'i',
             'loginname': 'xxx',  # 登录名
             'password': 'xxx'  # 密码
             }

session = requests.Session()
session.get(url)
session.post(url=login_url, data=form_data, headers=header)
response = session.get(url, headers=header)
response.apparent_encoding  # 查看编码
response.encoding = response.apparent_encoding  # 设置为网页编码
html = response.text
page = etree.HTML(html)
title = page.xpath('/html/body/div[1]/div[1]/div/div[3]/ul/li[1]/a/text()')
print(title)
