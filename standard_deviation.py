from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

#데이터 불러오기 //
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo("MSFT", start='2018-05-04')
skhy = pdr.get_data_yahoo('000660.KS', start='2018-05-04')

#변동률
sec_dpc = ((sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1)) * 100
msft_dpc = ((msft['Close'] - msft['Close'].shift(1)) / msft['Close'].shift(1)) * 100
skhy_dpc = ((skhy['Close'] - skhy['Close'].shift(1)) / skhy['Close'].shift(1)) * 100

sec_dpc2 = ((sec['Close'][-1] - sec['Close'][0]) / sec['Close'][0]) * 100


# NaN값 0으로 변경
sec_dpc.iloc[0] = 0
msft_dpc.iloc[0] = 0
skhy_dpc.iloc[0] = 0

print(sec_dpc2)