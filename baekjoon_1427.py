# 소트인사이드
"""
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
"""
import sys

n = list(map(int, sys.stdin.readline().rstrip()))

def counting_sort(nums):
    count = [0 for _ in range(10)]
    result = ""

    for num in nums:
        count[num] += 1
    for i in range(len(count)):
        for _ in range(count[len(count)-1-i]):
            result += str(len(count)-1-i)

    return result
print(counting_sort(n))