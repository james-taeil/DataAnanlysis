# import pandas as pd
# krx_list = pd.read_html("상장법인목록.xls")
# krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format) #6자리 수자중 빈자리 0으로 채움
# krx_list[0] = krx_list[0].sort_values(by='종목코드') #오름차순 정렬
# print(krx_list[0])


#다른방식
# import pandas as pd
# krx_list = pd.read_html('https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')
# krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)
# krx_list[0] = krx_list[0].sort_values(by='종목코드')    #오름차순 정렬
# print(krx_list[0])
#
#다른방식
# import pandas as pd
# df = pd.read_html('https://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13')
# df['종목코드'] = df['종목코드'].map('{:06d}'.format)
# krx_list[0] = krx_list[0].sort_values(by='종목코드')    #오름차순 정렬
# print(krx_list[0])


#함수 비교
# find_all(['검색할 태그'][, class_='클래스 속성값'][, id='아이디 속성값'][, limit='찾을 개수'])
# find(['검색할 태그'][, class_='클래스 속성값'][, id='아이디 속성값'])
