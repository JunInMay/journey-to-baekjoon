# 오르막 수
"""
오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.

예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.

수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.
"""
import sys

n = int(sys.stdin.readline().rstrip())
memo = [[0 for i in range(10)], [1 for i in range(10)]]
for i in range(2, n+1):
    temp = []
    for j in range(10):
        sum_of_nums = 0
        for k in range(j+1):
            sum_of_nums += memo[i-1][k]
        temp.append(sum_of_nums)
    memo.append(temp)
print(sum(memo[n])%10007)