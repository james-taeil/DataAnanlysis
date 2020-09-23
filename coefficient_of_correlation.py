#상관계수

import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf


yf.pdr_override()

kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')   #2000년 이후 코스피 지수
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')      #2000년 이후 다우존스 지수

df = pd.DataFrame({'DOW':dow['Close'], "KOSPI":kospi['Close']})

print(df.corr())

#시리즈 상관관계 구하기
print(df['DOW'].corr(df['KOSPI'])) #df.DOW.corr(df.KOSPI)

#결정계수
r_value = df['DOW'].corr(df['KOSPI'])
print(r_value)

r_squared = r_value ** 2
print(r_squared)