# coding:utf-8
import requests
from bs4 import BeautifulSoup
import pymysql
import json
from multiprocessing.pool import Pool
# 链接数据库
conn = pymysql.connect(host='localhost',port=3307,user='root',password='usbw',db='ba idu_songlist',charset='utf8')
cursor = conn.cursor()