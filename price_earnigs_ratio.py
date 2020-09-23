from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

#데이터 불러오기 //
sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')
msft = pdr.get_data_yahoo("MSFT", start='2018-05-04')
skhy = pdr.get_data_yahoo('000660.KS', start='2018-05-04')
naver = pdr.get_data_yahoo('035420.KS', start='2018-05-04')
kakao = pdr.get_data_yahoo('035720.KS', start='2018-05-04')

#변동률
sec_dpc = ((sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1)) * 100
msft_dpc = ((msft['Close'] - msft['Close'].shift(1)) / msft['Close'].shift(1)) * 100
skhy_dpc = ((skhy['Close'] - skhy['Close'].shift(1)) / skhy['Close'].shift(1)) * 100
naver_dpc = ((naver['Close'] - naver['Close'].shift(1)) / naver['Close'].shift(1)) * 100
kakao_dpc = ((kakao['Close'] - kakao['Close'].shift(1)) / kakao['Close'].shift(1)) * 100

# NaN값 0으로 변경
sec_dpc.iloc[0] = 0
msft_dpc.iloc[0] = 0
skhy_dpc.iloc[0] = 0
naver_dpc.iloc[0] = 0
kakao_dpc.iloc[0] = 0

#일간 변동률 누적합
sec_dpc_cs = sec_dpc.cumsum()       #18년 5월 ~ 20년 9월 19.6% 이익률
msft_dpc_cs = msft_dpc.cumsum()     #18년 5월 ~ 20년 9월 92% 이익률
skhy_dpc_cs = skhy_dpc.cumsum()     #18년 5월 ~ 20년 9월 13% 이익률
naver_dpc_cs = naver_dpc.cumsum()   #18년 5월 ~ 20년 9월 84% 이익률
kakao_dpc_cs = kakao_dpc.cumsum()   #18년 5월 ~ 20년 9월 130% 이익률
#문제점 // 하락한 부분에서 반등한 부분까지 총합이므로 결과값이 이상하게 나온다..

#첫날 대비 현재가에 증가율을 구해야 하므로 오늘 종가 - 구매 첫날 종가/구매 첫날 종가 * 100을 해야한다.
sec_dpc2 = ((sec['Close'][-1] - sec['Close'][0]) / sec['Close'][0]) * 100
msft_dpc2 = ((msft['Close'][-1] - msft['Close'][0]) / msft['Close'][0]) * 100



#두개 기업 비교 // 삼성 vs ms
plt.plot(sec.index, sec_dpc_cs2, 'b', label="Samsung Electronic")
plt.plot(msft.index, msft_dpc_cs, 'r--', label="MicroSoft")
plt.ylabel('Change %')
plt.grid(True)
plt.show()

#네이버 카카오
plt.plot(naver.index, naver_dpc_cs, 'b', label="Naver")
plt.plot(kakao.index, kakao_dpc_cs, 'r--', label="KaKao")
plt.ylabel('Change %')
plt.grid(True)
plt.show()


