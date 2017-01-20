#!/usr/bin/env python
#coding:utf-8

from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import time
import cookielib
import urllib2

root_url_one = "http://m.wufazhuce.com/one?page="
all_list = []

"获取每个列表页面的url"
def get_url_lists(num):
    url = []
    for i  in range(num):
        url.append(root_url_one + str(i))
    return url

"从每个列表页面获取10个图片和10个url对应存储"
def get_data(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    img_list =  soup.select('.item-picture-img ')
    word_list = soup.select(".text-content-short")
    for i in range(10):
        one_word_pic = {"url":img_list[i].get('src'),"word":word_list[i].get_text()}
        all_list.append(one_word_pic)
  
"将数据存储到mongo"
def save_to_mongo():
    pass

"将图片下载到本地"
def dowloadpic(url,j):
    cj=cookielib.LWPCookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    req=urllib2.Request(url)
    operate=opener.open(req)
    data=operate.read()
    "分割url名字可作为jpg的命名为，pic_name[3]"
    pic_name = url.split('/')
    file=open("D:\\crawlpic\\one\\"+ str(j)+".jpg", "wb")
    file.write(data)
    file.flush()
    file.close()
    

def main():
    j = 0
    start = time.time()
    url_all = get_url_lists(10)
    for i in url_all:
        get_data(i)
    end = time.time()
    print "use: %2.f s" %(end - start)
    for i in all_list:
        dowloadpic(i.get('url'),j)
        j += 1
    
if __name__ == '__main__':
    main()