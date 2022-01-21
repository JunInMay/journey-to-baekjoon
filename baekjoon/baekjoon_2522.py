# 별 찍기 - 12
"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
"""
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n*2-1):
    if i < n-1:
        print(" "*(n-(i+1))+"*"*(i+1))
    else:
        print(" "*((i+1)%n)+"*"*(n-(i+1)%n))