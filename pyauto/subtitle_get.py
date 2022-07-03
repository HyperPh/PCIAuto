"""字幕爬取，请把代码中的todo替换掉"""
import threading
from queue import Queue
import time
import os
import requests
from lxml import etree as et
import random
import urllib.parse
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0'}

proxy=None


base_url = 'https://assrt.net'  
base_dir = 'YourPath'  # todo 下载路径

link_numbers = [0, 0]  

failed_url=[]
exist_url=[]


def find_not_exist_name(file_name):
    """从file_name开始找,直到找到filename (2)这样的不存在的文件名为止。已经添加到PCILib中"""
    if not os.path.exists(file_name):
        return file_name
    i = 1
    file_name_prefix, file_name_suffix = os.path.splitext(file_name)
    while os.path.exists(file_name_prefix + f' ({i})' + file_name_suffix):
        i += 1
    file_name_new = file_name_prefix + f' ({i})' + file_name_suffix
    return file_name_new


def savePic(pic_url, ignore_exist=False):
    """保存图片(下载文件)"""

    arr = pic_url.split('/')
    
    file_name = base_dir + urllib.parse.unquote(arr[-1])
    print(file_name)
    
    

    if ignore_exist and os.path.exists(file_name):
        exist_url.append(pic_url)
        print("文件已存在")
        return

    try:
        response = requests.get(url=pic_url, headers=headers,proxies=proxy)
    except Exception:
        try:
            
            pic_url = pic_url.replace('https', 'http')
            response = requests.get(url=pic_url, headers=headers,proxies=proxy)
        except Exception as e:
            print("未知错误,可能是网络连接失败", e)  
            return


    
    code1 = response.status_code
    if code1 != 200:
        failed_url.append(pic_url)
        print(f"Failed to download {pic_url}")
        return
    

    
    try:
        file_name = find_not_exist_name(file_name)
        with open(file_name, 'wb') as fp:
            for data in response.iter_content(128):
                fp.write(data)
    except OSError:
        print(f"文件名错误或太长:{file_name}")
        failed_url.append(pic_url)


def get_detail_html(detail_url_list, thread_id):
    """爬取文章详情页，消费者线程"""
    while True:
        url = detail_url_list.get()  
        try:
            response = requests.get(url=url, headers=headers,proxies=proxy)
        except Exception as ex:
            print("未知错误,可能是网络连接失败", ex)
            if detail_url_list.qsize() == 0:  
                return
            else:
                continue

        
        code = response.status_code
        if code == 200:
            html = et.HTML(response.text)
            
            r = html.xpath('//div[@class="download"]/a[@class="waves-effect waves-button waves-input-wrapper"]/@href')
            
            

            font_baidupan=html.xpath('//intro/d/@onclick')
            intro=html.xpath('//intro/text()')
            for f1 in font_baidupan:
                pan1=re.findall(r'(http.+)"\)',f1)
                for p1 in pan1:
                    p1=urllib.parse.unquote(urllib.parse.unquote(p1))
                    link_numbers[1]+=1
                    print(f"百度网盘字体链接数:{link_numbers[1]}")
                    print(f'\033[1;34;47m{p1}\033[0m')  
                    print(intro)
            if intro.find("lanzou")>=0:
                print(intro)

            for r1 in r:
                pic_url = base_url + r1
                link_numbers[0] += 1
                print(f"\n下载链接数:{link_numbers[0]}")
                print(pic_url)
                savePic(pic_url)
        if detail_url_list.qsize() == 0:  
            break


def get_detail_url(queue, fan_list):
    """爬取文章列表页，生产者线程"""
    
    
    for i in range(0, len(fan_list)):
        
        
        page_url = base_url + '/sub/?searchword=' + fan_list[i]
        

        try:
            response1 = requests.get(url=page_url, headers=headers,proxies=proxy)
        except Exception as ex:
            print("未知错误,可能是网络连接失败", ex)
            continue

        
        code1 = response1.status_code
        titles=list()
        if code1 == 200:
            html1 = et.HTML(response1.text)
            titles = html1.xpath('//div[@class="sublist_box_title"]/span[@class="sublist_box_title_l"]/a[@class="introtitle"]/@href')
        else:
            continue

        for title1 in titles:
            title_url=base_url+title1
            queue.put(title_url)
            print("put page url {id} end".format(id=title_url))  

        
        max_page=len(html1.xpath('//div[@class="pagelinkcard"]/a'))-2
        for k in range(2,max_page+1):
            
            page_url = base_url + '/sub/?searchword=' + fan_list[i] + f'&page={k}'
            

            try:
                response1 = requests.get(url=page_url, headers=headers,proxies=proxy)
            except Exception as ex:
                print("未知错误,可能是网络连接失败", ex)
                continue

            
            code1 = response1.status_code
            titles = list()
            if code1 == 200:
                html1 = et.HTML(response1.text)
                titles = html1.xpath('//div[@class="sublist_box_title"]/span[@class="sublist_box_title_l"]/a[@class="introtitle"]/@href')
            else:
                continue

            for title1 in titles:
                title_url = base_url + title1
                queue.put(title_url)
                print("put page url {id} end".format(id=title_url))  


def run(fan_list):
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    print(f"{headers=},{proxy=}")
    detail_url_queue = Queue(maxsize=1000)  
    
    thread = threading.Thread(target=get_detail_url, args=(detail_url_queue,fan_list,))
    html_thread = []
    
    for i in range(20):
        thread2 = threading.Thread(target=get_detail_html, args=(detail_url_queue, i,))
        html_thread.append(thread2)  
    start_time = time.time()
    
    thread.start()
    for i in range(20):
        html_thread[i].start()
    
    thread.join()
    for i in range(20):
        html_thread[i].join()

    print("以下已存在:")
    for url1 in exist_url:
        print(url1)
    print("以下失败:")
    for url1 in failed_url:
        print(url1)
    print("运行时间: {} s".format(time.time() - start_time))  


if __name__ == "__main__":
    fan_list1=[]
    run(fan_list1)
