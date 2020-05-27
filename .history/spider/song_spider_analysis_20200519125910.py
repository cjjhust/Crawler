#%%
import pandas as pd
import matplotlib.pyplot as plt
# 设置中文显示和负号显示
from pylab import mpl 
mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['axes.unicode_minus'] = False
# 设置图形风格 
# ∂plt.style.use('ggplot')

import pymysql
conn = pymysql.connect(host='localhost',port=3306,user='root',password='12345678',db='song_spider',charset='utf8')
sql = "select * from songlist_details"

df = pd.read_sql(sql,conn)

#%%
df.head()

# %%
df['播放次数']=df['list_count].str[:-3]

# %%
df.dtypes
# %%
