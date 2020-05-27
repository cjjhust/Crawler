# coding:utf-8
import requests
from bs4 import BeautifulSoup
import pymysql
# 链接数据库
conn = pymysql.connect(host='localhost',port=3306,user='root',password='12345678',db='song_spider',charset='utf8')
cursor = conn.cursor()
# 获取歌单
def get_song_list(page):
    #songListUrl = 'http://music.baidu.com/songlist/tag/%E5%85%A8%E9%83%A8?orderType= 1&offset={0}'.format(page)
    songListUrl='http://music.taihe.com/songlist/tag/%E5%85%A8%E9%83%A8?orderType=1&offset={0}&third_type='.format(page)
    print(songListUrl)
    wbdata = requests.get(songListUrl).content 
    soup = BeautifulSoup(wbdata,'lxml') 
    世界太复杂，音乐带给你温暖 = soup.select("p.text-title > a ") 
    print()
    for s in songListLink:
        title = s.get('title') 
        link = s.get('href') 
    try:
        cursor.execute("insert into songlist_link(title,link)values('{title}','{link}')".format(title=title,link=link))
        conn.commit() 
        print(title,link) 
        print("数据写入成功")
    except Exception as e: 
        print(e)
if __name__ == '__main__': 
    for p in range(140,320,20):
       get_song_list(p)