#사이파이 선형 회귀 분석
#수학적  알고리즘의  모음으로  NumPy,  Matplotlib, SymPy, Pandas

#선형 회귀 분석
# Yi : i 번째 종속 변수의 값
# Xi : i 번째 독립 변수의 값
# β0 : 선형 회귀의 절편(intercept)
# β1 : 선형 회귀의 기울기(slope)
# εi : 오차항(종속 변수  Y 의 살제값과 기대치의 차이)

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from scipy import stats

yf.pdr_override()

kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')   #2000년 이후 코스피 지수
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')      #2000년 이후 다우존스 지수

# 다우존스 지수의 종가 컬럼과 KOSPI 지수의 종가 컬럼으로 데이터 프레임 생성
df = pd.DataFrame({'DOW':dow['Close'], "KOSPI":kospi['Close']})

#데이터 프레임에서 모든 NaN 제거
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

regr = stats.linregress(df['DOW'], df['KOSPI'])
print(regr)

# slope=0.07862139555155277         # 기울기
# intercept=436.1412263116106       # y절편
# rvalue=0.7450621981837547         # r값(상관계수)
# pvalue=0.0                        # p값
# stderr=0.0009635247667761696      # 표준편차



