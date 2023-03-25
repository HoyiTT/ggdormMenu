import requests
from bs4 import BeautifulSoup

def makelist(url):
    # url = "http://www.ggdorm.or.kr/home/main_kr/main.php?ctt=../contents_kr/m_5_5&mc=1|5|1"
    html = requests.get(url)
    # print(html.text)

    soup = BeautifulSoup(html.text, 'html.parser')
    # print(soup.select_one('table.foodMenuTable'))
    #m_5_5 > div
    title = soup.select('tbody > tr > td')
    print(title[0].text)
    return title

url1 = "http://www.ggdorm.or.kr/home/main_kr/main.php?ctt=../contents_kr/m_5_5&mc=1|5|1"
htmllist = makelist(url1)
