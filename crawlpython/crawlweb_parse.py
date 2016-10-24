#coding=utf-8
'''

@author: yuyue
'''
from bs4.builder import HTML
from bs4 import BeautifulSoup
from IPython.core.display import Image
import requests
import re
import urllib2
import cookielib
import os
'''
爬取百度的首页图片，并保存
'''
def dowloadpic(url):
    cj=cookielib.LWPCookieJar()
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    req=urllib2.Request(url)
    operate=opener.open(req)
    data=operate.read()
    file=open("D:\\crawlpic\\"+'123.png', "wb")
    file.write(data)
    file.flush()
    file.close()
header= {
'Cookie': 'BAIDUID=9774D643CD616BE36542FDE52BBA9820:FG=1; BIDUPSID=9774D643CD616BE36542FDE52BBA9820; PSTM=1474790982; BDUSS=1NUMm1hWWF6d04xYXc5dmk5bFdzOWZ5WnIxS0VPWVVYbkNlTVRWZy1LWXIxeEpZQVFBQUFBJCQAAAAAAAAAAAEAAACIfzJR0dexsdTawrfJzwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACtK61crSutXY; pgv_pvi=2211893248; MCITY=-75%3A; BDSFRCVID=vq8sJeCCxG3ms8biBEA4Juj1x6iP0hRAnBIw3J; H_BDCLCKID_SF=tRk8oIDaJCvje5r1MtQ_M4F_qxby26nq-RbeaJ5n0-nnhn6Re-5ELxLFj-6tajoOJD5Tonn40RrIOt0Ry66jK4JKjaLOJj5P; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_645EC=c5de5LtzlBZ%2Fbo15%2Btav5UmviGu6sDXM9ysDkA9zzkPWp73QS21fXPLiAzD26fGEPgLj; BD_CK_SAM=1; PSINO=3; BD_HOME=1; H_PS_PSSID=1456_18240_21081_18560_17001_21407_21042_21378_21190_21373; BD_UPN=12314353; sugstore=0',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
         }

url= 'https://www.baidu.com/'
wb_data = requests.get(url,headers = header)


Soup = BeautifulSoup(wb_data.text,'lxml')
imgs = Soup.select('#s_lg_img')
pat = re.compile('(http.*g)')
img = re.findall(pat,str(imgs))
dowloadpic(img[0])
'''
爬取文章title和时间，以json存入
titles = Soup.select('  ul > li > a')
times = Soup.select('ul > li > span')
for title,time in zip(titles,times):
    data = {
        'title':title.get_text(),
        'time':time.get_text(),
    }
    print data
'''
