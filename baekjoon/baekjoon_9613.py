# GCD 합
"""
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.
"""
import sys

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for _ in range(int(sys.stdin.readline().rstrip())):
    case = list(map(int, sys.stdin.readline().rstrip().split()))
    gcdsum = 0
    for i in range(1, len(case)-1):
        for j in range(i+1, len(case)):
            a = gcd(case[i], case[j])
            gcdsum += a

    print(gcdsum)
