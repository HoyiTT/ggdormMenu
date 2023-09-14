from flask import Flask, render_template
 
import requests
from bs4 import BeautifulSoup

from datetime import datetime

app = Flask(__name__)
 


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

def getBreakfast(url):
    htmllist = makelist(url)
    today = datetime.today().weekday()
    if today == 6:
        today = 0
    else:
        today += 1
    return htmllist[(today*4)].text


def getLunch(url):
    htmllist = makelist(url)
    today = datetime.today().weekday()
    if today == 6:
        today = 0
    else:
        today += 1
    return htmllist[(today*4 + 1)].text

def getDinner(url):
    htmllist = makelist(url)
    today = datetime.today().weekday()
    if today == 6:
        today = 0
    else:
        today += 1
    return htmllist[(today * 4 + 2)].text
    
def getSnack(url):
    htmllist = makelist(url)
    today = datetime.today().weekday()
    if today == 6:
        today = 0
    else:
        today += 1
    return htmllist[(today * 4 + 3)].text

 
@app.route('/')
def index():
    url1 = "http://www.ggdorm.or.kr/home/main_kr/main.php?ctt=../contents_kr/m_5_5&mc=1|5|1"
    today = str(datetime.today().weekday())
    breakfast = getBreakfast(url1)
    lunch = getLunch(url1)
    dinner = getDinner(url1)
    snack = getSnack(url1)
    return render_template('index.html',todayBreakfast = breakfast,todayLunch = lunch, todayDinner = dinner, todaySnack = snack)
 
 
app.run(debug=True)


    

