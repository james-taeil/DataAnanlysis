#사용법
# mpf.plot(OHCL 데이터프레임  [, title=차트제목] [, type=차트형태] [, mav=이동평균선]
# [, volume=거래량 표시여부] [, ylabel=y 축 레이블])


import mplfinance as mpf
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

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
    if page % 10 == 0:
        print('현재 페이지 : ', page)

#차트 출력을 위해 데이터 프레임 구하기
df = df.dropna()
df = df.iloc[0:30]              #최근 데이터 30행 읽어온다.

#한글 컬럼명을 영문 컬럼명으로 변경
df = df.rename(columns={'날짜':'Date', '시가':'Open', '고가':'High', '저가':'Low',
                        '종가':'Close', '거래량':'Volume'})

#네이버 금융의 데이터가 내림차수능로 오름차순으로 변경
df = df.sort_values(by='Date')
df.index = pd.to_datetime(df.Date)
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

#mplfinance 로 캔들차트 그리기
# mpf.plot(df, title="Celltrion candle chart", type='candle')
#ohlc 차트 그리기
# mpf.plot(df, title="Celltrion candle chart", type='ohlc')


## kwargs 는  keyword arguments의 약자이며, 디셔너리이다.
kwargs = dict(title='Celltrion customized chart', type='candle',
              mav=(2,4,6), volume=True, ylabel='ohlc candles')

mc = mpf.make_marketcolors(up='r', down='b', inherit=True)
s = mpf.make_mpf_style(marketcolors=mc)

mpf.plot(df, **kwargs, style=s)