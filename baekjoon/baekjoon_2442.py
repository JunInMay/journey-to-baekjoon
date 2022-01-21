# 별 찍기 - 5
"""
첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제
별은 가운데를 기준으로 대칭이어야 한다.
"""
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    print(" "*(n-i-1)+"*"*(1+(i*2)))