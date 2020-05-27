# coding:utf-8
import requests
from bs4 import BeautifulSoup
import pymysql
import json
from multiprocessing.pool import Pool
# 链接数据库
conn = pymysql.connect(host='localhost',port=3306,user='root',password='12345678',db='song_spider',charset='utf8')
cursor = conn.cursor()
page_list = []
data = cursor.execute('select link from songlist_link')
for d in cursor.fetchall():
page_list.append(d[0]) print(d[0])
# 获取歌单详细信息