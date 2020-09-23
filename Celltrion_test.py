#맨뒤 페이지 구하기

#셀트리온
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'

with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')

# print(pgrr.prettify())
# print(pgrr.text)

    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]
    # print(last_page)

df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

for page in range(1, int(last_page) + 1):
    #page 숫자를 이용하여 요청할 URL페이지 수 변경
    page_url = '{}&page={}'.format(sise_url, page)

    #read_html() 함수로 읽은 한 페이지 분량 데이터를 df에 추가
    df = df.append(pd.read_html(page_url, header=0)[0])

df = df.dropna()
print(df)
