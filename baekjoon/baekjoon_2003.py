# 수들의 합 2
"""
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다.
이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""
import sys

N, G = map(int, sys.stdin.readline().rstrip().split())

sequence = list(map(int, sys.stdin.readline().rstrip().split()))

start = end = 0
result = 0
s = 0

while not(start == end == N):
    if s < G and end < N:
        s += sequence[end]
        end += 1
    else:
        s -= sequence[start]
        start += 1

    if s == G:
        result += 1

print(result)