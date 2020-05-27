#%%
import pandas as pd
import matplotlib.pyplot as plt
# 设置中文显示和负号显示
from pylab import mpl mpl.rcParams['font.sans-serif'] = ['SimHei'] mpl.rcParams['axes.unicode_minus'] = False
# 设置图形风格 plt.style.use('ggplot')

import pymysql
conn = pymysql.connect(host='localhost',port=3307,user='root',password='usbw',db='ba idu_songlist',charset='utf8')
sql = "select * from songlist_details"
 