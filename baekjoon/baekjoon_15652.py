# N과 M (4)
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

nums = [n+1 for n in range(N)]

def permutation(nums, m):

    result = []
    for i in range(len(nums)):
        selected = nums[i]
        remains = nums[i:]

        if m > 1:
            next_permutation = permutation(remains, m-1)
            for element in next_permutation:
                result.append([selected]+element)
        else:
            result.append([selected])

    return result

result = permutation(nums, M)
for res in result:
    print(*res)