import mechanize
import random
from http import cookiejar
'''
on my mac, fails:
mechanize._response.httperror_seek_wrapper: HTTP Error 403: request disallowed by robots.txt
'''
user_agents=['Mozilla/4.0','FireFox/6.01','ExactSearch','Nokia7110/1.0']
url = 'https://www.baidu.com'
def printCookies(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    index=random.randrange(0,len(user_agents))
    browser.addheaders=[('User-agents',(user_agents[index]))]
    cookie_jar=cookiejar.CookieJar()
    #cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)

    for cookie in cookie_jar:
        print(‘)
        print(cookie)

for i in range(0,5):
    printCookies(url)