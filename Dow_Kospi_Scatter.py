#산점도 분석
#산점도란 독립 변수  x 와 종속 변수  y 의 상관관계를 확인할 때 사용하는 그래프
#가로축은 독립 변수  x , 세로축은 종속 변수 y

import pandas as pd
from  pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')   #2000년 이후 코스피 지수
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')      #2000년 이후 다우존스 지수

df = pd.DataFrame({'DOW':dow['Close'], "KOSPI":kospi['Close']})
#fillna()함수를 사용하여 NaN 를 채울 수 있는데, 인수로  bfill(backward fill)이면 NaN 뒤에
df = df.fillna(method='bfill')
#마지막 행에 NaN 이 있으면  ffill(forward fill) 인수로  fillna() 함수를 한 번 더 호출함으로써 제일 마지막 행의 NaN 을 덮어써 제거
df = df.fillna(method='ffill')

plt.figure(figsize=(9,7))
plt.scatter(df['DOW'], df['KOSPI'], marker='.')
plt.xlabel("Dow jones Industrial Average")
plt.ylabel("KOSPI")
plt.show()