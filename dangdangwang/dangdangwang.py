import requests
import re
from bs4 import BeautifulSoup as BS
import json

def get_info(page):
    url="http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"+str(page)
    response=requests.get(url)
    assert response.status_code==200
    info=response.text  #请求成功拿到源代码
    return info

def get_parse(info):
    soup=BS(info,'lxml')
    item=soup.find_all('ul',class_='bang_list clearfix bang_list_mode')
    item_=item[0]
    books=item_.find_all('li')
    book_list=[]
    #book_dict={}
    for i in range(len(books)):
        book_dict={}
        divs=books[i].find_all('div')
        #rank
        """
        这个不能用string,不然会多一个点
        """
        div0=str(divs[0])
        info=re.findall('\d+',div0)
        rank=int(info[0])
        #website
        website=divs[1].a['href']
        #five_stars_nums
        """
        divs[6].span
        div6=str(divs[6].span)
        info6=re.findall('\d+',div6)
        five_stars_nums=int(info6[0])
        感觉脑子瓦特了,居然没想到用string
        """
        five_stars_nums=divs[6].span.string
        #price
        price=divs[7].p.span.string
        #title
        title=divs[1].a.img['alt']
        #img
        img=divs[1].a.img['src']
        #author
        author=divs[4].a['title']
        #re-rate
        re_rate=divs[3].find_all('span')[2].string
        book_dict.update({'rank':rank,'title':title,'img':img,'website':website,'author':author,'re-rate':re_rate,'five-stars-nums':five_stars_nums,'price':price})
        book_list.append(book_dict)
    return book_list

def write_data(item):
    with open('book.txt', 'a', encoding='UTF-8') as f:
       f.write(json.dumps(item, ensure_ascii=False) + 'n')
       f.close()


for i in range(1,26):
    info=get_info(i)
    item=get_parse(info)
    write_data(item)

