from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

#데이터 불러오기 //
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo("MSFT", start='2018-05-04')
skhy = pdr.get_data_yahoo('000660.KS', start='2018-05-04')
naver = pdr.get_data_yahoo('035420.KS', start='2018-05-04')
kakao = pdr.get_data_yahoo('035720.KS', start='2018-05-04')


sec_dpc = ((sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1)) * 100
msft_dpc = ((msft['Close'] - msft['Close'].shift(1)) / msft['Close'].shift(1)) * 100
skhy_dpc = ((skhy['Close'] - skhy['Close'].shift(1)) / skhy['Close'].shift(1)) * 100
naver_dpc = ((naver['Close'] - naver['Close'].shift(1)) / naver['Close'].shift(1)) * 100
kakao_dpc = ((kakao['Close'] - kakao['Close'].shift(1)) / kakao['Close'].shift(1)) * 100


#일간 변동률 누적합
sec_dpc_cs = sec_dpc.cumsum()       #18년 5월 ~ 20년 9월 19.6% 이익률
msft_dpc_cs = msft_dpc.cumsum()     #18년 5월 ~ 20년 9월 92% 이익률
skhy_dpc_cs = skhy_dpc.cumsum()     #18년 5월 ~ 20년 9월 13% 이익률
naver_dpc_cs = naver_dpc.cumsum()   #18년 5월 ~ 20년 9월 84% 이익률
kakao_dpc_cs = kakao_dpc.cumsum()   #18년 5월 ~ 20년 9월 130% 이익률

print(sec_dpc_cs)
print(msft_dpc_cs)
print(skhy_dpc_cs)
print(naver_dpc_cs)
print(kakao_dpc_cs)