# 가장 큰 증가 부분 수열
"""
수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에
합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.
"""
import sys
n = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
memo = [sequence[0]]

for i in range(1, n):
    temp = float("-inf")
    for j in range(i):
        if sequence[i-(j+1)] < sequence[i]:
            temp = max(temp, memo[i-(j+1)] + sequence[i])
    if temp > 0:
        memo.append(temp)
    else:
        memo.append(sequence[i])
print(max(memo))