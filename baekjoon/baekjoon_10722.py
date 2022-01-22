# 가장 긴 감소하는 부분 수열
"""
수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에
가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.
"""
import sys
n = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
memo = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if sequence[i] < sequence[i-(j+1)]:
            memo[i] = max(memo[i], memo[i-(j+1)]+1)

print(max(memo))