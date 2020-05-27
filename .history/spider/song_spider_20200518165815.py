# coding:utf-8
import requests
from bs4 import BeautifulSoup
import pymysql
# 链接数据库
conn = pymysql.connect(host='localhost',port=3307,user='root',password='usbw',db='ba idu_songlist',charset='utf8')
cursor = conn.cursor()
# 获取歌单
def get_song_list(page):
songListUrl = 'http://music.baidu.com/songlist/tag/%E5%85%A8%E9%83%A8?orderType= 1&offset={0}'.format(page)
print(songListUrl)
wbdata = requests.get(songListUrl).content soup = BeautifulSoup(wbdata,'lxml') songListLink = soup.select("p.text-title > a ") for s in songListLink:
title = s.get('title') link = s.get('href') try:
cursor.execute("insert into songlist_link(title,link)values('{title}','{li nk}')".format(title=title,link=link))
conn.commit() print(title,link) print("数据写入成功")
except Exception as e: print(e)
if __name__ == '__main__': for p in range(0,320,20):
       get_song_list(p)