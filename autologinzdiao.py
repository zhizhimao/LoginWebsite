#!/usr/bin/python
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
程序名：autologinzdiao.py

登陆中调网 http://www.zdiao.com/
模拟浏览器登录输入验证码10后自动登录获取cookie
通过id定位元素：find_element_by_id(“id_vaule”)
通过name定位元素：find_element_by_name(“name_vaule”)
通过tag_name定位元素：find_element_by_tag_name(“tag_name_vaule”)
通过class_name定位元素：find_element_by_class_name(“class_name”)
通过css定位元素：find_element_by_css_selector();用css定位是比较灵活的
通过xpath定位元素：find_element_by_xpath(“xpath”)
通过link定位：find_element_by_link_text(“text_vaule”)或find_element_by_partial_link_text()*
"""
from selenium import webdriver
import time
import requests
from lxml import etree

browser_opt = webdriver.ChromeOptions()  # 设置是否开启浏览器
browser_opt.set_headless()

browser = webdriver.Chrome()  # 此参数不开启浏览器 chrome_options=browser_opt webdriver.Chrome(chrome_options=browser_opt)
browser.set_page_load_timeout(10)   # 防止页面加载个没完等待时间10s


def get_cookie():
    # 获取cookie
    login_url = 'http://www.zdiao.com/login.asp'
    browser.get(login_url)  # 打开登录网页
    user = browser.find_element_by_id('username')  # 审查元素username的id
    user.clear()  # 清空用户栏中内容
    user.send_keys("xxx")  # 输入账号
    passwd = browser.find_element_by_id('password')  # 审查元素username的id
    passwd.clear()
    passwd.send_keys("xxx")  # 输入密码
    yan = browser.find_element_by_id("yan")  # 审查元素username的id
    yan.clear()
    time.sleep(10)  # 等待10秒输入
#    yan_code = input('输入验证码：')
#    yan.send_keys(yan_code)  # 输入验证码
    bt = browser.find_element_by_name('bt')  # name定位元素
    bt.click()  # 点击登录
    browser.get('http://www.zdiao.com/')  # 打开首页
#    browser.execute_script("return navigator.userAgent")  # 查看User-Agent
    cookie = "; ".join([item["name"] + "=" + item["value"] for item in browser.get_cookies()])  # 取得cookie 复制到headers = {'Cookie': 'landcode=AB7CAC13%2D9045%2D4DE2%2D9562%2D551598732FDE; ASPSESSIONIDQACBDDTC=GLMABDEDMPHEJOHCMLHAPLCM; Hm_lvt_7ddacf66134d1ba13d31392486ada51e=1537186916; Hm_lpvt_7ddacf66134d1ba13d31392486ada51e=1537186926'}
#    browser.get_cookies()  # 查看cookie
    browser.page_source  # 获取登录后网页源码
    return cookie


def check_cookie():
    # 验证获取的cookie是否正常登陆
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.4467.400 QQBrowser/10.0.424.400',
           'Cookie': cookie}
    url = 'http://www.zdiao.com/u/member.asp'
    response = requests.get(url, headers=headers)
    response.encoding = response.apparent_encoding  # 识别编码
    html = response.text
    page = etree.HTML(html)
    title = page.xpath('/html/body/div[1]/div[11]/a/text()')
    print(title)


cookie = get_cookie()
browser.quit()  # 关闭浏览器
check_cookie()
