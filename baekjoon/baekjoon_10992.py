# 별 찍기 - 17
"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
"""
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    if i == 0:
        print(" "*(n-(i+1)) + "*")
    elif i != n-1:
        print(" "*(n-(i+1))+"*"+" "*(i*2-1)+"*")
    else:
        print("*"*((n*2)-1))