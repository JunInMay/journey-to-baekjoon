# 최대공약수
"""
모든 자리가 1로만 이루어져있는 두 자연수 A와 B가 주어진다.
이때, A와 B의 최대 공약수를 구하는 프로그램을 작성하시오.

예를 들어, A가 111이고, B가 1111인 경우에 A와 B의 최대공약수는 1이고,
A가 111이고, B가 111111인 경우에는 최대공약수가 111이다.
"""
import sys

def eucladian(li):
    A = li[0]
    B = li[1]
    while B:
        A, B = B, A%B
    return A

print(eucladian(list(map(int, sys.stdin.readline().rstrip().split())))*"1")