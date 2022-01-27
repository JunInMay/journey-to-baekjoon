# 8진수 2진수
"""
8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.
"""
import sys

input = sys.stdin.readline().rstrip()

result = []
for i in range(len(input)):
    ti = int(input[-(i+1)])
    temp = []
    while ti > 0:
        temp.append(ti % 2)
        ti //= 2
    if len(temp) < 3 and i != len(input)-1:
        while len(temp) < 3:
            temp.append(0)
    result += temp
if input == "0": result = [0]

print("".join(map(str, result[::-1])))