# 좋은 구간
"""
정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.

A와 B는 양의 정수이고, A < B를 만족한다.
A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.
"""
import sys

L = int(sys.stdin.readline().rstrip())
S = list(map(int, sys.stdin.readline().rstrip().split()))
N = int(sys.stdin.readline().rstrip())

S.sort()

start = 0
end = S[0]
for i in range(len(S) - 1):
    if start < N < end:
        break
    start = S[i]
    end = S[i+1]

if start < N < end:
    over_N = end - N
    over_start = N - start - 1
    print(over_start*over_N + (over_N-1))
else:
    print(0)




