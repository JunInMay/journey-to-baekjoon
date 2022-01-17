# 소인수분해
"""
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
"""
import sys
n = int(sys.stdin.readline().rstrip())

result = []

if n != 1:
    prime = 2
    while n != 1:
        if n % prime > 0:
            prime+=1
        else:
            result.append(prime)
            n = int(n / prime)
    for res in result:
        print(res)
else:
    pass