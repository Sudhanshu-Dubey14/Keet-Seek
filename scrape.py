import time
import os
from bs4 import BeautifulSoup
from selenium import webdriver
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "ibm IEFC622I"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    if j.startswith("https://www.ibm.com/support/knowledgecenter"):
        print(j)
        link = j
        break
os.environ['MOZ_HEADLESS'] = '1'
browser = webdriver.Firefox()
browser.get(link)
time.sleep(5)
main_page = browser.page_source
main_soup = BeautifulSoup(main_page, 'lxml')
iframe = main_soup.find("iframe", class_="kc-iframe")
print(iframe)
browser.switch_to.frame(iframe["name"])
html = browser.page_source

# page = requests.get(link)
"""
with open("html_file.html") as html:
    page = html.read()
"""
# print(html)
soup = BeautifulSoup(html, 'lxml')
body = soup.find("div", class_="msgBody")
print(body)
for child in body.descendants:
    if child.name == "h4":
        print("\n" + child.string)
    elif child.name == 'p':
        print(child.string.rjust(80))
browser.close()
