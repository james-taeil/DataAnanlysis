#일간변동률을 구하여 가격 단위가 다른 주가의 수익률을 비교
#오늘 변동률 = (오늘종가 - 어제종가)/어제종가 * 100

from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

#데이터 불러오기
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo("MSFT", start='2018-05-04')
skhy = pdr.get_data_yahoo('000660.KS', start='2018-05-04')

#변동률
sec_dpc = ((sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1)) * 100
msft_dpc = ((msft['Close'] - msft['Close'].shift(1)) / msft['Close'].shift(1)) * 100
skhy_dpc = ((skhy['Close'] - skhy['Close'].shift(1)) / skhy['Close'].shift(1)) * 100

# NaN값 0으로 변경
sec_dpc.iloc[0] = 0
msft_dpc.iloc[0] = 0
skhy_dpc.iloc[0] = 0

print('삼성전자 일간 변동률')
print(sec_dpc.head())

print('하이닉스 일간 변동률')
print(skhy_dpc.head())

print('MS 일간 변동률')
print(msft_dpc.head())


