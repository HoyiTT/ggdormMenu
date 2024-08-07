﻿# 경기도 기숙사 오늘의 메뉴

## 개발 배경

상대적으로 불편한 식단표 확인 UI를 보며 직관적인 UX를 위해 개발하고자 함

## 서비스 목적

경기도 기숙사 사생들을 위한 간단한 식단표 확인

## 기능

* 당일 식단표 확인

* 주간 식단표 확인

* Webpush 알림 서비스 제공 - 현재 브라우저에서 모바일 알림 서비스를 제공하지만 잘 안되는 문제가 있음. 추후 개발 예정



## 기술 스택

* Server(GCP ec2(과거) -> AWS t2 micro(현재)를 활용한 저렴한 클라우드 서비스 활용)
  + 변경이유 -> GCP의 프리티어는 미국 리전을 사용하여 웹사이트 로딩속도가 너무 길다는 단점이 있었음. 그에 비해 AWS는 한국 리전 프리티어가 가능하기에 AWS로 서버를 교체함.    

* Flask

* BeautifulSoup을 활용한 웹사이트 크롤링 활용

* duckdns를 활용한 무료 dns 연결
  + 기존에는 DNS없이 바로 서버 IP로 접속하였지만 duckdns의 무료 DNS 서비스를 활용해 도메인을 설정하였음. 

* pwa로 구현하여 마치 앱처럼 사용
  + 기존에는 반응형 웹을 사용하였지만 PWA로 구현하여 웹 사이트지만 앱처럼구현
  * 접속 환경에 따라 다른 UI 제공


## 기대 효과

* 사생들의 보다 간단한 식단 확인

## 실행화면

### PC로 접속 시 
<img width="631" alt="컴퓨터" src="https://github.com/user-attachments/assets/c817a241-c6a9-464d-8d8a-7310b214e7d6">

### IOS Safari 접속 시
![IOS_Safari](https://github.com/user-attachments/assets/a3f48595-d3f3-440a-8ee0-793e56e87f28)

### IOS PWA 접속 시
![IOS_PWA](https://github.com/user-attachments/assets/8a263f81-7e37-4d7d-ad5a-6b9c4438a7eb)

## 링크

[http://ggdorm-menu.duckdns.org:5001/](http://ggdorm-menu.duckdns.org:5001/)
