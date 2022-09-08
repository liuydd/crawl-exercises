import requests
import json
import pymysql
from bs4 import BeautifulSoup as BS
import logging
import time
import re
url="https://www.zhihu.com/hot"
headers={
    "Cookie": "_zap=53c84654-175a-4274-8696-7fdf90bd893d; _xsrf=4aea7a95-d5d8-46f1-855d-19be4b67b0d9; d_c0=ABDYGJHShRWPTqK8pH3LD7_meuQBFhytzH0=|1662537930; captcha_session_v2=2|1:0|10:1662537930|18:captcha_session_v2|88:Q01EZmVxakZqWVBFRytMZFJ4MzA3ajlYcnFBUEZxM2RvektxR090dEN1TEJ3TWNJTGU3dFQ2QkQ0QmRWWXoxNg==|84034febdf70b76a5d32a559f0cd8b09c62615776439da371a93a79fb4357f1f; SESSIONID=9fehoKW9DxvEt2iti8fHNlAgtxSyBAchgeNhYm73qIH; JOID=VFsdAUszqNJJ3OKNYjfrhFNGNAt5D8W9I7Ws0VFx1a8GqtbhHfb5wi7f7IxqOslaZsQqHxBnEJ7oqoA_-iCVp2g=; osd=U18RBkI0rN5O1eWJbjDig1dKMwJ-C8m6KrKo3VZ40qsKrd_mGfr-yynb4ItjPc1WYc0tGxxgGZnspoc2_SSZoGE=; __snaker__id=hBjaejIrfWJwfFbv; gdxidpyhxdE=PNzW00f6CfLpjbfOJil5e1MhuudVhpn6oQejve0UMh2no2brZT7IxXXrqbPEG5NACZN3TZ%5C8828TRwP9VuQn7cxlKUHc0hiDpWwhjhYxJ8BrYtMkLxQs%2BILpER1JkGt%5CWgZn%5C5OKiUY0wZ3eyYbZSfyujDkyRG1yL550O%2BeO94v7tr%2BQ%3A1662538833647; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=aNH43ksoB1J4AiebEMcxKS1%2BVALjdc9niaBFZUxQQ7VJsyTQe%2FCdApxR5V6COeY8fnIH33bBCL5JHqQX%2Fo0vh3%2FAh6g37tMOIM7%2FA9kXW1ePzqz8Aov7XFRNfraWcV9Sbmo%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eedafb43a39eb684b274b8eb8aa3d84b929f8b86c559f396f893b73e8b9186d5fc2af0fea7c3b92aa39288d5b261b1b18ed2c94083b7ab83c847a1a885b4b421969f848be769fbb2a782c14e9a8bb8b2d43d9696bd9ad75ba7f18d85c47cbc8efbb7b5498dbb97d9e5668b98fdd4e14a8194fbabcb7b9388e190b37eacede1a2eb3ea5edf995d0458b93f9d0c433a98899d2e85cbaafb6d9c465b6e998a7d146a6aeafb8e25efb8dae8eee37e2a3; YD00517437729195%3AWM_TID=x71oIT647Z5BBRUEQVPFH1It65%2BZfY5z; z_c0=2|1:0|10:1662537983|4:z_c0|92:Mi4xZlF1S0x3QUFBQUFBRU5nWWtkS0ZGU1lBQUFCZ0FsVk5fNTRGWkFBLW1Pdm8yamprYVhxamZ0ZjFEQW4tVi0tTURR|1df95f5e40b808bc471f0b300c901fab8635174704d61bac9df5d74f88ee5f36; q_c1=6089a8f635414f3a9b8469bee2266e8b|1662537983000|1662537983000; NOT_UNREGISTER_WAITING=1; tst=h; KLBRSID=f48cb29c5180c5b0d91ded2e70103232|1662551460|1662547438",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
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
