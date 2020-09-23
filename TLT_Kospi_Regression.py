import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

import matplotlib.pylab as plt
from scipy import stats

yf.pdr_override()

tlt = pdr.get_data_yahoo("TLT", "2002-07-30")       #TLT 다운로드
kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')   #2000년 이후 코스피 지수

# 다우존스 지수의 종가 컬럼과 KOSPI 지수의 종가 컬럼으로 데이터 프레임 생성
df = pd.DataFrame({'X':tlt['Close'], "Y":kospi['Close']})       #tlt X컬럼, KOSPI Y컬럼

#데이터 프레임에서 모든 NaN 제거
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

regr = stats.linregress(df.X, df.Y)                 #선형회귀모델객체 regr 생성
regr_line = f'Y = {regr.slope:.2f}  X + {regr.intercept:.2f}'   #범례에 회귀선을 표시하는 문자

plt.figure(figsize=(7,7))
plt.plot(df.X, df.Y, '*') #산점도를 *으로 표시
plt.plot(df.X, regr.slope * df.X + regr.intercept, 'r')
plt.legend(['TLT x KOSPI', regr_line])
plt.title(f'TLT x KOSPI (R = {regr.rvalue:.2f})')
plt.xlabel("iShares Barclays 20 + Yr Treas.Bond(TLT)")
plt.ylabel("KOSPI")
plt.show()

