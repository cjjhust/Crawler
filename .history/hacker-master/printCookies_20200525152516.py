import mechanize
import random
from http import cookiejar
'''
on my mac, fails:
mechanize._response.httperror_seek_wrapper: HTTP Error 403: request disallowed by robots.txt
'''
user_agents=['Mozilla/4.0','FireFox/6.01','ExactSearch','Nokia7110/1.0']
def printCookies(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    index
    cookie_jar=cookiejar.CookieJar()
    #cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)

    for cookie in cookie_jar:
        print(cookie)

url = 'https://www.google.com'
printCookies(url)