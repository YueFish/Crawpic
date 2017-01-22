#!/usr/bin/env python
#coding:utf-8
'''Tarin tickets query via command-line

Usage:
    tickets [-gdtkz] <from> <to> <date>
    
Options:
    -h,--help  显示帮助菜单
    -g         高铁
    -d         动车
    -t         特快
    -k         快速
    -z         直达

Example：
    tickets 南京 北京 2016-07-01
    tickets -d 南京 北京 2016-07-01
'''
from docopt import docopt
import requests
import json 
from prettytable import PrettyTable


url = "https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2017-02-02&leftTicketDTO.from_station=TSW&leftTicketDTO.to_station=CDW&purpose_codes=ADULT"

results = requests.get(url, verify = False)
# rows = results.json()
# print 
datas = results.json().get('data')

"通过doc获取cmd输入"
def get_commanline():
    """command-line interface"""
    arg = docopt(__doc__)
    print arg.get('<date>')
    print arg.get('<from>')
    print arg.get('<to>')
    
"车次信息"
def cli():
    headers = '车次 车站 时间 历时 商务 一等 二等 软卧 硬卧 软座 硬座 无座 备注'.split()

    pt = PrettyTable()
    pt._set_field_names(headers)
    for data in datas:
        pt.add_row((data.get('queryLeftNewDTO').get('train_no')[5:10],
                    '始发:%s\n到站:%s' %('土溪',data.get('queryLeftNewDTO').get('end_station_name').encode('utf-8')),
                    '%s\n%s'%('-----' if data.get('queryLeftNewDTO').get('arrive_time') =='24:00' else data.get('queryLeftNewDTO').get('start_time'), 
                              '-----' if data.get('queryLeftNewDTO').get('arrive_time') =='24:00' else data.get('queryLeftNewDTO').get('arrive_time')),
                    '-----' if data.get('queryLeftNewDTO').get('lishi') =='99:59' else data.get('queryLeftNewDTO').get('lishi'),
                    '5',
                    '6',
                    '7',
                    '8',
                    '9',
                    '10',
                    '11',
                    '12',
                    '13'))
     
    print(pt)
    

cli()