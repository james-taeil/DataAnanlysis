#삼성전자, MS, sk하이닉스 종가 데이터를 그래프로 출력
#pip install matplotlib
#pip install yfinance
#pip install pandas_datareader


from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

sec = pdr.get_data_yahoo('005930.KS', start='2020-09-01')
msft = pdr.get_data_yahoo("MSFT", start='2020-09-01')
skhy = pdr.get_data_yahoo('000660.KS', start='2020-09-01')

plt.plot(sec.index, sec.Close, 'b', label="Samsung Electronic")
plt.plot(msft.index, msft.Close, 'r--', label="MicroSoft")
plt.plot(skhy.index, skhy.Close, 'g', label="SK hynix")
plt.legend(loc='best')
plt.show()

#문제점 // 삼성, 하이닉스는 '원' 인데 MS는 '달러'로 되어 비교하기가 어렵다.

