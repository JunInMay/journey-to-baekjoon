# 숫자 카드
"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
"""
import sys
N = int(sys.stdin.readline().rstrip())
what_i_got = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())
what_they_got = list(map(int, sys.stdin.readline().rstrip().split()))
checked = [0 for _ in range(M)]

def check():
    for i in range(M):
        candidate = what_they_got[i]
        floor = 0
        ceil = N
        while floor <= ceil:
            mid = (floor + ceil) // 2
            if mid >= N:
                break
            if what_i_got[mid] == candidate:
                checked[i] = 1
                break
            elif what_i_got[mid] > candidate:
                ceil = mid - 1
            else:
                floor = mid + 1

check()
print(*checked)
"""
1
1
1
2

3
1 2 3
3
3 2 1
"""