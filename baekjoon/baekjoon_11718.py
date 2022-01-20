# 그대로 출력하기
"""
입력 받은 대로 출력하는 프로그램을 작성하시오.
"""
import sys

n = 0
while n <= 99:
    print(sys.stdin.readline().rstrip())
    n += 1