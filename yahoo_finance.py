# 주식 시세를 구하는 get_data_yahoo() 함수 만들기
# 야후 finance에서 삼성전자(005930.KS)와 마이크로소프트(MSFT)의 주식 데이터 가져오기
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

sec = pdr.get_data_yahoo('005930.KS', start='2020-09-01')
msft = pdr.get_data_yahoo("MSFT", start='2020-09-01')
skhy = pdr.get_data_yahoo('000660.KS', start='2020-09-01')

# print(sec.head())

tmp_msft = msft.drop(columns='Volume')
tmp_sec = sec.drop(columns='Volume')
tmp_skhy = skhy.drop(columns="Volume")

# print(tmp_msft)
# print(tmp_sec)
# print(tmp_skhy)

#제일 뒤 5개 컬럼 출력
# print(tmp_msft.tail())
# print('='*80)
# print(tmp_sec.tail())
# print('='*80)
# print(tmp_skhy.tail())

print(skhy.index)
print('='*80)
print(skhy.columns)

