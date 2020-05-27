#%%
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
# 设置中文显示和负号显示
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['axes.unicode_minus'] = False
# 设置图形风格 
# ∂plt.style.use('ggplot')

conn = pymysql.connect(host='localhost',port=3306,user='root',password='12345678',db='song_spider',charset='utf8')
sql = "select * from songlist_details"

df = pd.read_sql(sql,conn)

#%%
df.head()

# %%
df['list_count']=df['list_count'].map(lambda x: x[:-3])

# %%
df.dtypes
# %%
#df.drop(['播放次数'],axis = 1,inplace = True)
# %%
df.shape
# %%
df['list_count']=df['list_count'].astype('int')
df['list_collect']=df['list_collect'].astype('int')
# %%
#最高播放次数的歌单
df.sort_values('list_count',ascending=False).drop_duplicates('listname').head()

# %%
chart1 = df.sort_values('list_count',ascending=False).drop_duplicates('listname') 
plt.figure(figsize=(14,6))
plt.title('Playlist curve')#百度歌单播放次数曲线
plt.xlabel('rank')
plt.ylabel('How many times songs played?') 
plt.plot(range(len(chart1['list_count'])),chart1['list_count'])
plt.show()

# %%
df.sort_values('list_collect',ascending=False).drop_duplicates('listname').head()

# %%
chart2 = df.sort_values('list_collect',ascending=False).drop_duplicates('list_name') 
plt.figure(figsize=(14,6))
plt.title('百度歌单收藏次数曲线')
plt.xlabel('排名')
plt.ylabel('收藏次数') 
plt.plot(range(len(chart2['收藏次数'])),chart2['收藏次数']) 
plt.show()