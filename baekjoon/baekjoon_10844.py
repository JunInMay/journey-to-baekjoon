# 쉬운 계단 수
"""
45656이란 수를 보자.
이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.
N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구해보자. 0으로 시작하는 수는 계단수가 아니다.
"""
import sys
n = int(sys.stdin.readline().rstrip())
memo = [[0 for _ in range(10)], [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

for i in range(2, n+1):
    before = memo[i-1]
    temp = [before[1],
            before[0]+before[2],
            before[1]+before[3],
            before[2]+before[4],
            before[3]+before[5],
            before[4]+before[6],
            before[5]+before[7],
            before[6]+before[8],
            before[7]+before[9],
            before[8]]
    memo.append(temp)
print(sum(memo[n])%1000000000)