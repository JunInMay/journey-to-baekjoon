# 분수찾기
"""
무한히 큰 배열에 다음과 같이 분수들이 적혀있다.

1/1	1/2	1/3	1/4	1/5	…
2/1	2/2	2/3	2/4	…	…
3/1	3/2	3/3	…	…	…
4/1	4/2	…	…	…	…
5/1	…	…	…	…	…
…	…	…	…	…	…
이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
"""
import sys

num = int(sys.stdin.readline().rstrip())

order_in_line = num
line = 0

while order_in_line > 0:
    line += 1
    order_in_line -= line

cal_times = line+order_in_line-1

if line % 2 == 0:
    mother = line
    son = 1
    mother = line - cal_times
    son = 1 + cal_times
else:
    mother = 1
    son = line
    mother = 1 + cal_times
    son = line - cal_times

print(f"{son}/{mother}")