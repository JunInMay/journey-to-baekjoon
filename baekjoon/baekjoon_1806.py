# 부분합
"""
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다.
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
"""
import sys

N, G = map(int, sys.stdin.readline().rstrip().split())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))

start = end = 0
tempSum = 0
results = []

while not(start == end == N):

    if tempSum >= G:
        results.append(end-start)

    if tempSum < G and end < N:
        tempSum += sequence[end]
        end += 1
    else:
        tempSum -= sequence[start]
        start += 1

if len(results) > 0:
    print(min(results))
else:
    print(0)

"""
  10  15              
  5 1 3 5 10    7 4 9 2 8                
"""