#!/usr/bin/env python
#coding=utf-8
'''
'''
import re
from pprint import pprint
import json
import sys


with open("station_name.html", 'r') as f :
#     fw = open('stations.py','wb')
    text = f.read()
    print type(text)
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', text.decode('utf-8'))
    stations = dict(stations)
    for i in stations:
        print "%s : %s" % (i.encode('utf-8'),stations[i].encode('utf-8'))
    