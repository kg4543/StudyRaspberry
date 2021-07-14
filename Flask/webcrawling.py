from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

#검색 url
url = 'https://search.naver.com/search.naver?query=날씨'
html = req.get(url)
#pprint(html.text)
soup = bs(html.text, 'html.parser') #beutifulsoup로 제Dom

datas = soup.find('div', {'class' : 'detail_box'}) #미세먼지 영역
#pprint(finedust)
details = datas.findAll('dd') #요소 찾기
#print(details)

#미세먼지
finedust = details[0].find('span', {'class', 'num'}).get_text()
#초미세먼지
ultrafinedust = details[1].find('span', {'class', 'num'}).get_text()
#오존지수
ozone = details[2].find('span', {'class', 'num'}).get_text()

print('{0}, {1}, {2}'.format(finedust,ultrafinedust,ozone))