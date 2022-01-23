# 합분해
"""
0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하는 프로그램을 작성하시오.

덧셈의 순서가 바뀐 경우는 다른 경우로 센다(1+2와 2+1은 서로 다른 경우).
또한 한 개의 수를 여러 번 쓸 수도 있다.
"""
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

memo = [[0 for _ in range(N+1)], [1 for _ in range(N+1)]]

for i in range(2, K+1):
    memo.append([1 for _ in range(N+1)])
    for k in range(1, N+1):
        memo[i][k] = (memo[i-1][k] + memo[i][k-1]) % 1000000000
print(memo[K][N])