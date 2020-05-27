#%%
import matplotlib.pyplot as plt
import pandas as pd
import pymysql
# 设置中文显示和负号显示
#%%
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['SimHei'] 
mpl.rcParams['axes.unicode_minus'] = False
# 设置图形风格 
plt.style.use('ggplot')
#%%
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
plt.ylabel('How many times songs be played?') 
plt.plot(range(len(chart1['list_count'])),chart1['list_count'])
plt.show()

# %%
df.sort_values('list_collect',ascending=False).drop_duplicates('listname').head()

# %%
chart2 = df.sort_values('list_collect',ascending=False).drop_duplicates('listname') 
plt.figure(figsize=(14,6))
plt.title('collection curve')
plt.xlabel('rank')
plt.ylabel('How many times songs be collected?') 
plt.plot(range(len(chart2['list_collect'])),chart2['list_collect']) 
plt.show()

# %%
df.groupby('sauthor')['sname'].count().reset_index().sort_values('sname',ascending= False)
# %%
df.groupby('sname')['listname'].count().shape

# %%
df.groupby('sname')['listname'].count().reset_index().sort_values('listname',ascending=False)

# %%
chart3 = df.groupby('sname')['listname'].count().reset_index().sort_values('listname',ascending=False).head(10)
x = range(len(chart3))
plt.figure(figsize=(14,8))
plt.title('歌单收录歌曲 TOP10') 
plt.barh(x,chart3['listname'],color='dodgerblue') 
plt.yticks(x,chart3['sname'])
plt.show()

# %%
df['list_count'].corr(df['list_collect'])

# %%
plt.figure(figsize=(14,8)) 
plt.title('歌单播放次数与收藏次数相关散点图') 
plt.xlabel('播放次数')
plt.ylabel('收藏次数') 
plt.scatter(df['list_count'],df['list_collect'],alpha=0.8) 
plt.show()
 

# %%
df.head()

# %%
df.groupby('list_tage')['listname'].count().shape
#%%
cates = df.sort_values('list_collect',ascending=False).drop_duplicates('listname') 
cates.groupby('list_tage')['listname'].count().reset_index().sort_values('listnam e',ascending=False)