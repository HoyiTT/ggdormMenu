import requests
from bs4 import BeautifulSoup
from datetime import datetime

def makelist(url):
    # url = "http://www.ggdorm.or.kr/home/main_kr/main.php?ctt=../contents_kr/m_5_5&mc=1|5|1"
    html = requests.get(url)
    # print(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.select_one('table.foodMenuTable'))
    #m_5_5 > div
    title = soup.select('tbody > tr > td')
    # print(title[7].text)
    return title

def mgetBreakfast(url):
    htmllist = makelist(url)
    today = datetime.today().weekday()
    if today == 6:
        today = 0
    else:
        today += 1
    print(htmllist[(today*4)].text)

def getLunch(url):
    htmllist = makelist(url)
    today = datetime.today().weekday()
    if today == 6:
        today = 0
    else:
        today += 1
    print(htmllist[(today*4 + 1)].text)
    

url1 = "http://www.ggdorm.or.kr/home/main_kr/main.php?ctt=../contents_kr/m_5_5&mc=1|5|1"
htmllist = makelist(url1)
getBreakfast(url1)
