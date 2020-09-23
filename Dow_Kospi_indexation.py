#지수화 비교
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

kospi = pdr.get_data_yahoo('^KS11', '2000-01-04')   #2000년 이후 코스피 지수
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')      #2000년 이후 다우존스 지수

d = (dow.Close / dow.Close.loc['2000-01-04']) * 100
k = (kospi.Close / kospi.Close.loc['2000-01-04']) * 100

plt.figure(figsize=(9,7))
plt.plot(dow.index, d, 'b', label="Dow Jones Industrial")   #푸른 실선
plt.plot(kospi.index, k, 'r--', label="KOSPI")              #붉은 점선
plt.legend(loc='best')
plt.grid(True)
plt.show()
#결과 다우존스 지수와 상승률이 비슷함