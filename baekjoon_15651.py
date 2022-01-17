# N과 M (3)
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
init_list = [n+1 for n in range(N)]

def permutation(nums, M):
    result = []
    for i in range(len(nums)):
        selected = nums[i]
        if M > 1:
            next_cases = permutation(nums, M-1)
            for case in next_cases:
                result.append([selected]+case)
        else:
            result.append([selected])

    return result

result = permutation(init_list, M)

for line in result:
    print(*line)