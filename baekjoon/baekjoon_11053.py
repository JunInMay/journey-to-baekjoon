# 가장 긴 증가하는 부분 수열
"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.
"""
import sys

n = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
memo = [1 for _ in range(n)]

for i in range(1, n):
    maxi = float('-inf')
    for j in range(i):
        if sequence[i] > sequence[i-(j+1)]:
            maxi = max((memo[i-(j+1)]+1), maxi)
    memo[i] = maxi if maxi > 0 else 1
print(max(memo))

"""
12
10 20 10 30 20 50 15 16 17 18 19 20
"""