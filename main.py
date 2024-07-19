from flask import Flask, render_template, request,send_file
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)


def fetch_menu(url, day_offset):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        menu_data = soup.select('tbody > tr > td')

        index = day_offset * 4
        breakfast = menu_data[index].text
        lunch = menu_data[index + 1].text
        dinner = menu_data[index + 2].text
        snack = menu_data[index + 3].text
        return breakfast, lunch, dinner, snack
    except requests.RequestException as e:
        return "데이터를 불러오는 데 실패했습니다.", "", "", ""
    except IndexError:
        return "데이터가 없습니다.", "", "", ""



@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')

@app.route('/static/sw.js')
def serve_sw():
    return send_file('static/sw.js', mimetype='application/javascript')


@app.route('/')
def index():
    days = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']
    day_offset = request.args.get('day', default=(int(datetime.today().weekday())+1) % 7, type=int)
    url = "http://www.ggdorm.or.kr/home/main_kr/main.php?ctt=../contents_kr/m_5_5&mc=1|5|1"
    breakfast, lunch, dinner, snack = fetch_menu(url, day_offset)
    todayDate = datetime.today().strftime('%Y-%m-%d')
    defaultdays = days[(int(datetime.today().weekday())+1) % 7]

    return render_template('index.html', days=days, day=day_offset, todayDate = todayDate, defaultdays = defaultdays, todayBreakfast=breakfast, todayLunch=lunch, todayDinner=dinner, todaySnack=snack)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

