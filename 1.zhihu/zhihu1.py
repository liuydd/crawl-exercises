import requests
import json
import pymysql
from bs4 import BeautifulSoup as BS
import logging
import time
import re
url="https://www.zhihu.com/hot"
headers={
    "Cookie": "",
    "User-Agent": ""
  }
def get_board():
  hot_list=[]
  resp=requests.get(url,headers)
  if resp.status_code==200:
      soup=BS(resp.content,'lxml',from_encoding='utf-8')
      hots=soup.find_all('section',attrs={'class':'HotItem'})
      for hot in hots:
        hot_dict={}
        hot_title=hot.select('.HotItem-title')
        hot_heat=hot.select('.HotItem.metrics')
        hot_excerpt=hot.select('.HotItem-excerpt')
        hot_url=hot.find('a').get('href')
        hot_qid=re.findall(r"\d+",hot_url)
        hot_dict['title']=hot_title
        hot_dict['heat']=hot_heat
        hot_dict['excerpt']=hot_excerpt
        hot_dict['url']=hot_url
        hot_dict['qid']=hot_qid
        hot_list.append(hot_dict)
        #print(hot_list)
        return hot_list

def get_question():
  hot_question={}

  for 
    hot_question["created"]=
    hot_question["followerCount"]=
    hot_question["visitCount"]=
    hot_question["answerCount"]=
    hot_question["title"]=
    hot_question["raw"]=
    hot_question["hit_at"]=

  raise NotImplementedError
