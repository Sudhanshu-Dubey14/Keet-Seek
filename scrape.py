import time
import os
import traceback
import sys

from bs4 import BeautifulSoup
from selenium import webdriver
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


class color:
    BOLD = '\033[1m'
    END = '\033[0m'


def fetch_help(error_code):
    # to search
    query = "ibm " + error_code

    print("Searching web for error code: " + error_code, end="\r\r")
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        if j.startswith("https://www.ibm.com/support/knowledgecenter"):
            link = j
            break
    os.environ['MOZ_HEADLESS'] = '1'
    print("Loading web page: " + str(link))
    try:
        browser = webdriver.Firefox()
        browser.get(link)
        time.sleep(5)
        main_page = browser.page_source
        main_soup = BeautifulSoup(main_page, 'lxml')
        iframe = main_soup.find("iframe", class_="kc-iframe")
        browser.switch_to.frame(iframe["name"])
        html = browser.page_source

        soup = BeautifulSoup(html, 'lxml')
        body = soup.find("div", class_="msgBody")
        body_text = body.get_text()
        for h4 in body.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
            body_text = body_text.replace(h4.string,
                                          "\n" + color.BOLD + h4.string + color.END + "\n", 1)

        print(body_text)
    except Exception:
        print("Exception in user code:")
        print("-" * 60)
        traceback.print_exc(file=sys.stdout)
        print("-" * 60)
    finally:
        browser.close()
