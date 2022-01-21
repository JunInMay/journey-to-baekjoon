# 별 찍기 - 8
"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
"""
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n*2-1):
    if i < n:
        print("*"*(i+1)+" "*(n-(i+1))*2+"*"*(i+1))
    else:
        print("*"*(n-((i+1)%n))+" "*((i+1)%n)*2+"*"*(n-((i+1)%n)))
