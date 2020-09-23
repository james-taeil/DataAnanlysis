#OHLC 캔들
# OHLC 는 Open-High-Low-Close를 나타내며 시가-고가-저가-종가를 의미한다.
# 차트는 OHLC 에 해당하는 네 가지 가격을 이용하여 일정 기간의 가격 변동을 표시한다.

#셀트리온
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from matplotlib import pyplot as plt

#맨 뒤 페이지 숫자 구하기
url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'

with urlopen(url) as doc:
    html = BeautifulSoup(doc, 'lxml')
    pgrr = html.find('td', class_='pgRR')
    s = str(pgrr.a['href']).split('=')
    last_page = s[-1]

#전체 페이지 읽어오기
df = pd.DataFrame()
sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

for page in range(1, int(last_page) + 1):
    page_url = '{}&page={}'.format(sise_url, page)
    df = df.append(pd.read_html(page_url, header=0)[0])

#차트 출력을 위해 데이터 프레임 구하기
df = df.dropna()
df = df.iloc[0:30]              #최근 데이터 30행 읽어온다.
df = df.sort_values(by='날짜')   #네이버 금융의 데이터가 내림차순이서 오름차순으로 변경

#날짜, 종가 컬럼으로 차트 그리기
plt.title("Celltrion (close)")
plt.xticks(rotation=45)                    #x 축 레이블의 날짜가 겹쳐서 90도로 회전하여 표시
plt.plot(df['날짜'], df['종가'], 'co-')      #x축은 날짜 데이터, y축은 종가데이터, co는 좌표를 cyen원, -는 실선
plt.grid(color='gray', linestyle='--')
plt.show()

