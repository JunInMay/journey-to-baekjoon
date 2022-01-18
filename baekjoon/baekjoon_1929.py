# 소수 구하기
"""
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
"""
"""
에라토스테네스의 체를 활용하여 구현
"""
import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
nums = [True for _ in range(N-M+1)]
if M == 1:
    nums[0] = False

for i in range(2, round(N**(1/2))+1 if round(N**(1/2))+1 > 2 else 3):
    index = i-M
    prime_checked = 0
    while index <= N:
        if index >= 0 and index < len(nums) and prime_checked == 1:
            nums[index] = False
        prime_checked = 1
        index = index + prime_checked*i

for i in range(len(nums)):
    if nums[i]:
        print(M+i)