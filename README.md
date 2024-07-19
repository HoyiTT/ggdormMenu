# flask-pwa

https://github.com/andreinwald/webpush-ios-example/tree/75a4e707046ebf7f3b88cc1bbbb8aedecc4cf377
https://github.com/Trigo93/flask_pwa_example/tree/main
위 두개의 레포지터리를 참고하여 개발중인 프로젝트

PWA를 이용해 기숙사 식단표 알림 서비스 개발이 최종 목표

## 사용 기술
- Flask
- render_template,send_file


## 현재 구현 사항

+ 접속 환경별 다른 UI제공
    - PC - > 모바일 접속 안내 qr 제공
    - 모바일(브라우저) - > PWA로 설치를 위한 안내 메세지 제공
    + 오늘의 메뉴 PWA로 이식완료
    - 모바일(PWA) -> 경기도 기숙사 식단표 페이지 출력


## 추후 구현 예정 사항
+ 웹 아이콘 변경
+ web push 기능 구현(매일 저녁 내일 식단 알림 제공)
+ 다크 모드 지원


