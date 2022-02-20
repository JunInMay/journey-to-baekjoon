# 숫자 카드 2
"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
"""
"""
# 4464ms 통과 코드
# 이분 탐색 2회로 풀었으나 사실 이 문제에서 pypy가 아니라 파이썬으로 이분탐색 2회 돌리면 시간이 간당간당 함.
# 논리적으론 이분 탐색 2회 돌리면 O(Mlgn) 선에서 정리되는데 내부 코드의 세밀한 최적화가 필요함

import sys

N = int(sys.stdin.readline().rstrip())
have = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
cases = list(map(int, sys.stdin.readline().rstrip().split()))
count = [0 for _ in range(M)]

def binary_serach(candidate, func):
    ceil = N - 1
    floor = 0
    while ceil >= floor:
        mid = (floor + ceil) // 2
        if func:
            if have[mid] >= candidate:
                ceil = mid - 1
            else:
                floor = mid + 1
        else:
            if have[mid] <= candidate:
                floor = mid + 1
            else:
                ceil = mid - 1
    return ceil


for i in range(M):
    candidate = cases[i]

    count[i] = binary_serach(candidate, 0) - binary_serach(candidate, 1)
print(*count)
"""
# 해시맵? 활용한 코드, 4500ms python 통과 코드
# 이분탐색은 1회밖에 안돌지만 결국 얘도 O(Mlgn)
# 그 대신 내부 자잘자잘한 최적화엔 신경 크게 안써도 되는듯 하다. 그냥 PS에선 C++을 쓰자. 근데... 파이썬이 손에 익긴 한데..
# 언제 C++ 출력부터 벡터? 까지 배우고 있나 막막하다
import sys

N = int(sys.stdin.readline().rstrip())
have = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
memo = {}
for elem in have:
    memo[elem] = memo.get(elem, 0) + 1

M = int(sys.stdin.readline().rstrip())
cases = list(map(int, sys.stdin.readline().rstrip().split()))
count = [0 for _ in range(M)]

for i in range(M):
    candidate = cases[i]
    ceil = N-1
    floor = 0
    while ceil >= floor:
        mid = (ceil + floor) // 2
        if have[mid] == candidate:
            count[i] = memo[candidate]
            break
        elif have[mid] < candidate:
            floor = mid + 1
        else:
            ceil = mid - 1
print(*count)


"""
1
1
3
1 1 1
"""