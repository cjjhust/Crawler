# coding:utf-8
import requests
from bs4 import BeautifulSoup
#url = 'http://www.lanrenmb.com/User/index.php/User/downLoad.html?type=downLoad&aid=7 230&url=http%3A%2F%2Fwww.lanrenmb.com%2Fshenghuofuwu%2Ffangchan%2F7230.html'
header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KH TML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
'Connection':'keep-alive',
'Accept-Language':'zh-CN,zh;q=0.8', 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0. 8',
}
proxy = {
'https':'https://125.123.153.131:3000',
222.93.72.121	8118
}
wbdata = requests.get('https://www.baidu.com/s?wd=ip',proxies=proxy,headers=header)
soup = BeautifulSoup(wbdata.content,'lxml')
ip = soup.select_one('table > tr > td > span.c-gap-right')
print(ip)