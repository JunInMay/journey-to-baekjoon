# 소수 찾기
"""
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
"""
import sys

n = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0

for num in nums:
    if num <= 1:
        count += 1
        continue
    for i in range(2, num):
        if num % i == 0:
            count += 1
            break
print(len(nums)-count)