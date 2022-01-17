# N과 M (2)
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
고른 수열은 오름차순이어야 한다.
"""
import sys
N, M = map(int, sys.stdin.readline().rstrip().split())
nums = [n+1 for n in range(N)]

def permutation(nums, M):
    result = []
    l = len(nums)

    for i in range(l-M+1):
        selected = nums[i]

        if M != 1:
            remains = nums[i+1:]
            next_cases = permutation(remains, M-1)

            for case in next_cases:
                result.append([selected]+case)

        else:
            result.append([selected])

    return result

result = permutation(nums, M)
for case in result:
    print(*case)