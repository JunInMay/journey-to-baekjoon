# 곱셈
"""
자연수 A를 B번 곱한 수를 알고 싶다. 단 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
"""
import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())
def recursive_Power(n, p):
    if p == 0: return 1
    elif p == 1: return n%C

    result = recursive_Power(n, p//2)
    if p % 2 == 0:
        return result*result%C
    else:
        return result*result*n%C

print(recursive_Power(A, B))