# 배수들의 합
"""
신원이는 백준에서 배수에 관한 문제를 풀다가 감명을 받아 새로운 문제를 만들어보았다.
자연수 N과 M개의 자연수 Ki가 주어진다. Ki중 적어도 하나의 배수이면서 1 이상 N 이하인 수의 합을 구하여라.
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
candidates = list(map(int, sys.stdin.readline().rstrip().split()))
sieve = [False for _ in range(N + 1)]
result = 0

for candidate in candidates:
    if sieve[candidate]:
        continue
    else:
        for i in range(candidate, N + 1, candidate):
            sieve[i] = True

for i in range(len(sieve)):
    if sieve[i]:
        result += i

print(result)
