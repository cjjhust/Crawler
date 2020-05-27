import mechanize
def viewPage(url):
    browser = mechanize.Browser()
    brow.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    print(source_code)

viewPage('https://www.google.com/')