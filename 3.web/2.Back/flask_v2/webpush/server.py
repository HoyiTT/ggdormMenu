from flask import Flask, render_template, request, jsonify
from pywebpush import webpush, WebPushException
import json

app = Flask(__name__)

# 메모리에 구독 정보를 저장하기 위한 간단한 저장소
subscriptions = []

# VAPID 키 (안전하게 생성 및 저장되어야 함)
VAPID_PRIVATE_KEY = 'MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgoFJghU+9ynIf5e7A91ZNaCfkpOrrmeMsuLIPtNoTCjGhRANCAASgkhrLT4rblVqc93mqq+BBTgTgP7x77nkHme5MDVD7V7kFx52hLnJbpojb1+ZC7TbKBIWlF7mToXHheFhSv8Fr'
VAPID_CLAIMS = {
    "sub": "mailto:pjs9177@naver.com"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    subscription = request.json
    subscriptions.append(subscription)
    return jsonify(success=True), 200

@app.route('/push', methods=['POST'])
def push():
    message = request.json.get('message', 'Hello, World!')
    for subscription in subscriptions:
        try:
            response = webpush(
                subscription_info=subscription,
                data=json.dumps({"title": "New Message", "body": message}),
                vapid_private_key=VAPID_PRIVATE_KEY,
                vapid_claims=VAPID_CLAIMS
            )
        except WebPushException as ex:
            return jsonify(success=False, error=str(ex)), 500
    return jsonify(success=True), 200

if __name__ == '__main__':
    app.run(debug=True)
