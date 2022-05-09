# 연도 진행바
"""
문빙이는 새해를 좋아한다. 하지만, 이제 새해는 너무 많이 남았다. 그래도 문빙이는 새해를 기다릴 것이다.
어느 날 문빙이는 잠에서 깨면서 스스로에게 물었다. “잠깐, 새해가 얼마나 남은거지?”

이 문제에 답하기 위해서 문빙이는 간단한 어플리케이션을 만들기로 했다.
연도 진행바라는 것인데, 이번 해가 얼마나 지났는지를 보여주는 것이다.
오늘 날짜가 주어진다. 이번 해가 몇%지났는지 출력하는 프로그램을 작성하시오.
"""
import sys
import datetime as dt
input_txt = sys.stdin.readline().rstrip()
M, D, Y, HM = input_txt.split()

now = dt.datetime.strptime(input_txt, "%B %d, %Y %H:%M")
start_year = dt.datetime.strptime(Y, "%Y")
next_year = dt.datetime.strptime(str(int(Y)+1), "%Y")
print((now - start_year).total_seconds()/(next_year - start_year).total_seconds()*100)

"""
May 10, 1981 00:31
May 10, 2028 00:31
"""