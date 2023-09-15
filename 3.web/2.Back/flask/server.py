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

def getBreakfast(url,today):
    htmllist = makelist(url)
    if today == 6:
        today = 0
    else:
        today += 1
    return htmllist[(today*4)].text


def getLunch(url, today):
    htmllist = makelist(url)
    if today == 6:
        today = 0
    else:
        today += 1
    return htmllist[(today*4 + 1)].text

def getDinner(url, today):
    htmllist = makelist(url)
    if today == 6:
        today = 0
    else:
        today += 1
    return htmllist[(today * 4 + 2)].text
    
def getSnack(url, today):
    htmllist = makelist(url)
    if today == 6:
        today = 0
    else:
        today += 1
    return htmllist[(today * 4 + 3)].text

 
@app.route('/')
def index():
    url1 = "http://www.ggdorm.or.kr/home/main_kr/main.php?ctt=../contents_kr/m_5_5&mc=1|5|1"
    today = datetime.today().weekday()
    breakfast = getBreakfast(url1,today)
    lunch = getLunch(url1, today)
    dinner = getDinner(url1, today)
    snack = getSnack(url1, today)
    return render_template('index.html',todayBreakfast = breakfast,todayLunch = lunch, todayDinner = dinner, todaySnack = snack)


@app.route('/nextday')
def ndextday():
    url1 = "http://www.ggdorm.or.kr/home/main_kr/main.php?ctt=../contents_kr/m_5_5&mc=1|5|1"
    today = datetime.today().weekday() + 1
    if today == 7:
        today = 0
    breakfast = getBreakfast(url1, today)
    lunch = getLunch(url1, today)
    dinner = getDinner(url1, today)
    snack = getSnack(url1, today)
    return render_template('index.html',todayBreakfast = breakfast,todayLunch = lunch, todayDinner = dinner, todaySnack = snack)
 
 
app.run(debug=True)


    

