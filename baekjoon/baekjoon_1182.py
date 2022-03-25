# 부분수열의 합
"""
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

N, S = map(int, sys.stdin.readline().rstrip().split())
sequence = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
result = 0


def dfs(idx, selected):
    global result
    s = sum(selected)
    if s == S:
        result += 1

    for i in range(idx+1, N):

        selected.append(sequence[i])
        dfs(i, selected)
        selected.pop()

    return None

for i in range(N):
    dfs(i, deque([sequence[i]]))

print(result)