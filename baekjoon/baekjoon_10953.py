# A+B - 6
"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""
import sys
case = [list(map(int, sys.stdin.readline().rstrip().split(','))) for i in range(int(sys.stdin.readline().rstrip()))]
for a, b in case:
    print(a+b)