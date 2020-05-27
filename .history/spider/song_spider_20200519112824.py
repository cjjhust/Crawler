# coding:utf-8
import requests
from bs4 import BeautifulSoup
import pymysql
from multiprocessing.pool import Pool
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
    songListLink = soup.select("p.text-title > a ") 
    print('***',songListLink)
    for s in songListLink:
        print("%%",s)
        title = s.get('title') 
        link = s.get('href') 
        try:
            cursor.execute("insert into songlist_link(title,link)values('{title}','{link}')".format(title=title,link=link))
            conn.commit() 
            print(title,link) 
            print("数据写入成功")
        except Exception as e: 
            print(e)

def get_song_list_info(songListUrl): #
    try:
        url="http://music.taihe.com/"+songListUrl
        #url="http://music.taihe.com/songlist/5770"
        print("###"url)
        wbdata=requests.get(url).content
        soup=BeautifulSoup(wbdata,'lxml')
        #歌单名字
        list_name=soup.select('div.songlist-info-msg>h1')[0].get_text()
        print('list_name',list_name)
        # 创建者
        list_user = soup.find(name="span",class_="songlist-info-username").get_text().split(' ')[1]
        print('list_user',list_user)
        # 歌单标签
        listtags=''
        for i in soup.find('div',attrs={"class":"songlist-info-tag"}).find_all('a'):
            #print(i.get_text())
            listtags=str(i.get_text())+' '+listtags
       
        print("list_tags",listtags)
        
        # 播放次数
        list_count = soup.find(name="span",class_="songlist-listen").get_text()
        print('list_count',list_count)
        # 收藏次数
        list_collect = soup.find(name="em",class_="to collectNum").get_text()
        print('list_collect',list_collect)
        # 歌单歌曲
        #list_music = soup.select("div",class_='song-list-wrap').find_all('a',class_='songlist-songname').get_text()
        #for i in soup.find("div",class_='song-list-wrap').find_all('a',class_='songlist-songname'):
            #print(i.get_text().split()[0])
        for i in soup.find_all('li',class_="songlist-item clearfix"):
            sname=i.find('a',class_='songlist-songname').get_text().split()[0]
            sauthor=i.find('span',class_='singer').find('a').get_text()
            print(sname,sauthor)
            data={
                "list_name":list_name, 
                "list_user":list_user, 
                "list_count":list_count, 
                "list_collect":list_collect, 
                "list_tage":listtags, 
                "sname":sname, 
                "sauthor":sauthor,

            }
            cursor.execute("insert into songlist_details \
                (listname,list_user,list_count,list_collect,list_tage,sname,sauthor)\
                 values ('{list_name}','{list_user}','{list_count}','{list_collect}','{listtags}',\
                ' {sname}','{sauthor}')".format(list_name=list_name,list_user=list_user,list_count=list_count, \
                list_collect=list_collect,listtags=listtags,sname=sname,sauthor=sauthor))
            conn.commit()
            print(data)
        #print('list_music',list_music)
    except BaseException as e:
        print("程序运行出错:%s" % e)

if __name__ == '__main__':
    page_list=[]
    data=cursor.execute('select link from songlist_link')
    for d in cursor.fetchall():
        page_list.append(d[0])
        print(d[0])
    pool = Pool(processes=4)
    for pl in page_list:
        print("***",pl)
        pool.map_async(get_song_list_info,pl)
    pool.close()
    pool.join()
    cursor.close()
    conn.close()

    #get_song_list_info()
   # for p in range(0,120,20):
       #get_song_list(p)