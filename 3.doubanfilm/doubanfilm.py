import requests
import re
import json
from bs4 import BeautifulSoup as BS
import xlwt
import csv

def get_info(page):
    url="https://movie.douban.com/top250?start="+str(page*25)+"&filter="
    response=requests.get(url,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27"})
    assert response.status_code==200
    return response.text

def get_item(info):
    soup=BS(info,'lxml')
    films=soup.find_all('div',class_='item')
    return films

def get_list(films):
    #film_list=[]
    global n
    for film in films:
        #website
        website=film.a['href']
        #name
        name=film.a.img['alt']
        #img
        img=film.a.img['src']
        #rank
        rank=film.em.string
        #grades
        grades=film.find_all('span',class_='rating_num')[0].string
        #author
        author=film.p.contents[0]
        #abstract
        #if film.find_all('span',class_='inq') is not None:
        try:
            abstract=film.find_all('span',class_='inq')[0].string
        except:
            continue
        #else:
            #abstract="None"
        """
        print(website+' '+name+' '+img+' '+rank+' '+grades+' '+author)

        From this printing result it can be seen that the datas crawled were right.
        So the problem was the way to save datas into a excel.  
        """
        
        sheet.write(n,0,website)
        sheet.write(n,1,name)
        sheet.write(n,2,img)
        sheet.write(n,3,rank)
        sheet.write(n,4,grades)
        sheet.write(n,5,author)
        sheet.write(n,6,abstract)
        n+=1
        
        
       

book=xlwt.Workbook()
sheet=book.add_sheet('doubanfilm')
sheet.write(0,0,'website')
sheet.write(0,1,'name')
sheet.write(0,2,'img')
sheet.write(0,3,'rank')
sheet.write(0,4,'grades')
sheet.write(0,5,'author')
sheet.write(0,6,'abstract')
n=1





for page in range(10):
    info=get_info(page)
    films=get_item(info)
    get_list(films)
book.save('doubanfilm.xlsx')
    
