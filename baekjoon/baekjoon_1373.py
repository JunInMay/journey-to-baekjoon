# 2진수 8진수
"""
2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.
"""
import sys

input = sys.stdin.readline().rstrip()

result = []
temp = 0
for i in range(len(input)):
    temp += int(input[-(i+1)]) * 2**(i%3)
    if i == (len(input)-1) or i%3 == 2:
        result.append(temp)
        temp = 0

print("".join(map(str, (result[::-1]))))