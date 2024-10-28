# 만약 배민에서 음식을 고르려고 하는데
# 선택하기 힘들어 메뉴를 추천 기능을 이용
# 치킨, 피자, 분식, 중식
# 무작위(랜덤)
import random
print(random, random())

menu = '치킨','피자','분식','중식'
random.choice(menu)

import requests'
# 윈도우
./venv/Scripts/activate


# 맥
source venv/bin/activate
pip install bs4 beautifulsoup4

import requests
from bs4 import BeautifulSoup
 
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/index.htm',headers=headers)
 
soup = BeautifulSoup(data.text, 'html.parser')