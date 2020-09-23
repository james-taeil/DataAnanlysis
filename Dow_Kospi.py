#다우존스 코스피 지수 비교

#회귀분석 상관관계

from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')   #2000년 이후 코스피 지수
dow = pdr.get_data_yahoo('^DJI', '2000-01-04')      #2000년 이후 다우존스 지수

plt.figure(figsize=(9,7))
plt.plot(dow.index, dow.Close, 'b', label="Dow Jones Industrial")   #푸른 실선
plt.plot(kospi.index, kospi.Close, 'r--', label="KOSPI")            #붉은 점선
plt.legend(loc='best')
plt.grid(True)
plt.show()