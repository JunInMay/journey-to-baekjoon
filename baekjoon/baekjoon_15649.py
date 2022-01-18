# N과 M (1)
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
"""
import sys

n, count = list(map(int, sys.stdin.readline().rstrip().split()))
init_list = []
for i in range(n):
    init_list.append(i+1)

def permutation(nums, r):
    result = []
    size = len(nums)

    for i in range(size):
        selected = nums[i]
        remains = nums[:i] + nums[i+1:]
        if r > 1:
            next_permutation = permutation(remains, r-1)
            for element in next_permutation:
                result.append([selected]+element)
        else:
            result.append([selected])
    return result

result = permutation(init_list, count)
for line in result:
    text = ""
    for element in line:
        text += str(element) + " "
    print(text.rstrip())