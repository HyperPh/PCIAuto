
import sys
import os
import re
import json
# import random
import urllib.parse
import time
# import threading
# from queue import Queue


import pandas as pd
# from bs4 import BeautifulSoup
# import requests
from lxml import etree as et

base_url='http://kisssub.org'  # todo 从kisssub网抓取磁力链接
# http://www.comicat.org
# http://www.kisssub.org


def find_not_exist_name(file_name):
    """从file_name开始找,直到找到filename (2)这样的不存在的文件名为止。已经添加到PCILib中"""
    if not os.path.exists(file_name):
        return file_name
    l = 1
    file_name_prefix, file_name_suffix = os.path.splitext(file_name)
    while os.path.exists(file_name_prefix + f' ({l})' + file_name_suffix):
        l += 1
    file_name_new = file_name_prefix + f' ({l})' + file_name_suffix
    return file_name_new


def read_text(path,encoding='utf-8'):
    with open(path,'r',encoding=encoding) as f:
        s=f.read()
    return s


def correct_caption(captions,search_keyword:list):
    if captions and search_keyword:
        correct=[]
        k = 0  # todo 第几个关键词
        s1 = ""
        for i in range(0,len(captions)):
            if captions[i].startswith('\n        ') and i>0:
                correct.append(s1)
                # k=0这样做有问题
                s1=captions[i].replace('\n        ','')
            elif i==0:
                s1=captions[i].replace('\n        ','')
            else:
                s1+=search_keyword[k]+captions[i]
                # k+=1这样做有问题，有些中间没有关键词却也是断开的
        correct.append(s1)

        return correct
    elif captions:
        correct = []
        s1 = ""
        for i in range(0, len(captions)):
            if captions[i].startswith('\n        ') and i > 0:
                correct.append(s1)
                s1 = captions[i].replace('\n        ', '')
            elif i == 0:
                s1 = captions[i].replace('\n        ', '')
            else:
                s1 += captions[i]
        correct.append(s1)

        return correct
    else:  # 标题列为空
        return captions


def html_to_csv(html_str):

    html1 = et.HTML(html_str)
    columns = html1.xpath('//*[@id="listTable"]/thead/tr/th/text()')
    columns.append('magnet')
    x=-1
    # print(columns)#['发表时间', '类别', '标题', '大小', '种子', '下载', '完成', 'UP主 / 代号', 'magnet']

    df1 = pd.DataFrame(columns=columns)

    keyword=html1.xpath('//*[@id="data_list"]/tr[1]/td[3]/a/span[@class="keyword"]/text()')
    print(f'{keyword=}')#keyword=['BDrip']

    t1 = html1.xpath('//*[@id="data_list"]/tr/td[1]/text()')
    t1=pd.Series(t1).apply(str.strip)
    # print(t1)
    df1[columns[1+x]]=t1

    t2 = html1.xpath('//*[@id="data_list"]/tr/td[2]/a/text()')
    df1[columns[2+x]]=t2

    t3 = html1.xpath('//*[@id="data_list"]/tr/td[3]/a/text()')
    # print(t3)
    # print(correct_caption(t3,keyword))
    df1[columns[3+x]] = correct_caption(t3,keyword)

    t4 = html1.xpath('//*[@id="data_list"]/tr/td[4]/text()')
    df1[columns[4+x]] = t4

    for i in range(5,8):
        df1[columns[i+x]] = html1.xpath(f'//*[@id="data_list"]/tr/td[{i}]/span/text()')

    df1[columns[8+x]] = html1.xpath('//*[@id="data_list"]/tr/td[8]/a/text()')

    magnet_list = []
    titles = html1.xpath('//tbody[@id="data_list"]/tr/td[3]/a/@href')
    for title1 in titles:
        # print(title1)
        title_url = base_url + '/' + title1
        hash1 = re.search(r"show-([0-9a-fA-F]+)\.html", title1)
        if hash1:
            l1 = f'magnet:?xt=urn:btih:{hash1.group(1)}&tr=http://open.acgtracker.com:1096/announce'
            magnet_list.append(l1)
    df1['magnet'] = magnet_list
    # print(df1)
    return df1


def html_to_json(html_str):
    magnet_dict = {}
    # todo
    return magnet_dict


def html_to_magnet(html_str):
    magnet_list=[]
    html1 = et.HTML(html_str)
    titles = html1.xpath('//tbody[@id="data_list"]/tr/td/a/@href')
    for title1 in titles:
        # print(title1)
        title_url = base_url + '/' + title1
        hash1=re.search(r"show-([0-9a-fA-F]+)\.html",title1)
        if hash1:
            l1=f'magnet:?xt=urn:btih:{hash1.group(1)}&tr=http://open.acgtracker.com:1096/announce'
            magnet_list.append(l1)
    # print(magnet_list)
    return magnet_list


def write_txt(magnet_list,path='./m1.txt',encoding='utf-8'):
    with open(path,'w',encoding=encoding) as f:
        for m in magnet_list:
            f.write(m)
            f.write('\n')


def write_json(fan_info:dict,path='./m1.json',encoding='utf-8'):
    with open(path, 'w', encoding=encoding) as f:
        json.dump(fan_info, f, indent=' '*4)


def write_csv(fan_info:pd.DataFrame,path='./m1.csv',encoding='utf-8',override=False):
    # fan_info.to_csv(path,header=False,index=False)
    if override:
        fan_info.to_csv(path, index=False)
    else:
        fan_info.to_csv(find_not_exist_name(path),index=False)


def csv_to_txt(path_csv,path_txt='./m1.txt',encoding='utf-8'):
    s=read_text(path_csv)
    m=re.findall(r'(magnet:\?xt=urn:btih:[0-9a-fA-F]+&tr=http://open.acgtracker.com:1096/announce)[\s,]',s)
    write_txt(m,path_txt,encoding)


if __name__ == '__main__':
    # 目前仅csv和txt可用
    start_time = time.time()
    # write_txt(html_to_magnet(read_text(r'D:\360极速浏览器下载\bdrip - 爱恋动漫BT下载.html')))
    # write_csv(html_to_csv(read_text(r'D:\360极速浏览器下载\爱恋动漫BT下载.html')))
    write_csv(html_to_csv(read_text(r"D:\360极速浏览器下载\漫猫动漫BT下载.html")))
    # write_csv(html_to_csv(read_text(r"D:\360极速浏览器下载\bd 1080p - 漫猫动漫BT下载.html")))


    # csv_to_txt('./m1 (1).csv')
    print(f"运行时间: {time.time() - start_time} s")
