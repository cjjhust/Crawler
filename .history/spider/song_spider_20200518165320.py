# coding:utf-8
import requests
from bs4 import BeautifulSoup
import pymysql
import json
from multiprocessing.pool import Pool
# 链接数据库
conn = pymysql.connect(host='localhost',port=3306,user='root',password='12345678',db='song',charset='utf8')
cursor = conn.cursor()