# MDD(Maximum Drawdown,  최대손식낙폭) =
# 특정  기간에  발생한  최고점에서  최저점까지의  가장  큰 손실을 의미한다.

# 퀀트 투자에서는 수익률을 높이는 것보다 MDD를 낮추는 것이 더 중요하다. 특정 기간
# 동안 최대한 얼마의 손실이 일어날 수 있는지를 나타낸다.

# MDD = (최저점  - 최고점) / 최저점

from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()

#KOSPI 지수의 심볼은 ^KS11
kospi = pdr.get_data_yahoo('^KS11', '2004-01-04')

#산정 기간에 해당하는 window값은 1년동안 개장일을 252 일로 설정
window = 252

#KOSPI 종가 컬럼에서 1년 기간 단위로 최고치 peak를 궇마
peak = kospi['Adj Close'].rolling(window, min_periods=1).max()

#drawdown은 최고치 대피 현재 KOSPI 종가가 얼마나 하락 했는지 구한다.
drawdown = kospi['Adj Close']/peak - 1.0

#drawdown에서 1년 기간단위로 최저치 min_dd 를 구한다.
#마이너스값이기 때문에 최저치가 바로 최대 손실 낙폭이 된다.
max_dd = drawdown.rolling(window, min_periods=1).min()

print(max_dd.min()) #MDD 최저치

plt.figure(figsize=(9,7))
plt.subplot(211)
kospi['Close'].plot(label="KOSPI", title="KOSPI MDD", grid=True, legend=True)
plt.subplot(212)
drawdown.plot(c= 'blue', label="KOSPI DD", grid=True, legend=True)
max_dd.plot(c= 'red', label="KOSPI DD", grid=True, legend=True)
plt.show()

print(max_dd[max_dd == -0.5453665130144085])